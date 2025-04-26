import streamlit as st

# App title
st.title("Simple Diary App")

# Section 1: User details
st.header("Enter your details")

with st.form("user_info"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    submitted = st.form_submit_button("Continue")

# Section 2: Diary entry
if submitted and name and email and phone:
    st.success(f"Welcome, {name}! You're now allowed to write your diary entry.")

    st.header("Your Diary")
    diary_entry = st.text_area("Write your thoughts here...")

    if st.button("Submit Entry"):
        st.success("Diary entry saved successfully!")


elif submitted:
    st.error("Please fill out all fields before continuing.")
