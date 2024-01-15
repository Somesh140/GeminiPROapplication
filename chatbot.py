from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

# Initialize our streamlit app
st.set_page_config('Chatbot')
st.header('Conversational Chat-bot')

#Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:",key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    # Add user query and response to the session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is ")
    for chunk in response:
        if hasattr(chunk, 'text'):  # Check if the chunk has a 'text' attribute
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
        elif hasattr(chunk, 'parts'):  # Use 'parts' accessor if available
            for part in chunk.parts:
                st.write(part.text)
                st.session_state['chat_history'].append(("Bot", part.text))


    for role,text in st.session_state['chat_history']:
        st.write(f"{role} :{text}")
