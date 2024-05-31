import pandas as pd 
import json 
import re

file_path = 'medicine_data.csv'
df = pd.read_csv(file_path)

salt_drug_dict = {}

pattern = r'([A-Za-z\s]+)(?=\s*\()'

for index, row in df.iterrows():
    salt_composition = row['salt_composition']
    drug_interactions = json.loads(row['drug_interactions'])

    salts = re.findall(pattern, salt_composition)

    concatenated_key = ' '.join([salt.strip() for salt in salts])

    drugs = drug_interactions['drug']
    effects = drug_interactions['effect']

    for drug, effect in zip(drugs, effects):
        key = (concatenated_key.lower(), drug.lower())
        value = "unsafe"
        if effect.lower() in ["moderate", ""]:
            value = "safe"
        salt_drug_dict[key] = value


print(salt_drug_dict)