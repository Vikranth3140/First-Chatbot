import os
import requests
import streamlit as st

#App Framework
st.title("😃First Chatbot")
prompt = st.text_input("Plug in ur prompt")

# Public API URL
api_url = "https://api.publicapis.org/entries"

# Show things to screen if prompt exists
if prompt:
    # Send a request to the public API
    response = requests.post(api_url, json={"prompt": prompt})

    # Check the status of the response
    if response.status_code == 200:
        # Extract the response text from the API's response
        response_text = response.json()["response"]
        st.write(response_text)
    else:
        st.write("Please give a correct prompt.")