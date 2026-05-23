import streamlit as st

st.title("Hello, Streamlit!")

st.header("Welcome to Streamlit")
st.divider()
st.subheader("This is a subheader")
st.text("Streamlit is an open-source app framework for Machine Learning and Data Science teams. It allows you to create beautiful web apps in minutes.")
st.write("This is a simple Streamlit app.")

if st.button("Click me"):
    st.write("Button clicked!")

st.write("You can also add more components like sliders, checkboxes, and more.")
st.slider("Select a value", 0, 100, 50)
st.checkbox("Check me")
st.text_input("Enter some text")
st.write("That's it for this simple app. You can explore more features of Streamlit to create interactive web applications!")
