from sklearn.preprocessing import LabelEncoder

def encode_categorical_columns(df):

    label_encoders = {}
    for col in df.select_dtypes(include=["object", "category"]).columns:
        try:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
        except Exception as e:
            print(f" لم يتم ترميز العمود: {col} – {e}")
    return df
