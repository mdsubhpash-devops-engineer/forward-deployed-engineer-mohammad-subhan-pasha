# © 2026 Mohammad Subhan Pasha. All Rights Reserved.
# ™ FieldMitra™ | ™ SubhanOps™ - Forward Deployed Engineer
# Author: Mohammad Subhan Pasha
import streamlit as st

st.set_page_config(page_title="FieldMitra Voice Ops - Mohammad Subhan Pasha")
st.title("FieldMitra Voice Ops™")
st.caption("© 2026 Mohammad Subhan Pasha | Forward Deployed Engineer")

name = st.text_input("Customer Name")
village = st.text_input("Village")
due = st.number_input("Pending Amount", min_value=0, value=0)
visits = st.slider("Visits Done", 0, 10, 2)

if st.button("Check Trust Score"):
    score = 100 - (due // 500) + (visits * 3)
    score = max(10, min(100, score))
    if score >= 80:
        st.success(f"Trust Score: {score} - SAFE - {name} from {village}")
    elif score >= 50:
        st.warning(f"Trust Score: {score} - CAREFUL - {name} from {village}")
    else:
        st.error(f"Trust Score: {score} - HIGH RISK - {name} from {village}")
    st.info("© 2026 Mohammad Subhan Pasha")
