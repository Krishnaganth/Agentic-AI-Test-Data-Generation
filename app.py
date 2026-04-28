import streamlit as st
from orchestrator import run_pipeline

st.title("AI Test Data Generator")

req = st.text_area("Enter Requirement")

if st.button("Generate"):
    result = run_pipeline(req)

    st.subheader("Requirement")
    st.code(result["requirement"])

    st.subheader("Constraints")
    st.code(result["constraints"])

    st.subheader("Scenarios")
    st.code(result["scenarios"])

    st.subheader("Test Data")
    st.code(result["data"])
