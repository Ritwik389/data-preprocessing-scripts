
import pandas as pd
import numpy as np


df = pd.read_csv("data.csv")

obj_cols = df.select_dtypes(include=["object"]).columns.tolist()
print("Object columns:", obj_cols)

cols_to_encode = input("Which columns are to be ordinal encoded? (comma-separated): ").split(",")
cols_to_encode = [x.strip() for x in cols_to_encode]

for col in cols_to_encode:

    col = col.strip()
    while col not in df.columns:
        col = input(f"Column '{col}' does not exist. Please enter a valid column name: ").strip()
    unique = df[col].dropna().unique().tolist()
    print(f"Unique values in column '{col}': {unique}")
    order = input(f"Enter the desired order for column '{col}' (comma-separated): ").split(",")
    order = [x.strip() for x in order]
    mapping = {}
    for i, val in enumerate(order):
        mapping[val] = i+1 # Start encoding from 1
    df[col + '_encoded'] = df[col].map(mapping)

print(df.head())