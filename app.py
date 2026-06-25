import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("⚽ FIFA World Cup 2026 Player Performance Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("fifa_world_cup_2026_player_performance.csv")

df = load_data()

st.subheader("📊 Dataset")
st.dataframe(df)

st.sidebar.header("🔍 Filter Data")
team = st.sidebar.selectbox("Pilih Tim", df["team"].unique())
position = st.sidebar.selectbox("Pilih Posisi", df["position"].unique())

filtered_df = df[(df["team"] == team) & (df["position"] == position)]

st.subheader("📌 Data Terfilter")
st.write(filtered_df)

st.subheader("📈 Statistik Pemain")

col1, col2, col3 = st.columns(3)
col1.metric("Total Gol", int(filtered_df["goals"].sum()))
col2.metric("Total Assist", int(filtered_df["assists"].sum()))
col3.metric("Rata Rating", round(filtered_df["player_rating"].mean(), 2))

st.subheader("🏆 Top 10 Player by Rating")
top_players = df.sort_values(by="player_rating", ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(top_players["player_name"], top_players["player_rating"])
ax.invert_yaxis()
st.pyplot(fig)

st.subheader("⚽ Distribusi Gol")
fig2, ax2 = plt.subplots()
ax2.hist(df["goals"], bins=10)
st.pyplot(fig2)

st.write("Dibuat dengan Streamlit 🚀")
