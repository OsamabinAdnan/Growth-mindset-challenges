import streamlit as st  # For creating web apps
import pandas as pd  # For data analysis and manipulation
import datetime  # For handling dates and times
import csv  # For reading and writing CSV files
import os  # For interacting with the operating system and file operations
import base64  # For encoding and decoding binary data

# Set up the Streamlit app configuration
st.set_page_config(
    page_title="Mood Tracker",  # Title of the web app
    page_icon="🤨",  # Emoji icon for the app
    layout="centered",  # Layout setting
)

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"  # A constant variable to store the filename

# Function to read mood data from the CSV file
def load_mood_data():
    """
    Loads mood data from a CSV file. If the file does not exist, 
    it returns an empty DataFrame with predefined columns.
    """
    if not os.path.exists(MOOD_FILE):  # Check if file exists
        return pd.DataFrame(columns=["Date", "Mood"])  # Return empty DataFrame
    return pd.read_csv(MOOD_FILE)  # Read and return the CSV file as a DataFrame

# Function to save mood data to the CSV file
def save_mood_data(date, mood):
    """
    Appends the given date and mood to the mood_log.csv file.
    """
    with open(MOOD_FILE, "a") as file:  # Open file in append mode
        writer = csv.writer(file)  # Create a CSV writer
        writer.writerow([date, mood])  # Write a new row with date and mood

# Function to encode an image file in Base64 format
def get_base64_image(image_path):
    """
    Reads an image file and encodes it in Base64 format.
    """
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    else:
        return None  # Return None if image doesn't exist
# Encode the image for display in HTML
img_base64 = get_base64_image("images/mood2.png")

# Use HTML + CSS to control image size and centering
if img_base64:
    st.markdown(f"""
        <style>
            .custom-img-container {{
                display: flex;
                justify-content: center; /* Centers horizontally */
                align-items: center; /* Centers vertically */
            }}
            .custom-img {{
                width: 220px;  /* Set width */
                height: 120px; /* Set height */
                object-fit: cover; /* Prevents distortion */
                border-radius: 10px; /* Optional: Rounded corners */
            }}
        </style>
        <div class="custom-img-container">
            <img src="data:image/png;base64,{img_base64}" class="custom-img">
        </div>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Image not found! Please upload 'mood2.png' to the 'images' folder.")

# Title of the app
st.title("🙂 Mood 😐 Tracker ☹️")

# Get the current date in DD-MM-YYYY format
today = datetime.date.today().strftime("%d-%m-%Y")

# User input section
st.subheader("How are you feeling today?")

# Dropdown menu for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Excited", "Neutral", "Anxious"])

# Button to log the mood
if st.button("Log Mood"):
    save_mood_data(today, mood)  # Save the selected mood with today's date
    st.success("Mood logged successfully!")  # Display success message

# Load existing mood data from file
data = load_mood_data()

# If there is data to display, show visualizations
if not data.empty:
    
    # Section for visualization
    st.subheader("Mood Trends Over Time")
    
    # Convert date strings to datetime objects for proper analysis
    data["Date"] = pd.to_datetime(data["Date"])
    
    # Count frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]
    
    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)

   # Build with love by Osama bin Adnan
    st.write("Build with ❤️ by [Osama bin Adnan](https://github.com/OsamabinAdnan)")