import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the page title
st.title("Stock Price Visualizer")

# Load the dataset
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Ensure Date column is datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Show available categories (sectors)
    categories = df['Category'].unique()
    selected_category = st.selectbox("Select Sector (Category)", categories)

    # Filter by selected category
    filtered_by_category = df[df['Category'] == selected_category]

    # Show available symbols in this category
    symbols = filtered_by_category['symbol'].unique()
    selected_symbol = st.selectbox("Select Stock (Symbol)", symbols)

    # Filter by selected stock
    stock_data = filtered_by_category[filtered_by_category['symbol'] == selected_symbol]

    # Plot
    st.subheader(f"{selected_symbol} Stock Price Over Time")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=stock_data['Date'], y=stock_data['Close'], ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    plt.xticks(rotation=90)
    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to get started.")
