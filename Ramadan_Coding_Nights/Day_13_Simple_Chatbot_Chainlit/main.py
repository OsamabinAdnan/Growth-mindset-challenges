# Import the chainlit library for building conversational AI applications
# 'cl' is used as an alias for easier reference throughout the code
import chainlit as cl

# Decorator that registers this function to handle incoming chat messages
# This function will be called whenever a user sends a message
@cl.on_message
async def main (message: cl.Message):
    # Create a response by concatenating "You said: " with the user's message
    # message.content contains the text sent by the user
    response = f"You said: {message.content}"

    # Send the response back to the chat interface
    # Using await because Message.send() is an asynchronous operation
    # cl.Message creates a new message object with our response text
    await cl.Message(content=response).send()