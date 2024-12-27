import streamlit as st

def content_page():
    # Page Title
    st.title("MediTrain AI - About the Application")
    st.write("Welcome to MediTrain AI! This section provides a detailed overview of the application and its components.")

    # Section: Project Overview
    st.header("Project Overview")
    st.write(
        """
        MediTrain AI is an innovative chatbot designed to simulate patient interactions. 
        It serves as a virtual training assistant for medical professionals and students, allowing them to:
        - Practice diagnosing symptoms.
        - Respond to various patient queries.
        - Improve communication skills in real-world medical scenarios.
        By leveraging advanced technologies like LangChain and Groq, MediTrain AI creates realistic simulations to enhance learning experiences.
        """
    )

    # Section: Features
    st.header("Key Features")
    st.write(
        """
        - **Conversational AI:** A friendly, interactive chatbot to assist users with queries.
        - **Contextual Memory:** Tracks previous interactions for coherent and relevant responses.
        - **Medical Training Simulation:** Simulates different patient personas and query complexities.
        - **Seamless Frontend-Backend Integration:** Built using Flask for the backend and Streamlit for the frontend.
        """
    )

    # Section: Technologies Used
    st.header("Technologies Used")
    st.write(
        """
        MediTrain AI integrates cutting-edge tools and frameworks:
        - **Streamlit:** A Python library to create beautiful, interactive web applications with ease.
        - **Flask:** A lightweight WSGI web application framework for building robust APIs.
        - **LangChain:** A framework to build LLM-powered applications with memory, chaining, and prompt management.
        - **Groq:** A high-performance model that enhances conversational AI capabilities with scalable and efficient infrastructure.
        """
    )

    # Section: Development Journey
    st.header("Development Journey")
    st.write(
        """
        The development of MediTrain AI involved the following steps:
        1. **Defining Requirements:** Identified the need for a chatbot focused on medical training.
        2. **Backend Setup:** Created a Flask-based API to handle AI responses using LangChain and Groq.
        3. **Frontend Development:** Designed a Streamlit-based interface for an engaging user experience.
        4. **Integration:** Linked the Streamlit frontend with the Flask backend for seamless interaction.
        5. **Hosting:** Hosted the backend on Railway and explored options for hosting the frontend on Streamlit Cloud or Vercel.
        """
    )

    # Section: Health Tips
    st.header("Health Tips")
    st.write(
        """
        Maintaining a healthy lifestyle is crucial. Here are some practical tips:
        - **Regular Checkups:** Early detection can prevent complications.
        - **Balanced Diet:** Include nutritious foods like fruits, vegetables, and proteins.
        - **Exercise:** Stay active with at least 30 minutes of exercise daily.
        - **Hydration:** Drink plenty of water to keep your body hydrated.
        - **Stress Management:** Practice mindfulness or yoga to reduce stress.
        """
    )

    # Section: Safety Tips
    st.header("Safety Tips")
    st.write(
        """
        - **Wash Hands Regularly:** Prevent the spread of germs.
        - **Wear Masks:** Especially in crowded places.
        - **Stay Updated:** Follow vaccination and public health guidelines.
        """
    )

    # Footer
    st.write("---")
    st.write(
        """
        MediTrain AI is your trusted companion for health and learning. Explore its features, stay informed with the health tips, 
        and improve your medical knowledge through interactive training simulations.
        """
    )

# Entry point for the content.py module
if __name__ == "__main__":
    content_page()
