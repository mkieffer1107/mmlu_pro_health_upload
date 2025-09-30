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
  - name: test
    num_bytes: 357105
    num_examples: 553
  - name: validation
    num_bytes: 3114
    num_examples: 4
  download_size: 244445
  dataset_size: 360219
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
  - split: validation
    path: data/validation-*
---


# MMLU-Pro-Health

Filtered and deduped version of the MMLU-Pro health category to remove extraneous rows. If used, please cite the original authors using the citation below.

## Dataset Details

### Dataset Description

The dataset contains two splits:
  - **test**: up to ten-option multiple-choice QA (choices A-J)
  - **validation**: up to ten-option multiple-choice QA (choices A-J)

The train/validation splits from the original dataset were not altered, only filtered down.

### Dataset Sources

- **Dataset:** https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro
- **Paper:** https://arxiv.org/pdf/2406.01574

### Direct Use

```python
import json
from datasets import load_dataset


if __name__ == "__main__":
    # load all data
    dataset = load_dataset("mkieffer/MMLU-Pro-Health")

    # load only train split
    dataset_train = load_dataset("mkieffer/MMLU-Pro-Health", split="test")

    # load only test split
    dataset_test = load_dataset("mkieffer/MMLU-Pro-Health", split="validation")

    print("\nfull dataset:\n", dataset)
    print("\ntrain split:\n", dataset_train)
    print("\ntest split:\n", dataset_test)

    print("\ntrain sample:\n", json.dumps(dataset_train[0], indent=2))
    print("\ntest sample:\n", json.dumps(dataset_test[0], indent=2))
```



## Citation 

```
@article{wang2024mmlu,
  title={Mmlu-pro: A more robust and challenging multi-task language understanding benchmark},
  author={Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and others},
  journal={arXiv preprint arXiv:2406.01574},
  year={2024}
}
```

## Filtered Rows

The question ID's of filtered rows are included below. In general, rows that are not specifically about health or that are duplicates were removed.

Filtering details related to the health category can be found [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/discussions/31), and general deduping details of the MMLU-Pro dataset can be found [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/discussions/33).


