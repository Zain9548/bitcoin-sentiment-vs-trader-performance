import streamlit as st
import pandas as pd

st.title("Hyperliquid Trader Behavior vs Market Sentiment Dashboard")

df = pd.read_csv("final_metrics.csv")

st.sidebar.header("Filters")

sentiment_filter = st.sidebar.selectbox("Select Sentiment", ["All","Fear","Greed"])
segment_filter = st.sidebar.selectbox("Select Segment", ["All","High Frequency","Low Frequency"])

if sentiment_filter != "All":
    df = df[df['Sentiment'] == sentiment_filter]

if segment_filter != "All":
    df = df[df['Segment'] == segment_filter]

st.subheader("Filtered Dataset Preview")
st.dataframe(df.head(30))

st.subheader("Average Daily PnL by Sentiment")
st.bar_chart(df.groupby("Sentiment")['DailyPnL'].mean())

st.subheader("Win Rate by Sentiment")
st.bar_chart(df.groupby("Sentiment")['WinRate'].mean())

st.subheader("Trades per Day by Sentiment")
st.bar_chart(df.groupby("Sentiment")['TradesCount'].mean())

st.subheader("Long/Short Ratio by Sentiment")
st.bar_chart(df.groupby("Sentiment")['LongShortRatio'].mean())
