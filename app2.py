import streamlit as st
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Function to simulate conversation and meditation AI process
def start_meditrain_ai(user_input):
    # Simulate the conversation flow based on user input
    user_input = user_input.lower()
    
    if 'start' in user_input:
        return "Starting your meditation session. Please relax and follow the guidance."
    elif 'how' in user_input and 'meditation' in user_input:
        return ("Meditation helps in reducing stress, enhancing focus, and calming the mind. "
                "It involves deep breathing, mindfulness, and staying present in the moment.")
    elif 'help' in user_input:
        return "I am Meditrain AI. I can guide you through meditation sessions and answer questions about the process."
    elif 'thank' in user_input:
        return "You're welcome! Feel free to reach out whenever you need assistance."
    elif 'time' in user_input and 'session' in user_input:
        return "A typical meditation session can last anywhere from 5 to 30 minutes depending on your preference."
    else:
        return "I'm here to help you with meditation. How can I assist you today?"

# Streamlit App
def run_streamlit():
    st.title("Meditrain AI - Meditation Assistant")

    # Instruction and description of the app
    st.write("""
    *Welcome to Meditrain AI!*  
    You can talk to me about meditation, start a session, or ask questions. I am here to help you relax and meditate.
    
    Type your message below, and I'll respond accordingly.
    """)

    # Create a text input for the user to type their message
    user_input = st.text_input("Ask me about meditation:")

    # Create a button to submit the user's input
    if st.button('Send'):
        if user_input:
            # Get AI's response based on user input
            response = start_meditrain_ai(user_input)
            st.write(f"*Meditrain AI*: {response}")
        else:
            st.write("Please type something to start the conversation.")

    # Chat History (keep track of previous conversation)
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if user_input:
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Meditrain AI: {start_meditrain_ai(user_input)}")

    # Display chat history
    for message in st.session_state.chat_history:
        st.write(message)

    # Optionally, add more interactive features like session length, type of meditation, etc.
    if st.button("Start Guided Meditation (10 minutes)"):
        st.write("Starting your 10-minute guided meditation session. Follow my instructions to relax.")
        # Additional logic for the meditation session can be added here

# Main function to run both Flask and Streamlit
if __name__ == "__main__":
    import threading

    # Start Flask app in a thread (if you still want Flask for a backend server)
    def run_flask():
        app.run(host="0.0.0.0", port=5000)  # Running Flask on all IPs on port 5000

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Run Streamlit
    run_streamlit()
