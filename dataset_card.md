---
dataset_info:
  features:
  - name: question_id
    dtype: int64
  - name: question
    dtype: string
  - name: options
    struct:
    - name: A
      dtype: string
    - name: B
      dtype: string
    - name: C
      dtype: string
    - name: D
      dtype: string
    - name: E
      dtype: string
    - name: F
      dtype: string
    - name: G
      dtype: string
    - name: H
      dtype: string
    - name: I
      dtype: string
    - name: J
      dtype: string
  - name: answer
    dtype: string
  - name: cot_content
    dtype: string
  - name: src
    dtype: string
  splits:
  - name: train
    num_bytes: 425279.87120291614
    num_examples: 658
  - name: test
    num_bytes: 106643.12879708385
    num_examples: 165
  download_size: 342680
  dataset_size: 531923.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---
