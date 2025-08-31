import os

# Force Streamlit to use a writable directory for configs and metrics
os.environ["STREAMLIT_CONFIG_DIR"] = "/tmp/.streamlit"
os.environ["STREAMLIT_CACHE_DIR"] = "/tmp/.streamlit-cache"

os.makedirs(os.environ["STREAMLIT_CONFIG_DIR"], exist_ok=True)
os.makedirs(os.environ["STREAMLIT_CACHE_DIR"], exist_ok=True)


import streamlit as st
from query import run_query

st.set_page_config(page_title="Plantation Buddy 🌱", page_icon="🌱")

st.title("🌱 Plantation Buddy - Ask Me Anything")

st.markdown("This bot helps farmers and nature enthusiasts with queries about plantation and sustainability.")

# Input box
user_query = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Thinking...🤔"):
            response = run_query(user_query)
        st.success(response)
    else:
        st.warning("⚠️ Please enter a valid question.")



