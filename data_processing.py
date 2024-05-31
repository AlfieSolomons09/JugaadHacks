import pandas as pd 
import json 
import re
import csv

# loading csv file
file_path = 'medicine_data.csv'
df = pd.read_csv(file_path)

salt_drug_dict = {}

pattern = r'()'

for index, row in df.iterrows():
    salt_composition = row['salt_composition']
    drug_interactions = json.loads(row['drug_interactions'])
    # print(drug_interactions)

    salts = re.findall(pattern, salt_composition)

    concatenated_key = ' '.join([salt.strip() for salt in salts])

    # print(salts)
    # for salt in salts:
        # key = salt.strip()
        
    interactions = []

    drugs = drug_interactions['drug']
    effects = drug_interactions['effect']

    for drug,effect in zip(drugs, effects):
            interactions.append((drug, effect))

    salt_drug_dict[concatenated_key] = interactions

# print(salt_drug_dict["Insulin Isophane/NPH"])
print(salt_drug_dict)
print(salt_drug_dict["Insulin Aspart Insulin Aspart Protamine"])
