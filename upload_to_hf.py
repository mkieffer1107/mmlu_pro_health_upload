#!/usr/bin/env python3
import os
import json
import argparse

from datasets import DatasetDict, load_dataset, concatenate_datasets
from huggingface_hub import create_repo

def str_to_bool(v: str) -> bool:
    return str(v).strip().lower() in {"1", "true", "t", "yes", "y"}

parser = argparse.ArgumentParser(description="Format Medbullets data and push to HF with aligned splits")
parser.add_argument("--hf_username", default=os.environ.get("HF_USERNAME", "mkieffer"))
parser.add_argument("--hf_repo_name", default=os.environ.get("HF_REPO_NAME", "Medbullets"))
parser.add_argument("--private", default=os.environ.get("PRIVATE", "false"),
                    help="Whether the HF dataset repo should be private (true/false)")
parser.add_argument("--eval_frac", type=float, default=float(os.environ.get("EVAL_FRAC", 0.20)),
                    help="Fraction of each split to put in eval (default 0.20)")
args = parser.parse_args()

HF_USERNAME = args.hf_username
HF_REPO_NAME = args.hf_repo_name
PRIVATE = str_to_bool(args.private)
EVAL_FRAC = float(args.eval_frac)
HF_REPO_ID = f"{HF_USERNAME}/{HF_REPO_NAME}"

DATA_DIR = "data"
OUT_DIR = "output"
os.makedirs(OUT_DIR, exist_ok=True)

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def preprocess(example):
    # Convert options from list to dict
    if isinstance(example["options"], list):
        letters = [chr(65 + i) for i in range(len(example["options"]))]
        example["options"] = {letter: text for letter, text in zip(letters, example["options"])}
    
    # Remove unwanted fields
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

    # exclude questions that aren't related to health
    excluded_ids = set()
    with open("problem_ids.json", "r") as f:
        data = json.load(f)
        # excluded_ids.update(data["unrelated"])
        # excluded_ids.update(data["fact_or_stat_that_could_change"])
        # excluded_ids.update(data["tangentially_related"])
        # excluded_ids.update(data["answer_format_wrong"])
        # excluded_ids.update(data["weird_questions"])
        for pair in data.get("duplicates", []):
            if len(pair) == 2:
                excluded_ids.add(pair[1])

    # combine them into one dataset
    combined = concatenate_datasets([health_dataset["test"], health_dataset["validation"]])

    print(f"Combined dataset before filtering num_rows: {combined.num_rows}")
    combined = combined.filter(lambda ex: ex["question_id"] not in excluded_ids)
    combined = combined.map(preprocess)
    print(f"Combined dataset after filtering num_rows: {combined.num_rows}")


    # 80/20 split
    dataset = combined.train_test_split(test_size=EVAL_FRAC, seed=12345)
    print(f"Train num_rows: {dataset['train'].num_rows}")
    print(f"Test num_rows: {dataset['test'].num_rows}")

    combined_path = os.path.join(OUT_DIR, "combined_health.json")
    train_path = os.path.join(OUT_DIR, "train_health.json")
    test_path = os.path.join(OUT_DIR, "test_health.json")

    save_json(combined.to_list(), combined_path)
    print(f"Saved combined dataset to: {combined_path}")
    
    save_json(dataset["train"].to_list(), train_path)
    print(f"Saved train dataset to: {train_path}")
    
    save_json(dataset["test"].to_list(), test_path)
    print(f"Saved test dataset to: {test_path}")

    # print(f"\nPushing dataset to Hugging Face Hub as {HF_REPO_ID} (private={PRIVATE})...")
    # create_repo(HF_REPO_ID, repo_type="dataset", private=PRIVATE, exist_ok=True)


    # dataset.push_to_hub(HF_REPO_ID, private=PRIVATE)
    # print(f"Dataset pushed to https://huggingface.co/datasets/{HF_REPO_ID}")