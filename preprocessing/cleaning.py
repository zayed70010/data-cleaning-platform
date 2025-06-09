import pandas as pd

def remove_duplicates(df):

    return df.drop_duplicates()

def drop_empty_rows(df, threshold=0.5):

    return df.dropna(thresh=int(threshold * df.shape[1]))

def drop_empty_columns(df, threshold=0.5):

    return df.dropna(axis=1, thresh=int(threshold * len(df)))
