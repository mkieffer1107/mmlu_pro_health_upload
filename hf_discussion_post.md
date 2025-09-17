I've found some problems in the health category and categorize them below. In general, there are 94 duplicate pairs, a lot of unrelated questions, and many questions that probably belong in a different category.

---

### unrelated:
View SQL query [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/sql-console/_dqqf1M)

**Summary**
These are questions that just don't relate to health at all, e.g., the McDonaldization of society (6394), smart houses (6091), and visits to grandma (6153).

**Recommendation**
Remove these from the health category.

---

### fact_or_stat_that_could_change:
View SQL query [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/sql-console/Th9ceR1)

**Summary**
These contain facts or statistics that seem like they might change, so they test for memorization of dated facts.

**Recommendation**
Remove them from the dataset. 

---

### tangentially_related:
View SQL query [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/sql-console/ZbIt8dO)

**Summary**
These are questions that are tangentially related to health and might better fit within a different category. It was hard to determine where exactly to draw the line since many of these can be classified as health/biology/chemistry/psychology. I ultimately decided to include a question as tangentially_related if the focus is not on health, and instead something else. For example, if the question is just a stoichiometry problem (6008, chemistry knowledge), asks about a point mutation in a strand of DNA (6074, genetics knowledge), or is just a biochemistry fact (6813, biochemisty knowledge), and makes no attempt at relating back to health, I include it. I'd say that this is the most likely category where I might've made mistakes of omission or inclusion (since there are 800+ rows), so please double check my work. I wouldn't be surpised if you disagree with some of my choices here.

**Recommendation**
Check my work and consider recategorizing.

---

### answer_format_wrong:
View SQL query [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/sql-console/3DYBHjF)

**Summary**
Question ID 6065 has an incorrectly formatted answer choice. Option C gets cut off and the last word is added to option D:

```json
        "options": {
            "A": "Exclusively formula fed for six months",
            "B": "Exclusively breast fed for six months",
            "C": "Should receive both breast milk and other foods as tolerated in the first 6",
            "D": "months",
        }
```

**Recommendation**
Update to

```json
        "options": {
            "A": "Exclusively formula fed for six months",
            "B": "Exclusively breast fed for six months",
            "C": "Should receive both breast milk and other foods as tolerated in the first 6 months"
        }
```

---

### weird_questions:
View SQL query [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/sql-console/l89Yv_x)

**Summary**
These are just weird questions. Either they are extremely long or have strange answer choices that don't make sense or don't seem to relate to the question. There are questions that make references to a specific doctor's recommendations and a segment called Senior View (I'm guessing both come from textbooks).

**Recommendation**
Check them over and consider updating or removing them.

---

### duplicates:
View SQL query [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/sql-console/tXnJYQ6)


**Summary**
I found 94 duplicates in the health category. These duplicates always came in pairs, like 6131 and 6132. I wrote a script to find them all, including in the entire dataset, and have a discussion post [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/discussions/33) with the code to find them.


Note that this only includes exact duplicates. There are other, near duplicates that have the same question and answer, but with expanded answer choices like 6123 and 6124, or 6194 and 6195 (maybe one has answer choices A-C, while another has A-F). It might be a good idea to only include rows that contain the superset of answer choices.

**Recommendation**
Dedup the exact matches, and consider deduping near matches.

---

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
    ]
}
```