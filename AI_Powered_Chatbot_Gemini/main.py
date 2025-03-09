import os  # Import the os module to interact with environment variables
import time  # Import time module for creating a typing effect
import streamlit as st  # Import Streamlit for building the web app
from dotenv import load_dotenv  # Import dotenv to load environment variables from a .env file
import google.generativeai as gen_ai  # Import Google's Generative AI SDK for using Gemini models
import streamlit.components.v1 as com # Import Streamlit's components module

# Load environment variables from .env file (API key, configurations, etc.)
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title=" Chat with Gemini Flash!",  # Sets the webpage title
    page_icon="🤖",  # Emoji used as the page icon (favicon)
    layout="centered",  # Uses a wider layout for better chat display
)

# Retrieve the Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if the API key is missing; raise an error if it's not set
if not GOOGLE_API_KEY:
    st.error("❌ Google API Key is missing! Check your .env file.")
    st.stop()

# Configure the Generative AI client with the retrieved API key
gen_ai.configure(api_key=GOOGLE_API_KEY)

# Select the AI model to use (Gemini 1.5 Flash latest version, optimized for speed)
model = gen_ai.GenerativeModel('gemini-1.5-flash-latest')

# # Uncomment below code to check the list of available models in cmd
# models = gen_ai.list_models()  # Fetch available AI models
# for single_model in models:
#     print(single_model.name)  # Print each model name in the console

# Function to translate AI-generated role names to Streamlit-friendly roles
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"  # Streamlit uses "assistant" instead of "model"
    else:
        return user_role  # Keep other roles unchanged (e.g., "user")

# Sidebar with chatbot details and a button to clear chat
with st.sidebar:
    # Display the chatbot's avatar in the sidebar
    com.iframe("https://lottie.host/embed/d601225e-a7e6-4024-bd11-b14ab33f80c0/7Cp4UDeCos.lottie")
    st.title("🔧 Chatbot Settings")
    st.write("💡 Powered by Google Gemini AI")
    st.write("⚡ Model: `gemini-1.5-flash-latest`")

    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_session = None
        st.rerun()  # Updated to use st.rerun() instead of deprecated experimental_rerun()

# Initialize chat session in Streamlit if it's not already created
if "chat_session" not in st.session_state or st.session_state.chat_session is None:
    st.session_state.chat_session = model.start_chat(history=[])  # Start a chat session with an empty history

# Display the chatbot's avatar on the Streamlit app
com.iframe("https://lottie.host/embed/fa78f214-1d06-4ab8-b4b2-bf8950b53ce1/WA4qG3Gj9c.lottie")
# Display the chatbot's title on the Streamlit app
st.markdown("""
    <h1 style='text-align: center;'> Gemini Flash - ChatBot</h1>
    <p style='text-align: center; color: gray;'>Ask me anything and I'll respond instantly!</p>
""", unsafe_allow_html=True)

# Loop through and display previous chat messages from the session history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):  # Display messages with proper roles
        st.markdown(message.parts[0].text)  # Render the text of each message in markdown format

# Input field for user's message
user_prompt = st.chat_input("💬 Type your query here...")  # Chat input field for user queries
if user_prompt:
    # Display the user's message in the chat
    st.chat_message("user").markdown(user_prompt)

    # Simulated typing effect for AI response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        
        for char in gemini_response.text:
            full_response += char
            response_placeholder.markdown(full_response + "▌")  # Cursor effect
            time.sleep(0.01)  # Typing effect speed
        
        response_placeholder.markdown(full_response)  # Final response rendering
