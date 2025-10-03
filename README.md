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
    --hf_username mkieffer \
    --hf_repo_name MMLU-Pro-Health \
    --private false
```

Voila! The dataset now lives [on HuggingFace](https://huggingface.co/datasets/mkieffer/MMLU-Pro-Health).

All credit belongs to the [original authors](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)

---

**Filtering details**:

The question ID's of filtered rows are included below. In general, rows that are not specifically about health or that are duplicates were removed.

Filtering details related to the health category can be found [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/discussions/31), and general deduping details of the MMLU-Pro dataset can be found [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/discussions/33).

**158 duplicate pairs identified in MMLU-Pro (94 in the health split)**:
```sh
python find_duplicates.py
```

**111 redundant superset pairs identified in MMLU-Pro**:
```sh
python find_supersets.py
```

The `cot_content` columns in the validation split, which are meant to be used as few-shot examples, were replaced to remove excessive references to Wikipedia that polluted downstream generation. The new `cot_content` columns were generated using the final output of [Baichuan-M2-32B](https://huggingface.co/baichuan-inc/Baichuan-M2-32B). We chose not to use the full reasoning trace, and instead go with the exposed, summarized CoT from the model to ensure that the new `cot_content` has a similar length to others in the dataset.
