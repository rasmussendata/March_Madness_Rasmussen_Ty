import streamlit as st
import pandas as pd
import numpy as np


# Page config
st.set_page_config(
    page_title="March Madness",
    page_icon="🏀",
    layout="wide",
)


# Title & Intro
st.title("  March Madness Analysis")
st.markdown(
    "Exploring key statistics in 2024"
    "Use the controls in the sidebar to filter by year"
)


# Load Data

@st.cache_data
def load_data():
    return pd.read_pickle("FINAL_Valid_MMData_v2.pkl")

df = load_data()






year = st.selectbox("Select Season", sorted(df["season"].unique()))

team = st.selectbox("Select Team", ["All"] + sorted(df["team_name"].unique()))


filtered_df = df[df["season"] == year]

if team != "All":
    filtered_df = filtered_df[filtered_df["team_name"] == team]


st.scatter_chart(
    filtered_df,
    x="adjusted_offensive_efficiency",
    y="adjusted_defensive_efficiency"
)


team_selected = st.selectbox("Select Team for Breakdown", filtered_df["team_name"].unique())

team_data = filtered_df[filtered_df["team_name"] == team_selected]

st.write(team_data)





#import matplotlib.pyplot as plt

#fig, ax = plt.subplots()

#ax.scatter(
 #   filtered_df["adjusted_offensive_efficiency"],
  #  filtered_df["adjusted_defensive_efficiency"]
#)

# Label teams
#for i, row in filtered_df.iterrows():
 #   ax.text(row["adjusted_offensive_efficiency"], row["adjusted_defensive_efficiency"], row["team_name"])

#ax.set_xlabel("Adjusted Offensive Efficiency")
#ax.set_ylabel("Adjusted Defensive Efficiency")
#ax.set_title("Team Performance: Offense vs Defense")

#st.pyplot(fig)



