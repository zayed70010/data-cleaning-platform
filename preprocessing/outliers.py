import pandas as pd
import numpy as np

def remove_outliers_iqr(df):

    numeric_cols = df.select_dtypes(include='number').columns
    cleaned_df = df.copy()

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        cleaned_df = cleaned_df[(cleaned_df[col] >= lower_bound) & (cleaned_df[col] <= upper_bound)]

    return cleaned_df

def remove_outliers_zscore(df, threshold=3):

    numeric_cols = df.select_dtypes(include='number').columns
    z_scores = ((df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()).abs()
    mask = (z_scores < threshold).all(axis=1)
    return df[mask]
