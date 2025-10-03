import json
from datasets import load_dataset


if __name__ == "__main__":
    # load all data
    dataset = load_dataset("mkieffer/MMLU-Pro-Health")

    # load only test split
    dataset_test = load_dataset("mkieffer/MMLU-Pro-Health", split="test")

    # load only validation split
    dataset_val = load_dataset("mkieffer/MMLU-Pro-Health", split="validation")

    print("\nfull dataset:\n", dataset)
    print("\test split:\n", dataset_test)
    print("\validation split:\n", dataset_val)

    print("\test sample:\n", json.dumps(dataset_test[0], indent=2))
    print("\validation sample:\n", json.dumps(dataset_val[0], indent=2))