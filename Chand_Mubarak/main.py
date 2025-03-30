import streamlit as st
import random
from datetime import datetime
import base64

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

# Function to set background image (using a URL instead of local file)
def set_background():
    # Using a publicly hosted image URL for deployment
    image_url = "https://images.unsplash.com/photo-1579003593419-98f949b9398f?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            animation: fadeIn 2s ease-in-out;
            min-height: 100vh;
            position: relative;
        }}
        .stApp::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.4); /* Semi-transparent overlay */
            z-index: 0;
        }}
        .stApp > * {{
            position: relative;
            z-index: 1;
        }}
        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Custom CSS for animations and aesthetics
def add_custom_css():
    st.markdown(
        """
        <style>
        /* Import a festive font */
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

        /* General styling */
        .main-title {
            font-family: 'Great Vibes', cursive;
            color: #FFD700;
            text-align: center;
            font-size: 4em;
            animation: glow 1.5s ease-in-out infinite alternate;
            text-shadow: 0 0 10px #FFD700, 0 0 20px #FFFFFF;
            margin-top: 20px;
        }
        .sub-title {
            font-family: 'Arial', sans-serif;
            color: #FFFFFF;
            text-alignV: initial;
            text-align: center;
            font-size: 1.5em;
            animation: slideIn 1s ease-out;
            margin-bottom: 30px;
        }
        .quote-box {
            background-color: rgba(26, 60, 52, 0.9);
            padding: 20px;
            border-radius: 15px;
            color: #FFFFFF;
            font-style: italic;
            animation: bounceIn 0.8s ease;
            margin: 20px 0;
            border: 2px solid #FFD700;
        }
        .button-style {
            background-color: #FFD700;
            color: #1A3C34;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: bold;
            transition: transform 0.3s;
            display: block;
            margin: 10px auto;
        }
        .button-style:hover {
            transform: scale(1.1);
        }
        /* Animations */
        @keyframes glow {
            from { text-shadow: 0 0 5px #FFD700, 0 0 10px #FFFFFF; }
            to { text-shadow: 0 0 20px #FFD700, 0 0 30px #FFFFFF; }
        }
        @keyframes slideIn {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes bounceIn {
            0% { transform: scale(0.3); opacity: 0; }
            50% { transform: scale(1.05); opacity: 1; }
            100% { transform: scale(1); }
        }
        .countdown {
            color: #FFFFFF;
            text-align: center;
            font-size: 1.2em;
            background-color: rgba(0, 0, 0, 0.7);
            padding: 15px;
            border-radius: 10px;
            animation: pulse 2s infinite;
            margin: 20px auto;
            width: fit-content;
            border: 2px solid #FFD700;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .footer {
            text-align: center;
            color: #FFFFFF;
            font-size: 1.5em;
            margin-top: 40px;
            margin-bottom: 20px;
            padding: 15px;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            border: 2px solid #FFD700;
        }
        .footer a {
            color: #FFD700;
            text-decoration: none;
            margin: 0 15px;
            font-size: 1.2em;
            transition: transform 0.3s, color 0.3s;
        }
        .footer a:hover {
            color: #FFFFFF;
            transform: scale(1.2);
        }
        /* Improve Streamlit elements */
        .stCheckbox, .stRadio, .stTextArea, .stFileUploader, .stButton {
            background-color: rgba(255, 255, 255, 0.95);
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            border: 2px solid #FFD700;
        }
        .stCheckbox > label, .stRadio > label, .stTextArea > label, .stFileUploader > label {
            color: #FFFFFF;
            font-weight: bold;
            text-shadow: 1px 1px 2px #000000;
        }
        .stButton > button {
            background-color: #FFD700;
            color: #1A3C34;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: bold;
            transition: transform 0.3s;
            border: 2px solid #1A3C34;
        }
        .stButton > button:hover {
            transform: scale(1.1);
        }
        .stRadio > div {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .stRadio > div > label {
            color: #FFFFFF;
            font-weight: bold;
            text-shadow: 1px 1px 2px #000000;
        }
        .st-subheader {
            color: #FFD700;
            text-align: center;
            font-size: 1.8em;
            text-shadow: 1px 1px 2px #000000;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main app
def main():
    # Add custom CSS
    add_custom_css()

    # Set festive background using a URL
    set_background()

    # Title and greeting with animation
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

    # Footer with icons
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