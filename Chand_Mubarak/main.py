import streamlit as st
import random
from datetime import datetime
import pytz

# Set page configuration
st.set_page_config(
    page_title="Chand Raat & Eid Mubarak",
    page_icon="🌙",
    layout="centered"
)

# Sample quotes
quotes = [
    "Chand Raat Mubarak! May this moonlit night bring peace and happiness.",
    "Wishing you a blessed Chand Raat filled with love and joy!",
    "May the moon sighting bring new hopes. Chand Raat Mubarak!",
    "Chand Raat Mubarak! Celebrate this beautiful night with loved ones.",
    "May Allah bless you this Chand Raat and always!"
]

timezone = pytz.timezone('Asia/Karachi')

# Eid date for countdown
eid_date = timezone.localize(datetime(2025, 3, 31, 0, 0, 0))

# Simplified CSS
def add_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');
        
        body {
            background: #FFF8E1;
            font-family: 'Open Sans', sans-serif;
            color: #212121;
        }
        .container {
            background: #FFFFFF;
            margin: 20px auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
        }
        h1 {
            text-align: center;
            font-size: 2em;
            margin-bottom: 10px;
        }
        h3 {
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        .quote-box {
            background: #F1EFEC;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #2ECC71;
            margin: 15px 0;
            font-style: italic;
        }
        .countdown {
            background: #F1EFEC;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #2ECC71;
            text-align: center;
            margin: 15px 0;
            font-weight: 600;
            font-size: 1.2em;
        }
        button {
            background: #2ECC71;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 600;
            display: block;
            margin: 10px auto;
        }
        button:hover {
            background: #F1EFEC;
            color: #212121;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 1em;
        }
        .footer a {
            color: #2ECC71;
            margin: 0 10px;
        }

        @media (max-width: 600px) {
            .container {
                margin: 10px;
                padding: 15px;
            }
            h1 { font-size: 1.8em; }
            h3 { font-size: 1em; }
            .quote-box, .countdown {
                margin: 10px 0;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main app
def main():
    add_custom_css()
    
    with st.container():
        st.markdown("<h1>🌙 Chand Raat Mubarak! 🌙</h1>", unsafe_allow_html=True)
        st.markdown("<h3>Wishing you joy and blessings</h3>", unsafe_allow_html=True)

        if st.checkbox("Show Eid Countdown"):
            now = datetime.now(timezone)
            time_left = eid_date - now
            st.balloons()
            if time_left.total_seconds() > 0:
                days = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes = remainder // 60
                st.markdown(f"<div class='countdown'>Eid in: {days}d {hours}h {minutes}m</div>", unsafe_allow_html=True)
            elif time_left.total_seconds() == 0:
                st.markdown("<div class='countdown'>Count down is over! Wishing you Eid Mubarak!</div>",unsafe_allow_html=True)

        if st.button("Generate Wish"):
            st.markdown(f"<div class='quote-box'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

        st.subheader("Share Your Greetings")
        greeting_option = st.radio("Format:", ("Text", "Image"))

        if greeting_option == "Text":
            user_greeting = st.text_area("Your greeting:", height=100)
            if st.button("Share Greeting") and user_greeting:
                st.markdown(f"<div class='quote-box'>{user_greeting}</div>", unsafe_allow_html=True)
                st.success("Greeting shared!")
        
        else:
            uploaded_image = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
            if uploaded_image and st.button("Share Image"):
                st.image(uploaded_image, caption="Your Greeting", use_column_width=True)
                st.success("Image shared!")

    st.markdown(
        """
        <div class='footer'>
            <p>Made by Osama bin Adnan with ❤️</p>
            <a href='https://www.linkedin.com/in/osama-bin-adnan/' target='_blank'>
                <img src='https://img.icons8.com/ios-filled/50/000000/linkedin.png' alt='LinkedIn' width=40px>
            </a>
            <a href='https://x.com/osamabinadnan1' target='_blank'>
                <img src='https://img.icons8.com/ios-filled/50/000000/x.png' alt='X' width=30px>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()