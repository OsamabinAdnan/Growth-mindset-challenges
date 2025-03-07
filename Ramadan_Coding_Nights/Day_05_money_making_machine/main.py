# Import necessary tools/libraries
import streamlit as st  # Imports Streamlit for making web apps
import random  # Imports random number generator
import time  # Imports time-related functions
import requests  # Imports tool for making web requests

st.set_page_config(
    page_title="Money Making Machine",
    page_icon=":moneybag:",
    layout="centered")

# Set the title of our web app
st.title("💸 Money Making Machine 💰")


# Function to create random amount of money
def generate_money():
    return random.randint(1, 1000)  # Gives random number between 1 and 1000


# Create a section for generating money
st.subheader("Instant Cash Generator")
if st.button("Generate Money"):  # When user clicks the button
    st.write("Counting your money...")  # Show loading message
    time.sleep(3)  # Wait for 5 seconds
    amount = generate_money()  # Get random amount
    st.success(f"You made $ {amount} !")  # Show success message with amount


# Function to get Get Inspired with a Quote ideas from a server
def fetch_famous_quotes():
    try:
        # Try to get data from local server
        response = requests.get("https://dummyjson.com/quotes/random") # API taken from https://dummyjson.com/
        if response.status_code == 200:  # If request successful
            data = response.json()  # Convert response to JSON
            return f'"{data["quote"]}" — *{data["author"]}*'  # Return the hustle idea
        else:
            return "Failed to fetch quote!"  # Default response if server fails

    except:
        return "Something went wrong!"  # Error message if request fails


# Create a section for side hustle ideas
st.subheader("Get Inspired with a Quote")
if st.button("Generate Quote"):  # When user clicks button
    quote = fetch_famous_quotes()  # Get a hustle idea
    st.info(quote)  # Show the idea


# Function to get money-related quotes from server
def fetch_advices():
    try:
        # Try to get quote from local server
        response = requests.get("https://api.adviceslip.com/advice") # API taken from https://api.adviceslip.com/
        if response.status_code == 200:  # If request successful
            quotes = response.json()  # Convert response to JSON
            return quotes["slip"]["advice"]  # Return the quote
        else:
            return "Money is the root of all evil!"  # Default quote if server fails
    except:
        return "Something went wrong!"  # Error message if request fails


# Create a section for motivation quotes
st.subheader("Get Some Advices")
if st.button("Generate Advice"):  # When user clicks button
    quote = fetch_advices()  # Get a quote
    st.info(quote)  # Show the quote