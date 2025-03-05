import streamlit as st  # Importing Streamlit for building the web app
import random  # Importing random module for generating random passwords
import string  # Importing string module to get different character sets

# Set up the page configuration
st.set_page_config(
    page_title="Password Generator 🔐",  # Title of the browser tab
    page_icon="🔑",  # Favicon or emoji for the tab
    layout="centered",  # Layout style: "centered" keeps it in the middle
    initial_sidebar_state="expanded"  # Sidebar starts expanded by default
)

# Function to generate a random password based on user preferences
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Start with uppercase and lowercase letters | Includes all letters from A to Z and a to z

    if use_digits:
        characters += string.digits  # Add digits (0-9) if selected
    if use_special:
        characters += string.punctuation  # Add special characters if selected
    
    # Generate a random password of the specified length using the characters defined above
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI setup
# App Title
st.title("🔒 Password Generator 🔑")  # Displays the main heading of the app

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select the length of the password:", min_value=6, max_value=20, value=12)

# Checkboxes to include digits and special characters
use_digits = st.checkbox("Include digits")  # Allows the user to include numbers in the password
use_special = st.checkbox("Include special characters")  # Allows the user to include special characters

# Button to generate the password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)  # Generate the password with selected options
    
    # Display the generated password in a styled format | Call the password generation function
    st.markdown(
        f"<p style='font-size:24px; font-weight:bold; display:inline;'>Generated Password: </p>"
        f"<span style='font-size:24px; font-weight:bold; color:green; background-color:lightgray; padding:3px; border-radius:5px;'>{password}</span>",
        unsafe_allow_html=True
    )

# Horizontal line for better UI separation
st.write("-------------------------------------")

# Footer with the creator's name and GitHub link
st.write("Build by ❤️ [Osama bin Adnan](https://github.com/OsamabinAdnan)")
