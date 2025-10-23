import pandas as pd
import numpy as np


df = pd.read_csv('data.csv')


print(f'Missing values before imputation:\n {df.isnull().sum()}')
while True:
    strategy = input("Enter imputation strategy (mean, median, most_frequent, constant): ")
    if strategy in ['mean', 'median', 'most_frequent', 'constant']:
        break
    print("Invalid strategy. Please try again.")

for col in df.columns:
    if df[col].dtype != 'object': 
        if strategy == 'mean':
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == 'median':
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == 'most_frequent':
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif strategy == 'constant':
            fill_val = input(f"Enter constant value for column '{col}': ")
            try:
                fill_val = float(fill_val)
            except ValueError:
                pass
            df[col].fillna(fill_val, inplace=True)
    else:  
        if strategy == 'most_frequent':
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif strategy == 'constant':
            fill_val = input(f"Enter constant value for column '{col}': ")
            df[col].fillna(fill_val, inplace=True)
            

print(f'Missing values after imputation:\n {df.isnull().sum()}')

df.to_csv('imputed_data.csv', index=False)


