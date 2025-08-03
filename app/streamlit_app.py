import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.sidebar.header("Azure RAG Chatbot")
st.sidebar.markdown("Chat with your documents using Azure's free-tier services.")

question = st.text_input("Ask a question:")

if st.button("Submit"):
    res = requests.post("https://ragbot-webapp.azurewebsites.net/chat", json={"query": question})
    st.success(res.json()["answer"])