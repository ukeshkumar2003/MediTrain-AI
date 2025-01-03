import os
import streamlit as st
import requests

def main():
    # Streamlit app title and description
    st.title("Chatbot App")
    st.subheader("Ask your question and get instant responses!")

    # Get backend URL from environment variable or use default
    backend_url = os.environ.get("BACKEND_URL", "http://localhost:8000")

    # Initialize conversation history in session state
    if "conversation_history" not in st.session_state:
        st.session_state["conversation_history"] = []

    # Input box for user's query
    user_input = st.text_input("Your Query:", placeholder="Type something...")

    # Button to send the query
    if st.button("Send"):
        if user_input.strip():
            # API request payload
            payload = {"query": user_input}
            try:
                # Send POST request to the backend
                response = requests.post(f"{backend_url}/response", json=payload)

                if response.status_code == 200:
                    # Parse JSON response
                    bot_response = response.json().get("response", "No response received.")
                    # Update conversation history
                    st.session_state["conversation_history"].append(
                        {"user": user_input, "bot": bot_response}
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.reason}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a query before sending.")

    # Display conversation history
    if st.session_state["conversation_history"]:
        st.write("### Conversation History")
        for i, chat in enumerate(st.session_state["conversation_history"], start=1):
            st.write(f"*{i}. You:* {chat['user']}")
            st.write(f"*{i}. Bot:* {chat['bot']}")

if _name_ == "_main_":
    main()
