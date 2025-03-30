import streamlit as st
import random
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Chand Raat & Eid Mubarak",
    page_icon="🌙",
    layout="centered"
)

# Sample Chand Raat quotes/wishes
quotes = [
    "Chand Raat Mubarak! May this moonlit night bring peace and happiness to your life.",
    "Wishing you a blessed Chand Raat filled with love, joy, and sweet moments!",
    "May the sighting of the moon bring new hopes and dreams. Chand Raat Mubarak!",
    "Chand Raat Mubarak! Let's celebrate the beauty of this night with loved ones.",
    "May Allah shower His blessings upon you this Chand Raat and always!"
]

# Eid date (for countdown) - Assuming Eid is on March 31, 2025
eid_date = datetime(2025, 3, 31, 0, 0, 0)

# Custom CSS for the new design
def add_custom_css():
    st.markdown(
        """
        <style>
        /* Import fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Dancing+Script:wght@700&display=swap');

        /* General styling */
        .stApp {
            background: #1A2A44; /* Midnight Blue */
            min-height: 100vh;
            position: relative;
            overflow: hidden;
        }
        .stApp::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('https://www.transparenttextures.com/patterns/stardust.png');
            opacity: 0.2;
            z-index: 0;
        }
        .stApp > * {
            position: relative;
            z-index: 1;
        }
        .container {
            background: rgba(255, 255, 255, 0.95);
            max-width: 600px;
            margin: 40px auto;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        }
        .main-title {
            font-family: 'Dancing Script', cursive;
            color: #FFC107; /* Golden Yellow */
            text-align: center;
            font-size: 3.5em;
            margin-bottom: 10px;
            animation: fadeIn 1.5s ease-in-out;
        }
        .sub-title {
            font-family: 'Poppins', sans-serif;
            color: #1A2A44; /* Midnight Blue */
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 30px;
            animation: fadeIn 2s ease-in-out;
        }
        .quote-box {
            background: #1A2A44; /* Midnight Blue */
            color: #F5F5F5; /* Soft White */
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #FFC107; /* Golden Yellow */
            margin: 20px 0;
            font-family: 'Poppins', sans-serif;
            font-style: italic;
            animation: slideInLeft 0.8s ease;
        }
        .countdown {
            background: #1A2A44; /* Midnight Blue */
            color: #F5F5F5; /* Soft White */
            text-align: center;
            font-size: 1.2em;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #FFC107; /* Golden Yellow */
            margin: 20px auto;
            width: fit-content;
            font-family: 'Poppins', sans-serif;
            animation: fadeIn 1s ease;
        }
        /* Animations */
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        @keyframes slideInLeft {
            0% { transform: translateX(-50px); opacity: 0; }
            100% { transform: translateX(0); opacity: 1; }
        }
        /* Streamlit elements */
        .stCheckbox > label, .stRadio > label, .stTextArea > label, .stFileUploader > label, .st-subheader {
            font-family: 'Poppins', sans-serif;
            color: #1A2A44; /* Midnight Blue */
            font-weight: 600;
            margin-bottom: 10px;
        }
        .st-subheader {
            text-align: center;
            font-size: 1.5em;
        }
        .stCheckbox, .stRadio, .stTextArea, .stFileUploader {
            background: #F5F5F5; /* Soft White */
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #1A2A44; /* Midnight Blue */
            transition: border-color 0.3s;
        }
        .stCheckbox:hover, .stRadio:hover, .stTextArea:hover, .stFileUploader:hover {
            border-color: #26A69A; /* Teal */
        }
        .stRadio > div {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .stRadio > div > label {
            color: #1A2A44; /* Midnight Blue */
            font-weight: 400;
        }
        .stButton > button {
            background: linear-gradient(45deg, #FFC107, #FFCA28); /* Golden Yellow to Amber */
            color: #1A2A44; /* Midnight Blue */
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            transition: transform 0.3s, background 0.3s;
            display: block;
            margin: 10px auto;
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, #26A69A, #4DB6AC); /* Teal gradient */
            transform: scale(1.05);
            color: #F5F5F5; /* Soft White */
        }
        .stSuccess, .stError {
            font-family: 'Poppins', sans-serif;
            text-align: center;
        }
        /* Footer (same as your original) */
        .footer {
            text-align: center;
            color: #FFFFFF;
            font-size: 1.5em;
            margin-top: 40px;
            margin-bottom: 20px;
            padding: 15px;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            border: 2px solid #FFC107; /* Golden Yellow */
            font-family: 'Poppins', sans-serif;
        }
        .footer a {
            color: #FFC107; /* Golden Yellow */
            text-decoration: none;
            margin: 0 15px;
            font-size: 1.2em;
            transition: transform 0.3s, color 0.3s;
        }
        .footer a:hover {
            color: #F5F5F5; /* Soft White */
            transform: scale(1.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main app
def main():
    # Add custom CSS
    add_custom_css()

    # Main container
    with st.container():
        st.markdown('<div class="container">', unsafe_allow_html=True)

        # Title and greeting
        st.markdown("<h1 class='main-title'>🌙 Chand Raat Mubarak! 🌙</h1>", unsafe_allow_html=True)
        st.markdown("<h3 class='sub-title'>Wishing you a night full of joy and blessings</h3>", unsafe_allow_html=True)

        # Countdown timer
        if st.checkbox("Show Eid Countdown"):
            now = datetime.now()
            time_left = eid_date - now
            st.balloons()
            if time_left.total_seconds() > 0:
                days = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                st.markdown(
                    f"<p class='countdown'>Eid is in: {days}d {hours}h {minutes}m {seconds}s</p>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown("<p class='countdown'>Eid Mubarak! The celebration begins!</p>", unsafe_allow_html=True)

        # Random quote generator
        if st.button("Generate a Wish", key="quote_btn", help="Click for a festive wish!"):
            random_quote = random.choice(quotes)
            st.markdown(f"<div class='quote-box'>{random_quote}</div>", unsafe_allow_html=True)

        # Share greetings section
        st.subheader("Share Your Greetings")
        greeting_option = st.radio("Choose format:", ("Text", "Image"))

        if greeting_option == "Text":
            user_greeting = st.text_area("Write your greeting:", height=100)
            if st.button("Share Text Greeting", key="text_btn"):
                if user_greeting:
                    st.markdown(f"<div class='quote-box'>Your greeting: {user_greeting}</div>", unsafe_allow_html=True)
                    st.success("Greeting shared successfully!")
                else:
                    st.error("Please enter a greeting!")
        
        else:  # Image sharing
            uploaded_image = st.file_uploader("Upload a festive image", type=["png", "jpg", "jpeg"])
            if uploaded_image and st.button("Share Image Greeting", key="img_btn"):
                st.image(uploaded_image, caption="Your Chand Raat Greeting", use_column_width=True)
                st.success("Image shared successfully!")

        st.markdown('</div>', unsafe_allow_html=True)

    # Footer (same as your original)
    st.markdown(
        """
        <div class='footer'>
            <p>Made by Osama bin Adnan with ❤️</p>
            <a href='https://www.linkedin.com/in/osama-bin-adnan/' target='_blank'>🌐 LinkedIn</a>
            <a href='https://x.com/osamabinadnan1' target='_blank'>🐦 X</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()