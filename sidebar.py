import streamlit as st

def sidebar_navigation():
    st.sidebar.title("📋 Menu")
    return st.sidebar.radio("Navigate to", [
        "📊 Client Overview", 
        "➕ Add Client", 
        "📞 Contact Info"
    ])
