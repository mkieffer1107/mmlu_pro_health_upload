**How to run:**

First, create the venv:
```
uv venv --python 3.10 --seed
source .venv/bin/activate
uv sync
```

Login to the HF CLI:
```sh
huggingface-cli login 
```

And enter the configs you like:
```sh
python upload_to_hf.py \
    --hf_username <username> \
    --hf_repo_name MMLU-Pro-Health \
    --private true
```

Voila! The dataset now lives [on HuggingFace](https://huggingface.co/datasets/mkieffer/MMLU-Pro-Health).

All credit belongs to the [original authors](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)

---

**Filtering details**:
The question ID's of filtered rows are included below. In general, rows that are not specifically about health or that are duplicates were removed.

Filtering details related to the health category can be found [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/discussions/31), and general deduping details of the MMLU-Pro dataset can be found [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/discussions/33).


**158 duplicate pairs identified in MMLU-Pro**:
```sh
python find_duplicates.py
```

**111 redundant superset pairs identified in MMLU-Pro**:
```sh
python find_supersets.py
```