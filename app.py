import os
import requests
import streamlit as st

api_key = "1c4aaa597dd29ba9c44da6839c89fbf6"

#App Framework
st.title("😃First Chatbot")
prompt = st.text_input("Plug in ur prompt")

# Public API URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + prompt

print(complete_url)
# Show things to screen if prompt exists
if prompt:
    # Send a request to the public API

    response = requests.post(complete_url, json={"prompt": prompt})

    # Check the status of the response
    if response.status_code == 200:
        # Extract the response text from the API's response
        response_text = requests.get(complete_url).json()
        print(type(response_text))

    for i in response_text.keys():
        if i == "coord":
            st.write(response_text.get(i))
        else:
            continue
    else:
        st.write("Please give a correct prompt.")


# import os
# from apikey import apikey
# import streamlit as st
# from langchain.llms import OpenAI
# os.environ["OPENAI_API_KEY"] = apikey

# #App Framework
# st.title("😃First Chatbot")
# prompt = st.text_input("Plug in ur prompt")

# # pip install streamlit langhchain openai wikipedia chromadb tiktoken
# # pip install pydantic==1.8 - for lanchain

# # LLMs
# llm = OpenAI(temperature = 0.9)

# # Show things to screen if prompt exists
# if prompt:
#     response = llm(prompt)
#     st.write(response)