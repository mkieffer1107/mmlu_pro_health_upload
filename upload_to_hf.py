#!/usr/bin/env python3
import os
import json
import argparse

from datasets import Dataset, DatasetDict, Features, Value, load_dataset, concatenate_datasets
from huggingface_hub import create_repo

def str_to_bool(v: str) -> bool:
    return str(v).strip().lower() in {"1", "true", "t", "yes", "y"}

parser = argparse.ArgumentParser(description="Format Medbullets data and push to HF with aligned splits")
parser.add_argument("--hf_username", default=os.environ.get("HF_USERNAME", "mkieffer"))
parser.add_argument("--hf_repo_name", default=os.environ.get("HF_REPO_NAME", "Medbullets"))
parser.add_argument("--private", default=os.environ.get("PRIVATE", "false"),
                    help="Whether the HF dataset repo should be private (true/false)")
args = parser.parse_args()

HF_USERNAME = args.hf_username
HF_REPO_NAME = args.hf_repo_name
PRIVATE = str_to_bool(args.private)
HF_REPO_ID = f"{HF_USERNAME}/{HF_REPO_NAME}"

DATA_DIR = "data"
OUT_DIR = "output"
os.makedirs(OUT_DIR, exist_ok=True)

OPTION_KEYS = [chr(65 + i) for i in range(10)]
OPTIONS_FEATURE = {key: Value("string") for key in OPTION_KEYS}
DATASET_FEATURES = Features({
    "question_id": Value("int64"),
    "question": Value("string"),
    "options": OPTIONS_FEATURE,
    "answer": Value("string"),
    "cot_content": Value("string"),
    "src": Value("string"),
})

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def as_option_dict(options):
    formatted = {key: "" for key in OPTION_KEYS}

    if options is None:
        return formatted

    if isinstance(options, dict):
        for key, value in options.items():
            normalized_key = str(key).strip().upper()
            if normalized_key in formatted:
                formatted[normalized_key] = "" if value is None else str(value)
        return formatted

    for index, value in enumerate(options):
        if index >= len(OPTION_KEYS):
            break
        formatted[OPTION_KEYS[index]] = "" if value is None else str(value)

    return formatted


def preprocess(example):
    example["options"] = as_option_dict(example.get("options"))

    for key in ("question", "answer", "cot_content", "src"):
        value = example.get(key)
        example[key] = "" if value is None else str(value)

    question_id = example.get("question_id")
    try:
        example["question_id"] = int(question_id)
    except (TypeError, ValueError):
        example["question_id"] = -1

    example.pop("answer_index", None)
    example.pop("category", None)
    return example

if __name__ == "__main__":
    dataset = load_dataset("TIGER-Lab/MMLU-Pro") 

    # filter for health category only
    def is_health(ex):
        return ex["category"].strip().lower() == "health"

    health_dataset = DatasetDict({split: ds.filter(is_health) for split, ds in dataset.items()})
            
    print("test num_rows:", health_dataset["test"].num_rows)
    print("validation num_rows:", health_dataset["validation"].num_rows)

    # exclude questions flagged in problem_ids.json with precedence rules
    exclusion_config = load_json("problem_ids.json")

    superset_ids = set()
    excluded_ids = set()

    def _ensure_int(value):
        try:
            return int(value)
        except (TypeError, ValueError):
            return None

    supersets_cfg = exclusion_config.get("supersets", {})
    for superset_id_str, subset_ids in supersets_cfg.items():
        superset_id = _ensure_int(superset_id_str)
        if superset_id is None:
            continue
        superset_ids.add(superset_id)
        for subset_id in subset_ids or []:
            subset = _ensure_int(subset_id)
            if subset is not None:
                excluded_ids.add(subset)

    for category in [
        "unrelated",
        "fact_or_stat_that_could_change",
        "tangentially_related",
        "answer_format_wrong",
        "weird_questions",
    ]:
        for problem_id in exclusion_config.get(category, []):
            normalized = _ensure_int(problem_id)
            if normalized is not None:
                excluded_ids.add(normalized)

    for pair in exclusion_config.get("duplicates", []):
        if not pair:
            continue
        for duplicate_id in pair[1:]:
            normalized = _ensure_int(duplicate_id)
            if normalized is not None:
                excluded_ids.add(normalized)

    excluded_ids.difference_update(superset_ids)

    print(f"Excluding {len(excluded_ids)} question ids based on problem_ids.json.")

    filtered_splits = {}
    for split, split_dataset in health_dataset.items():
        before_rows = split_dataset.num_rows
        filtered = split_dataset.filter(lambda ex: ex["question_id"] not in excluded_ids)
        filtered = filtered.map(preprocess)
        filtered = filtered.cast(DATASET_FEATURES)
        filtered = Dataset.from_list(filtered.to_list(), features=DATASET_FEATURES)
        print(f"{split} num_rows after filtering: {filtered.num_rows} (from {before_rows})")
        filtered_splits[split] = filtered

    filtered_dataset = DatasetDict(filtered_splits)
    combined = concatenate_datasets(list(filtered_dataset.values())) if filtered_splits else None

    combined_path = os.path.join(OUT_DIR, "combined_health.json")
    if combined is not None:
        save_json(combined.to_list(), combined_path)
        print(f"Saved combined dataset to: {combined_path}")
    else:
        print("No data available to save to combined dataset.")

    for split, split_dataset in filtered_dataset.items():
        split_path = os.path.join(OUT_DIR, f"{split}_health.json")
        save_json(split_dataset.to_list(), split_path)
        print(f"Saved {split} dataset to: {split_path}")

    print(f"\nPushing dataset to Hugging Face Hub as {HF_REPO_ID} (private={PRIVATE})...")
    create_repo(HF_REPO_ID, repo_type="dataset", private=PRIVATE, exist_ok=True)


    filtered_dataset.push_to_hub(HF_REPO_ID, private=PRIVATE)
    print(f"Dataset pushed to https://huggingface.co/datasets/{HF_REPO_ID}")