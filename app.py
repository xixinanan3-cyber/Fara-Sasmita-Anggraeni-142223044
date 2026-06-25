import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Viewer", layout="wide")

st.title("📊 Streamlit Data App")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data.csv")

st.subheader("Preview Data")
st.dataframe(df)

st.subheader("Basic Info")
st.write(df.describe())

st.subheader("Columns")
column = st.selectbox("Select column to visualize", df.columns)

if df[column].dtype in ['int64', 'float64']:
    st.bar_chart(df[column])
else:
    st.write(df[column].value_counts())
