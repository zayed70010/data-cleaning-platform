import streamlit as st
import pandas as pd

from preprocessing.reader import read_data
from preprocessing.cleaning import remove_duplicates, drop_empty_rows, drop_empty_columns
from preprocessing.missing import fill_missing_with_mean, fill_missing_with_median, fill_missing_with_mode
from preprocessing.encode import encode_categorical_columns
from preprocessing.outliers import remove_outliers_iqr, remove_outliers_zscore
from preprocessing.normalize import min_max_scale, z_score_scale

st.set_page_config(page_title=" Intelligent Data Preprocessing Platform ", layout="wide")
st.title("  Intelligent Data Preprocessing Platform ")

uploaded_file = st.file_uploader("Upload CSV or JSON file", type=["csv", "json"])

if uploaded_file is not None:
    try:
        df = read_data(uploaded_file)
        st.success("File successfully loaded")
    except Exception as e:
        st.error(f" Failed to load the file  : {e}")
        st.stop()

    st.subheader(" Original Data ")
    st.dataframe(df.head())

    exclude_cols = st.multiselect(" Select columns to exclude from preprocessing ", df.columns.tolist())

    fill_method = st.selectbox(" Missing values handling method ", ["mean", "median", "mode"])
    outlier_method = st.selectbox(" Outlier removal method ", [None, "iqr", "zscore"])
    normalize_method = st.selectbox(" Normalization method ", [None, "minmax", "zscore"])

    if st.button("▶️ Start Preprocessing "):
        try:
        
            df = remove_duplicates(df)
            df = drop_empty_rows(df)
            df = drop_empty_columns(df)

            cols_to_process = df.drop(columns=exclude_cols, errors="ignore")

    
            if fill_method == "mean":
                cols_to_process = fill_missing_with_mean(cols_to_process)
            elif fill_method == "median":
                cols_to_process = fill_missing_with_median(cols_to_process)
            elif fill_method == "mode":
                cols_to_process = fill_missing_with_mode(cols_to_process)


            cols_to_process = encode_categorical_columns(cols_to_process)

            if outlier_method == "iqr":
                cols_to_process = remove_outliers_iqr(cols_to_process)
            elif outlier_method == "zscore":
                cols_to_process = remove_outliers_zscore(cols_to_process)

            if normalize_method == "minmax":
                cols_to_process = min_max_scale(cols_to_process)
            elif normalize_method == "zscore":
                cols_to_process = z_score_scale(cols_to_process)

            final_df = pd.concat([cols_to_process, df[exclude_cols].loc[cols_to_process.index]], axis=1)

            st.success(" Preprocessing completed successfully")
            st.subheader("  Processed Data ")
            st.dataframe(final_df.head())

            csv = final_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=" Download Processed Data",
                data=csv,
                file_name="processed_data.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f" Error during preprocessing : {e}")

            
#venv\Scripts\activate 
#streamlit run frontend.py