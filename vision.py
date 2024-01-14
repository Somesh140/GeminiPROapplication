import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load gemini-pro model and get responses
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!=" ":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

# Intialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header('Gemini Application')
input = st.text_input("Input Prompt:",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""