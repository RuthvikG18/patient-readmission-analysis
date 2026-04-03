import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # Replace '?' with NaN (this dataset uses ? for missing values)
    df.replace('?', np.nan, inplace=True)

    # Drop columns that have too many missing values
    cols_to_drop = ['weight', 'payer_code', 'medical_specialty']
    df.drop(columns=cols_to_drop, inplace=True)

    # Keep only first hospital visit per patient
    df.drop_duplicates(subset='patient_nbr', keep='first', inplace=True)

    # Create simple target column: 1 = readmitted within 30 days, 0 = not
    df['readmitted_binary'] = df['readmitted'].apply(
        lambda x: 1 if x == '<30' else 0
    )

    return df