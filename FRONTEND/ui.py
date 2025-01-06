import streamlit as st
from PIL import Image

# App Configuration
st.set_page_config(
    page_title="Meditrain AI",
    page_icon="🩺",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("Meditrain AI")
    st.write("Your personalized AI-powered medical training platform.")
    menu = st.radio(
        "Navigate",
        ["Home", "Diagnosis Assistance", "Learning Modules", "About"]
    )

# Home Page
if menu == "Home":
    st.title("Welcome to Meditrain AI 🩺")
    st.write("""
    Meditrain AI is designed to assist medical professionals and students 
    with cutting-edge tools for learning, diagnosis, and skill enhancement.
    """)

# Diagnosis Assistance
elif menu == "Diagnosis Assistance":
    st.title("Diagnosis Assistance")
    st.write("Provide symptoms or patient details, and let Meditrain AI assist you.")

    # User input
    symptoms = st.text_area("Enter Symptoms", placeholder="e.g., fever, cough, fatigue")
    patient_age = st.number_input("Patient Age", min_value=0, max_value=120, step=1)
    patient_gender = st.selectbox("Patient Gender", ["Male", "Female", "Other"])

    # Process and display results
    if st.button("Analyze Symptoms"):
        # Placeholder for AI diagnosis function
        st.success("AI Analysis in Progress...")
        st.write("This is a placeholder for diagnosis results.")
        # Replace with your backend AI logic

# Learning Modules
elif menu == "Learning Modules":
    st.title("Learning Modules")
    st.write("Explore interactive learning content on various medical topics.")

    topics = ["Cardiology", "Neurology", "Pediatrics", "Dermatology"]
    selected_topic = st.selectbox("Select Topic", topics)

    if st.button("Start Learning"):
        st.write(f"Loading learning content for *{selected_topic}*...")
        # Replace with learning module content retrieval

# About Page
elif menu == "About":
    st.title("About Meditrain AI")
    st.write("""
    Meditrain AI is a platform designed to empower medical professionals and students 
    by providing AI-assisted tools for diagnosis and medical learning.
    """)

    st.write("### Contact Us")
    st.write("- Email: support@meditrain.ai")
    st.write("- Website: [meditrain-ai-ukesh.streamlit.app](https://meditrain.ai)")

    st.write("### Our Mission")
    st.write("""
    To revolutionize medical education and patient care with the help of artificial intelligence.
    """)

# Footer
st.write("---")
st.write("© 2025 Meditrain AI. All rights reserved.")
