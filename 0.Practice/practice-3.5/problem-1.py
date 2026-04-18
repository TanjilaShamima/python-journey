# Create a calculator using Streamlit:
# Two number inputs
# A selectbox for operations (+, -, *, /)
# Display the result when a button is clicked

import streamlit as st

input1 = st.number_input("Enter the first number:", value=None, placeholder="Enter first number")
input2 = st.number_input("Enter the second number:", value=None, placeholder="Enter second number")

operation = st.selectbox("Select an operation:", options=["+", "-", "*", "/"])

result = None

if input1 is not None and input2 is not None:
    if operation == "+":
        result = input1 + input2
    elif operation == "-":
        result = input1 - input2
    elif operation == "*":
        result = input1 * input2
    elif operation == "/":
        if input2 != 0:
            result = input1 / input2
        else:
            result = "Error: Division by zero is not allowed."
pressed = st.button("Calculate")

if pressed:
    st.write(f"Result: {result}")