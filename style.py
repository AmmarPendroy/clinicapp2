import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f8f9fa;
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)
