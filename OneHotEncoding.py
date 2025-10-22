
import pandas as pd
import numpy as np


df = pd.read_csv("data.csv")
print(df.head())
obj_cols = df.select_dtypes(include=["object"]).columns.tolist()
print("Object columns:", obj_cols)

cols_to_encode = input("Which columns are to be one hot encoded?(comma-separated): ").split(",")

cols_to_encode = [x.strip() for x in cols_to_encode]

for col in cols_to_encode:
    col = col.strip()
    while col not in df.columns:
        col = input(f"Column '{col}' does not exist. Please enter a valid column name: ").strip()
    df[col] = df[col].astype(str).str.lower().str.strip()
    unique = df[col].dropna().unique().tolist()

    print(f"Unique values in column '{col}': {unique}")
    for val in unique:
        new_col = f'{col}_{val}'
        df[new_col] = (df[col] == val).astype(int)

    if f'{col}_nan' in df.columns:
        df = df.drop(columns=[f'{col}_nan'], inplace=False)
    df = df.drop(columns=[col], inplace=False)

df.to_csv("onehot_encoded_data.csv", index=False)
