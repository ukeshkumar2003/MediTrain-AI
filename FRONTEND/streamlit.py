import streamlit as st
import requests

# Backend API URL
API_URL =  os.environ.get("BACKEND_URL")

# Streamlit app configuration
st.set_page_config(page_title="AI Chat Assistant", layout="centered")

# App Header
st.title("AI Chat Assistant")
st.write("Interact with your intelligent assistant below:")

# Chat history container
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["sender"] == "user":
        st.markdown(f"*You:* {message['message']}")
    else:
        st.markdown(f"*Assistant:* {message['message']}")

# Input for user message
user_input = st.text_input("Type your message:", key="user_input")

# Submit button
if st.button("Send"):
    if user_input:
        # Add user message to session state
        st.session_state.messages.append({"sender": "user", "message": user_input})

        try:
            # Send the user message to the backend
            response = requests.post(API_URL, json={"query": user_input})
            response_data = response.json()

            # Get the assistant response
            if "response" in response_data:
                assistant_message = response_data["response"]
            else:
                assistant_message = "No response from the assistant."

            # Add assistant message to session state
            st.session_state.messages.append({"sender": "assistant", "message": assistant_message})

        except Exception as e:
            st.session_state.messages.append({"sender": "assistant", "message": f"Error: {e}"})
        
        # Clear the input box after sending the message
        st.experimental_rerun()
