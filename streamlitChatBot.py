import streamlit as st
import os
from dotenv import find_dotenv, load_dotenv
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())
api__key = st.secrets["GROQ_API_KEY"]

model = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    groq_api_key=api__key,
    max_tokens=1000,
    temperature=0.5
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def streamlit_ui():
    st.title("LLM Chatbot Application")
    st.write("This is a simple chatbot application.")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input at the bottom
    if user_input := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get response from the model
        response = model.invoke(user_input)

        # Format the response (e.g., truncate or clean up)
        formatted_response = str(response)[:500]  # Convert response to string and limit to 500 characters

        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": formatted_response})

        # Display bot response
        with st.chat_message("assistant"):
            st.markdown(formatted_response)

streamlit_ui()