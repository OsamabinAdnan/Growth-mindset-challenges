# Import required libraries
import os  # For accessing environment variables
import chainlit as cl  # Framework for building chat applications
import google.generativeai as genai  # Google's Generative AI library
from dotenv import load_dotenv  # For loading environment variables from .env file

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini AI with the API key
genai.configure(api_key=gemini_api_key)

# Initialize the Generative AI model
# Using the 'gemini-2.0-flash' model which is optimized for faster responses
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash"
)

# Chainlit decorator that handles the start of a new chat session
@cl.on_chat_start
async def handle_chat_start():
    # Send an initial welcome message when a user starts the chat
    await cl.Message(content="Hello! I'm a Gemini AI chatbot. How can I help you?").send()

# Chainlit decorator that handles each message received from the user
@cl.on_message
# cl.Message is a class that represents chat messages.It handles message formatting, sending, and display in the chat interface
async def handle_message(message: cl.Message): # cl.Message creates a new message object with the specified content
    # Extract the content/prompt from the user's message
    prompt = message.content

    # Generate a response using the Gemini model
    response = model.generate_content(prompt)

    # Extract the text from the response
    # If response has a 'text' attribute, use it; otherwise use empty string
    response_text = response.text if hasattr(response, 'text') else ""

    # Send the response back to the user
    await cl.Message(content=response_text).send()