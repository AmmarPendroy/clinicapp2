import streamlit as st
import pandas as pd
from datetime import datetime, date

# Set up page
st.set_page_config(page_title="Clinic Dashboard", layout="wide")

# Title
st.title("🏥 Clinic Client Dashboard")

# Load or initialize data
@st.cache_data
def load_data():
    try:
        return pd.read_csv("database.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Client ID", "Name", "Age", "Gender", "Last Visit", "Diagnosis"])

def save_data(df):
    df.to_csv("database.csv", index=False)

df = load_data()

# Sidebar navigation
menu = st.sidebar.selectbox("Choose a page", ["View Clients", "Add New Client", "Contact Info"])

# View Clients Page
if menu == "View Clients":
    st.subheader("📋 All Clients")
    st.dataframe(df, use_container_width=True)

    st.markdown("### 🔍 Filter Clients")
    name_filter = st.text_input("Search by name")
    if not df.empty:
        age_range = st.slider("Select age range", 0, 100, (0, 100))
        gender_filter = st.multiselect("Gender", options=df["Gender"].unique(), default=list(df["Gender"].unique()))

        filtered_df = df[
            df["Name"].str.contains(name_filter, case=False, na=False) &
            df["Age"].between(age_range[0], age_range[1]) &
            df["Gender"].isin(gender_filter)
        ]

        st.dataframe(filtered_df, use_container_width=True)

# Add New Client Page
elif menu == "Add New Client":
    st.subheader("➕ Add New Client")
    with st.form("add_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        last_visit = st.date_input("Last Visit", value=date.today())
        diagnosis = st.text_area("Diagnosis")

        submitted = st.form_submit_button("Add Client")
        if submitted:
            new_id = df["Client ID"].max() + 1 if not df.empty else 1
            new_entry = pd.DataFrame([{
                "Client ID": new_id,
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Last Visit": last_visit.strftime("%Y-%m-%d"),
                "Diagnosis": diagnosis
            }])
            df = pd.concat([df, new_entry], ignore_index=True)
            save_data(df)
            st.success("Client added successfully!")

# Contact Info Page
elif menu == "Contact Info":
    st.subheader("📞 Contact Information")
    st.markdown("""
    **Clinic Name:** Healthy Life Clinic  
    **Phone:** +123 456 789  
    **Email:** hello@healthylife.com  
    **Address:** 123 Wellness Street, Care City  
    """)

