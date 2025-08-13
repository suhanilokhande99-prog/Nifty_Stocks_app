import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Nifty_Stocks.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Streamlit UI
st.title("📈 Nifty Stocks Visualizer")
st.markdown("Select a sector and stock to view its historical closing prices.")

# Dropdown for sectors
sectors = df['Category'].unique()
selected_sector = st.selectbox("Select Sector", sorted(sectors))

# Filter stocks by selected sector
filtered_df = df[df['Category'] == selected_sector]
symbols = filtered_df['Symbol'].unique()

# Dropdown for stock symbols
selected_stock = st.selectbox("Select Stock", sorted(symbols))

# Filter data for selected stock
stock_df = filtered_df[filtered_df['Symbol'] == selected_stock]

# Plotting
st.subheader(f"{selected_stock} - Closing Price Over Time")

fig, ax = plt.subplots(figsize=(12, 6))
sb.lineplot(data=stock_df, x='Date', y='Close', ax=ax)
ax.set_title(f"{selected_stock} Closing Price Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
plt.xticks(rotation=45)
st.pyplot(fig)
