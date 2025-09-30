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

**158 duplicate pairs identified in MMLU-Pro**:
```sh
python find_duplicates.py
```

**111 redundant superset pairs identified in MMLU-Pro**:
```sh
python find_supersets.py
```