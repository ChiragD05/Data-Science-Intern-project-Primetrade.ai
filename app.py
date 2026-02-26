import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("📊 Trader Performance vs Market Sentiment")

# Load processed data
@st.cache_data
def load_data():
    return pd.read_csv("daily_metrics.csv")

daily_metrics = load_data()

# Sidebar filter
st.sidebar.header("Filters")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=daily_metrics['classification'].unique(),
    default=daily_metrics['classification'].unique()
)

filtered = daily_metrics[
    daily_metrics['classification'].isin(sentiment_filter)
]

# ===== METRICS =====
col1, col2, col3 = st.columns(3)

col1.metric("Avg Daily PnL",
            round(filtered['daily_pnl'].mean(), 2))

col2.metric("Avg Trade Count",
            round(filtered['trade_count'].mean(), 2))

col3.metric("Win Rate",
            round(filtered['win'].mean(), 2))

st.markdown("---")

# ===== CHART 1 =====
st.subheader("Daily PnL Distribution")

fig1, ax1 = plt.subplots(figsize=(8,5))
sns.boxplot(
    data=filtered,
    x='classification',
    y='daily_pnl',
    ax=ax1
)
ax1.axhline(0, linestyle='--')
plt.xticks(rotation=45)
st.pyplot(fig1)

# ===== CHART 2 =====
st.subheader("Trade Frequency vs Daily PnL")

fig2, ax2 = plt.subplots(figsize=(8,5))
sns.scatterplot(
    data=filtered,
    x='trade_count',
    y='daily_pnl',
    alpha=0.4,
    ax=ax2
)
st.pyplot(fig2)

st.markdown("---")
st.write("Built for Data Science Intern Assignment – Trader Behavior Insights")