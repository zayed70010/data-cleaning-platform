import pandas as pd

def min_max_scale(df):

    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        min_val = df[col].min()
        max_val = df[col].max()
        if min_val != max_val:
            df[col] = (df[col] - min_val) / (max_val - min_val)
    return df

def z_score_scale(df):

    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        mean_val = df[col].mean()
        std_val = df[col].std()
        if std_val != 0:
            df[col] = (df[col] - mean_val) / std_val
    return df
