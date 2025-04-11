import streamlit as st
import pandas as pd
from datetime import date

def add_client(df, save_function):
    st.title("➕ Add New Client")

    with st.form("add_client_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        last_visit = st.date_input("Last Visit Date", value=date.today())
        diagnosis = st.text_area("Diagnosis")

        submitted = st.form_submit_button("Add Client")

        if submitted:
            new_client = {
                "Client ID": df["Client ID"].max() + 1 if not df.empty else 1,
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Last Visit": last_visit.strftime("%Y-%m-%d"),
                "Diagnosis": diagnosis
            }
            df = pd.concat([df, pd.DataFrame([new_client])], ignore_index=True)
            save_function(df)
            st.success("Client added successfully!")

    return df

def save_data_to_github(df, filename):
    # This function is just a placeholder.
    # In actual use, you’d push the CSV to a GitHub repo using PyGitHub or GitHub API.
    df.to_csv(filename, index=False)
