import streamlit as st
import requests

# Set up the chatbot page
def chatbot_interface():
    st.title("MediTrain AI Bot")
    st.write("Ask any question, and I’ll respond!")

    # Initialize session state to manage conversation history
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # Display the chat history
    for message in st.session_state["conversation"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input box for user queries
    user_input = st.chat_input("Your Query")
    if user_input:
        # Display user message in chat
        with st.chat_message("user"):
            st.markdown(user_input)

        # Append user input to conversation
        st.session_state["conversation"].append({"role": "user", "content": user_input})

        # API call to the Flask backend
        payload = {"query": user_input}
        try:
            response = requests.post("https://meditrain-ai-9.onrender.com/response", json=payload)

            if response.status_code == 200:
                bot_reply = response.json().get("response", "No response found.")
                
                # Display chatbot response in chat
                with st.chat_message("assistant"):
                    st.markdown(bot_reply)

                # Append bot reply to conversation
                st.session_state["conversation"].append({"role": "assistant", "content": bot_reply})
            else:
                st.error(f"API Error {response.status_code}: Unable to fetch response.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error occurred: {e}")

# Entry point for bot.py
if __name__ == "__main__":
    chatbot_interface()