```json
{
    "unrelated": [
        6717,
        6079,
        6205,
        6394,
        6645,
        6018,
        6021,
        6077,
        6091,
        6092,
        6093,
        6094,
        6150,
        6153,
        6194,
        6195,
        6205,
        6214,
        6215,
        6287,
        6288,
        6292,
        6320,
        6328,
        6337,
        6340,
        6341,
        6342,
        6384,
        6404,
        6405,
        6407,
        6410,
        6413,
        6414,
        6459,
        6469,
        6470,
        6585,
        6598,
        6623,
        6624,
        6645,
        6647,
        6656,
        6657,
        6732,
        6738,
        6739,
        6770

    ],
    "fact_or_stat_that_could_change": [
        6022,
        6049,
        6145,
        6154,
        6190,
        6196,
        6269,
        6270,
        6282,
        6290,
        6291,
        6293,
        6298,
        6324,
        6325,
        6329,
        6339,
        6406,
        6408,
        6409,
        6411,
        6412,
        6468,
        6474,
        6512,
        6520,
        6530,
        6532,
        6533,
        6571,
        6572,
        6574,
        6582,
        6695,
        6730,
        6820,
        8

    ],
    "tangentially_related": [
        6003,
        6522,
        6139,
        6646,
        6003,
        6006,
        6008,
        6016,
        6023,
        6049,
        6053,
        6054,
        6004,
        6005,
        6056,
        6067,
        6068,
        6072,
        6074,
        6090,
        6134,
        6136,
        6155,
        6156,
        6157,
        6203,
        6204,
        6206,
        6216,
        6217,
        6219,
        6266,
        6331,
        6338,
        6367,
        6417,
        6460,
        6516,
        6523,
        6524,
        6579,
        6597,
        6622,
        6638,
        6639,
        6696,
        6697,
        6705,
        6737,
        6771,
        6775,
        6779,
        6813,
        6815,
        6816,
        6818


    ],
    "answer_format_wrong": [
        6065 
    ],
    "weird_questions": [
        6329,
        6472,
        6640,
        6652,
        6698,
        6714,
        6781,
        6782,
        6783,
        6784,
        6824

    ],
    "duplicates": [
        [6261, 6262],
        [6036, 6037],
        [6041, 6042],
        [6043, 6044],
        [6050, 6051],
        [6061, 6062],
        [6104, 6105],
        [6108, 6109],
        [6113, 6114],
        [6115, 6116],
        [6119, 6120],
        [6121, 6122],
        [6125, 6126],
        [6131, 6132],
        [6176, 6177],
        [6179, 6180],
        [6185, 6186],
        [6188, 6189],
        [6226, 6227],
        [6231, 6232],
        [6233, 6234],
        [6236, 6237],
        [6240, 6241],
        [6243, 6244],
        [6246, 6247],
        [6248, 6249],
        [6250, 6251],
        [6252, 6253],
        [6254, 6255],
        [6264, 6265],
        [6266, 6267],
        [6274, 6275],
        [6311, 6312],
        [6313, 6314],
        [6321, 6322],
        [6357, 6358],
        [6368, 6369],
        [6371, 6372],
        [6373, 6374],
        [6375, 6376],
        [6380, 6381],
        [6385, 6386],
        [6388, 6389],
        [6433, 6434],
        [6435, 6436],
        [6439, 6440],
        [6441, 6442],
        [6444, 6445],
        [6446, 6447],
        [6448, 6449],
        [6450, 6451],
        [6493, 6494],
        [6497, 6498],
        [6501, 6502],
        [6503, 6504],
        [6507, 6508],
        [6510, 6511],
        [6544, 6545],
        [6548, 6549],
        [6550, 6551],
        [6553, 6554],
        [6555, 6556],
        [6557, 6558],
        [6559, 6560],
        [6563, 6564],
        [6565, 6566],
        [6574, 6575],
        [6579, 6580],
        [6612, 6613],
        [6618, 6619],
        [6634, 6635],
        [6666, 6667],
        [6669, 6670],
        [6672, 6673],
        [6674, 6675],
        [6677, 6678],
        [6682, 6683],
        [6685, 6686],
        [6692, 6693],
        [6699, 6700],
        [6701, 6702],
        [6751, 6752],
        [6756, 6757],
        [6760, 6761],
        [6762, 6763],
        [6790, 6791],
        [6793, 6794],
        [6796, 6797],
        [6798, 6799],
        [6803, 6804],
        [6805, 6806],
        [6808, 6809],
        [6813, 6814],
        [6822, 6823]
    ],
  "supersets": {
    "6039": [
      6038
    ],
    "6054": [
      6053
    ],
    "6124": [
      6123
    ],
    "6182": [
      6181
    ],
    "6194": [
      6195
    ],
    "6257": [
      6256
    ],
    "6260": [
      6259
    ],
    "6310": [
      6309
    ],
    "6325": [
      6324
    ],
    "6361": [
      6360
    ],
    "6362": [
      6363
    ],
    "6378": [
      6377
    ],
    "6491": [
      6492
    ],
    "6496": [
      6495
    ],
    "6506": [
      6505
    ],
    "6542": [
      6543
    ],
    "6546": [
      6547
    ],
    "6562": [
      6561
    ],
    "6568": [
      6567
    ],
    "6569": [
      6570
    ],
    "6572": [
      6571
    ],
    "6577": [
      6576
    ],
    "6614": [
      6615
    ],
    "6616": [
      6617
    ],
    "6623": [
      6624
    ],
    "6626": [
      6627
    ],
    "6679": [
      6680
    ],
    "6689": [
      6688
    ],
    "6691": [
      6690
    ],
    "6697": [
      6696
    ],
    "6704": [
      6703
    ],
    "6755": [
      6754
    ],
    "6765": [
      6764
    ],
    "6801": [
      6800
    ],
    "6812": [
      6811
    ],
    "6815": [
      6816
    ]
  }
}
```