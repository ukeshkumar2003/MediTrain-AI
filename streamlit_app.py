import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Clear Cache
st.cache_data.clear()

# Set tab title and favicon
st.set_page_config(
    page_title="MediTrain AI",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* General Page Styling */
    body {
        background-color: #121212;
        color: #FFD700;
    }

    .stSidebar {
        background-color: #1e1e1e;
        color: #FFD700;
    }

    .css-1v3fvcr {
        color: #FFD700 !important; /* Sidebar menu text color */
    }

    .css-17z2g3v {
        color: #FF4500 !important; /* Main heading text */
    }

    .stButton button {
        background-color: #FF4500;
        color: yellow;
        border: none;
        border-radius: 5px;
    }

    .stButton button:hover {
        background-color: #FFD700;
        color: white;
    }

    /* Titles and Subtitles */
    .st-emotion-cache-1otqz59 h1, .st-emotion-cache-1cvow4s h1,
    .st-emotion-cache-1otqz59 h2, .st-emotion-cache-1cvow4s h2,
    .st-emotion-cache-1otqz59 h3, .st-emotion-cache-1cvow4s h3 {
        color: #FFD700 !important;
        text-decoration: none !important; /* Prevent strikethrough or any other decoration */
    }

    /* Horizontal Line Styling */
    hr {
        border: 1px solid #FF4500;
    }
</style>
    """,
    unsafe_allow_html=True,
)

# Menu configuration (1=sidebar menu, 2=horizontal menu)
MENU_TYPE = 1

# Function to set up the menu
def streamlit_menu(menu_type=1):
    if menu_type == 1:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home", "Meditrain AI Bot", "Description"],
                icons=["house", "robot", "book"],
                menu_icon="cast",
                default_index=0,
                key="sidebar_menu",
            )
        return selected

# Initialize the menu
selected = streamlit_menu(menu_type=MENU_TYPE)

# Pages
if selected == "Home":
    st.title("Welcome to MediTrain AI!")
    st.subheader("Empowering Healthcare Education Through AI")
    st.markdown("""
        **MediTrain AI** is your AI-powered healthcare assistant designed to enhance medical education and patient communication. 
        Use the navigation menu to explore features like:
        - **Interactive Chatbot**: Simulate real-time patient conversations.
        - **Health Resources**: Access valuable information on health checkups and tips.
        - **Learn and Explore**: Discover insights on healthcare technologies.
    """)

elif selected == "Meditrain AI Bot":
    st.title("MediTrain AI Bot")
    st.markdown("""
        ### How to Use MediTrain AI Bot
        1. **Enter Your Query**: Type a medical-related question or scenario in the input box. For example:
           - "What are the symptoms of diabetes?"
           - "Suggest a treatment plan for hypertension."
        2. **Receive an AI Response**: The bot, trained on medical datasets, provides detailed and informative replies.
        3. **Refine Your Queries**: Ask follow-up questions or clarify scenarios for better accuracy.
        4. **Simulated Patient Interactions**: Use the bot to practice diagnosis or patient communication skills.

        ### Example Use Cases
        - **For Medical Students**:
          - "How should I explain asthma management to a patient?"
        - **For Doctors**:
          - "What are the guidelines for prescribing antibiotics?"
        - **For General Users**:
          - "What are the benefits of regular health checkups?"

        ### Features
        - Real-time responses powered by AI.
        - Tailored to address medical scenarios and datasets.
        - Built for education, training, and better healthcare communication.
    """)
    try:
        bot = importlib.import_module("bot")
        if hasattr(bot, "chatbot_interface"):
            bot.chatbot_interface()
        else:
            st.error("The bot module does not have a 'chatbot_interface' function.")
    except Exception as e:
        st.error(f"Error loading the chatbot interface: {e}")

elif selected == "Description":
    st.title("Description")
    st.markdown("""
        ### About MediTrain AI
        MediTrain AI is designed to empower users with the ability to simulate medical interactions and access health-related information efficiently.

        ### How It Works
        - **Chatbot Feature**: Built using AI models trained on medical datasets, the bot can respond to a wide range of queries, helping users learn and explore healthcare topics.
        - **Interactive Interface**: Intuitive design ensures ease of use for all users, from students to professionals.

        ### Technologies Behind MediTrain AI
        - **Streamlit**: Provides an interactive and user-friendly interface for the application.
        - **Flask**: Powers the backend for handling and processing user queries.
        - **LangChain**: Enhances AI responses by structuring context-based interactions.
        - **Medical Datasets**: Carefully curated datasets ensure accurate and reliable responses.

        ### Why Choose MediTrain AI?
        - Enhance medical training with real-time conversational AI.
        - Gain access to reliable health tips and insights.
        - Improve patient communication skills in a safe and simulated environment.
    """)
    try:
        content = importlib.import_module("content")
        if hasattr(content, "content_page"):
            content.content_page()
        else:
            st.error("The content module does not have a 'content_page' function.")
    except Exception as e:
        st.error(f"Error loading the content module: {e}")
