import json
from datasets import load_dataset


if __name__ == "__main__":
    # load all data
    dataset = load_dataset("mkieffer/MMLU-Pro-Health")

    # load only train split
    dataset_train = load_dataset("mkieffer/MMLU-Pro-Health", split="train")

    # load only test split
    dataset_test = load_dataset("mkieffer/MMLU-Pro-Health", split="test")

    print("\nfull dataset:\n", dataset)
    print("\ntrain split:\n", dataset_train)
    print("\ntest split:\n", dataset_test)

    print("\ntrain sample:\n", json.dumps(dataset_train[0], indent=2))
    print("\ntest sample:\n", json.dumps(dataset_test[0], indent=2))