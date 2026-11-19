# © 2026 Mohammad Subhan Pasha. All Rights Reserved.
# ™ Ops Copilot™ - Author: Mohammad Subhan Pasha
import streamlit as st
st.set_page_config(page_title="Ops Copilot - Mohammad Subhan Pasha")
st.title("Ops Copilot™")
st.caption("© 2026 Mohammad Subhan Pasha | Forward Deployed Engineer")
q = st.text_input("Ask Officer Question - Ex: Who has highest pending?")
if st.button("Ask Copilot"):
    if "highest" in q.lower() or "pending" in q.lower():
        st.success("Venkat - Renigunta - Rs 8000 pending - HIGH RISK. Visit first.")
    elif "safe" in q.lower():
        st.success("Kavitha - Chittoor - Score 92 - SAFE. Can give new loan.")
    else:
        st.info("Copilot: Based on field data, check pending list first, then visit high-risk customers in morning.")
