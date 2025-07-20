import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Books to Scrape Data Visualization")

try:
    df = pd.read_csv("books.csv")
except FileNotFoundError:
    st.error("books.csv not found. Please run the Scrapy spider first.")
    st.stop()

st.subheader("Raw Data")
st.dataframe(df)

st.subheader("Price Distribution")
fig_price = px.histogram(df, x="price", nbins=10, title="Book Price Distribution (£)")
st.plotly_chart(fig_price)

st.subheader("Books by Rating")
rating_counts = df["rating"].value_counts().reset_index()
rating_counts.columns = ["Rating", "Count"]
fig_rating = px.bar(rating_counts, x="Rating", y="Count", title="Number of Books by Rating")
st.plotly_chart(fig_rating)

st.subheader("Summary Statistics")
st.write(f"Average Price: £{df['price'].mean():.2f}")
st.write(f"Total Books: {len(df)}")