import pandas as pd
import numpy as np


df = pd.read_csv("data.csv")

obj_cols = df.select_dtypes(include=["object"]).columns.tolist()
print("Object columns:", obj_cols)

cols_to_encode = input("Which columns are to be ordinal encoded? (comma-separated): ").split(",")
cols_to_encode = [x.strip() for x in cols_to_encode if x.strip()]

for col in cols_to_encode:
    while col not in df.columns:
        col = input(f"Column '{col}' does not exist. Please enter a valid column name: ").strip()


    df[col] = df[col].str.lower().str.strip()
    unique = df[col].dropna().unique().tolist()

    print(f"Unique values in column '{col}': {unique}")
    while True:
        a = input(f"Do you want to specify the order of encoding for column '{col}' or do u want them to be sorted alphabetically? (O/A): ").strip().lower()
        if a == 'o':
            order = input(f"Enter the desired order for column '{col}' (comma-separated): ").split(",")
            order = [x.strip() for x in order]
            break
        elif a == 'a':
            order = sorted(unique)
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    mapping = {}
    for i, val in enumerate(order):
        mapping[val] = i+1 
    df[col + '_encoded'] = df[col].map(mapping)
    df = df.drop(columns=[col], inplace=False)


df.to_csv("ordinal_encoded_data.csv", index=False)
print(df.head())