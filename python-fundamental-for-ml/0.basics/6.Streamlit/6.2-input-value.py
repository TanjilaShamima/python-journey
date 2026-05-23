import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

name = st.text_input("Enter your name:", placeholder="Enter your name")
if name:
    st.write(f"Hello, {name}!")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1, value=None, placeholder="Enter your age")
if age:
    st.write(f"You are {age} years old.")
favorite_color = st.selectbox("Select your favorite color:", ["Red", "Green", "Blue", "Yellow"])
if favorite_color:
    st.write(f"Your favorite color is {favorite_color}.")
if st.checkbox("Subscribe to newsletter"):
    st.write("Thank you for subscribing!")

