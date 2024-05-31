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
        key = (concatenated_key, drug)
        value = "UNSAFE"
        if(effect == "MODERATE" or effect == ""): value = "SAFE"
        salt_drug_dict[key] = value


# def return_effect(salt_interaction, med_name):
#     example_key = (salt_interaction, med_name)

#     if example_key in salt_drug_dict:
#         print(f"\nEffect for Salt Intearction {salt_interaction} and Drug {med_name}: {salt_drug_dict[example_key]}")
#     else:
#         print("No interaction found")


# def get_effect():
#     salt_interaction = input("Enter medicine1: ")
#     med_name = input("Enter medicine2: ")
#     return_effect(salt_interaction, med_name)


print(salt_drug_dict)