import streamlit as st
import pandas as pd

# Sample client data (you can replace this with your actual data source)
data = {
    'Client ID': [101, 102, 103, 104],
    'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Lee', 'Diana Patel'],
    'Age': [34, 45, 29, 54],
    'Gender': ['Female', 'Male', 'Male', 'Female'],
    'Last Visit': ['2024-12-01', '2025-01-15', '2025-03-10', '2025-04-01'],
    'Diagnosis': ['Flu', 'Diabetes', 'Check-up', 'Hypertension']
}

df = pd.DataFrame(data)

# Streamlit UI
st.set_page_config(page_title="Clinic Client Dashboard", layout="centered")

st.title("🏥 Clinic Client Dashboard")
st.write("Welcome to the clinic dashboard. View and filter client records easily.")

# Filter by name
search_name = st.text_input("🔍 Search by client name")

if search_name:
    filtered_df = df[df['Name'].str.contains(search_name, case=False)]
else:
    filtered_df = df

# Show table
st.dataframe(filtered_df, use_container_width=True)

# Show basic stats
st.subheader("📊 Client Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Clients", len(df))

with col2:
    st.metric("Average Age", round(df["Age"].mean(), 1))

with col3:
    st.metric("Last Visit Date", df["Last Visit"].max())

st.caption("Simple clinic dashboard - Powered by Streamlit")

