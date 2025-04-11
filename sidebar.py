import streamlit as st

def sidebar_navigation():
    st.sidebar.title("📋 Menu")
    return st.sidebar.radio("Go to", ["📊 Client Overview", "➕ Add Client", "📞 Contact Info"])
