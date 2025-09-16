there were still many more that i felt might not necessarily belong in health

many of the unrelated and tangentially related questions should be moved to a different category like economics, chemistry, psychology, biology, history, philosophy, etc.


there were many that are on the borderline of health/biology/chemistry that I didn't include because I just wasn't sure.

it was hard to determine where exactly to draw the line, so if it ultimately related to human health i ignored it, but if it requires skills outside of health, i included it, e.g., stoichiometry-type questions or determining a point mutation in a DNA strand

anyway, there were so many to go through that i just quickly determined problem ids

the duplicates always came in pairs, so it might be a good idea to write a script to find them. just have it first check for sequential samples with the same question, and then put their answer choices into a set to confirm a match (because sometimes the answer choices might be expanded or slightly different).

I've identified a few questions that don't relate to health category they are assigned to. The problem items all come from the source "ori_mmlu-college_medicine"



Not related to health at all:
6717
6079
6205
6394
6645

Tangentially related to health:
6522
6139
6646
6647
6328

You can view all the problem rows using my HF dataset SQL query [here](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/sql-console/Qt_zTeD)



Here are a few of the duplicate mappings. I didn't want to do this for every example 😅

---
Duplicates: 6036, 6037

QID 6036:
0) Acute myocardial infarction
1) Congestive heart failure
2) Angina pectoris
3) Aortic dissection <<<<<<<<<<
4) Mitral valve prolapse
5) Esophageal rupture
6) Hypertensive crisis
7) Thoracic aortic aneurysm
8) Pulmonary embolism
9) Aortic stenosis

QID 6037:
0) Angina pectoris
1) Pulmonary embolism
2) Aortic dissection <<<<<<<<<<<<
3) Esophageal rupture
4) Hypertensive crisis
5) Thoracic aortic aneurysm
6) Aortic stenosis
7) Congestive heart failure
8) Mitral valve prolapse
9) Acute myocardial infarction

Here's the mapping from QID 6036 → 6037:
• 0 → 9
• 1 → 7
• 2 → 0
• 3 → 2 (correct answer)
• 4 → 8
• 5 → 3
• 6 → 4
• 7 → 5
• 8 → 1
• 9 → 6

---
Duplicates: 6050, 6051

QID 6050:
0) Oxidation of glucose to carbon dioxide and water
1) Conversion of pyruvate to lactate
2) Synthesis of methionine from homocysteine
3) Synthesis of purine nucleotides
4) Decarboxylation of amino acids to form amine neurotransmitters
5) Synthesis of fatty acids from acetyl-CoA
6) Conversion of phenylalanine to tyrosine
7) Conversion of glucose to glycogen
8) Carboxylation of pyruvate to oxaloacetate.  <<<<<<<<<<<<<<<<<<<<<<<<<<
9) Synthesis of methylene tetrahydrofolate

QID 6051:
0) Synthesis of methylene tetrahydrofolate
1) Conversion of glucose to glycogen
2) Synthesis of purine nucleotides
3) Synthesis of methionine from homocysteine
4) Oxidation of glucose to carbon dioxide and water
5) Carboxylation of pyruvate to oxaloacetate <<<<<<<<<<<<<<<<<<<<
6) Synthesis of fatty acids from acetyl-CoA
7) Conversion of pyruvate to lactate
8) Conversion of phenylalanine to tyrosine
9) Decarboxylation of amino acids to form amine neurotransmitters

Here's the mapping from QID 6050 → 6051:
• 0 → 4
• 1 → 7
• 2 → 3
• 3 → 2
• 4 → 9
• 5 → 6
• 6 → 8
• 7 → 1
• 8 → 5 (correct answer)
• 9 → 0

---

Duplicates: 6061, 6062

QID 6061:
0) Saturated fat
1) High fiber diet
2) Eating citrus fruits
3) Alcohol
4) Lack of physical activity
5) Low protein intake
6) Vitamin D deficiency
7) Obesity
8) High dose ß-carotene supplements <<<<<<<<<<<
9) Drinking green tea

QID 6062:
0) Lack of physical activity
1) High fiber diet
2) Alcohol
3) Low protein intake
4) High dose ß-carotene supplements <<<<<<<<<<<
5) Saturated fat
6) Vitamin D deficiency
7) Obesity
8) Eating citrus fruits
9) Drinking green tea

Here's the mapping from QID 6061 → 6062:
• 0 → 5
• 1 → 1
• 2 → 8
• 3 → 2
• 4 → 0
• 5 → 3
• 6 → 6
• 7 → 7
• 8 → 4 (correct answer)
• 9 → 9