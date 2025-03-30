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
        @import url('https://fonts.googleapis.com/css2?family=Lora:wght@600&family=Open+Sans:wght@400;600&display=swap');

        /* General styling */
        .stApp {
            background: #FFF8E1; /* Soft Cream */
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
            background: url('https://www.transparenttextures.com/patterns/arabesque.png');
            opacity: 0.1;
            z-index: 0;
        }
        .stApp > * {
            position: relative;
            z-index: 1;
        }
        .container {
            background: #FFFFFF; /* Pure White */
            max-width: 600px;
            margin: 40px auto;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        .main-title {
            font-family: 'Lora', serif;
            color: #212121; /* Jet Black */
            text-align: center;
            font-size: 3.2em;
            margin-bottom: 10px;
            animation: fadeIn 1.5s ease-in-out;
        }
        .sub-title {
            font-family: 'Open Sans', sans-serif;
            color: #212121; /* Jet Black */
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 30px;
            animation: fadeIn 2s ease-in-out;
        }
        .quote-box {
            background: #FFCC80; /* Golden Peach */
            color: #212121; /* Jet Black */
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #2ECC71; /* Emerald Green */
            margin: 20px 0;
            font-family: 'Open Sans', sans-serif;
            font-style: italic;
            animation: slideInLeft 0.8s ease;
        }
        .countdown {
            background: #FFCC80; /* Golden Peach */
            color: #212121; /* Jet Black */
            text-align: center;
            font-size: 1.2em;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #2ECC71; /* Emerald Green */
            margin: 20px auto;
            width: fit-content;
            font-family: 'Open Sans', sans-serif;
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
            font-family: 'Open Sans', sans-serif;
            color: #212121; /* Jet Black */
            font-weight: 600;
            margin-bottom: 10px;
        }
        .st-subheader {
            text-align: center;
            font-size: 1.5em;
        }
        .stCheckbox, .stRadio, .stTextArea, .stFileUploader {
            background: #FFFFFF; /* Pure White */
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #2ECC71; /* Emerald Green */
            transition: border-color 0.3s;
        }
        .stCheckbox:hover, .stRadio:hover, .stTextArea:hover, .stFileUploader:hover {
            border-color: #FFCC80; /* Golden Peach */
        }
        .stRadio > div {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .stRadio > div > label {
            color: #212121; /* Jet Black */
            font-weight: 400;
        }
        .stButton > button {
            background: #2ECC71; /* Emerald Green */
            color: #FFFFFF; /* White for contrast */
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            font-family: 'Open Sans', sans-serif;
            font-weight: 600;
            transition: transform 0.3s, background 0.3s;
            display: block;
            margin: 10px auto;
        }
        .stButton > button:hover {
            background: #FFCC80; /* Golden Peach */
            transform: scale(1.05);
            color: #212121; /* Jet Black */
        }
        .stSuccess, .stError {
            font-family: 'Open Sans', sans-serif;
            text-align: center;
            color: #212121; /* Jet Black */
        }
        /* Footer (same as your original, with color adjustments) */
        .footer {
            text-align: center;
            color: #212121; /* Jet Black */
            font-size: 1.5em;
            margin-top: 40px;
            margin-bottom: 20px;
            padding: 15px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            border: 2px solid #2ECC71; /* Emerald Green */
            font-family: 'Open Sans', sans-serif;
        }
        .footer a {
            color: #2ECC71; /* Emerald Green */
            text-decoration: none;
            margin: 0 15px;
            font-size: 1.2em;
            transition: transform 0.3s, color 0.3s;
        }
        .footer a:hover {
            color: #FFCC80; /* Golden Peach */
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

    # Footer (same as your original, with color adjustments)
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