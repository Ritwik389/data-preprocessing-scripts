import pandas as pd
import numpy as np

def load_data():
    data = {
        'City': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Delhi', np.nan, 'Mumbai', 'Kolkata'],
        'Education': ['High School', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', np.nan, 'High School'],
        'Experience': [1, 3, 5, np.nan, 7, 2, 10, np.nan],
        'Salary': [25000, 40000, 60000, 80000, np.nan, 30000, 75000, 50000]
    }

    df = pd.DataFrame(data)
    return df


df = load_data()
df.to_csv('data.csv', index=False)

