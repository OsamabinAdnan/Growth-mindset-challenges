# Welcome to Chainlit! 🚀🤖

Hi there, Developer! 👋 We're excited to have you on board. Chainlit is a powerful tool designed to help you prototype, debug and share applications built on top of LLMs.

Chainlit is an open-source Python framework designed for building **conversational AI applications** quickly. It allows developers to create chatbot interfaces around **LLMs (Large Language Models)**, including OpenAI's GPT models, LangChain, and other AI frameworks.

With Chainlit, you can:

* Create **chatbot interfaces** with ease.
* Monitor **chat sessions** and **events**.
* Use **hooks and decorators** for handling messages and interactions.
* Extend functionality with **custom UIs and logging**

## Core Concepts in Chainlit

### 1. Chat Session

A chat session represents a single conversation between a user and the chatbot. It starts when a user sends a message and ends when they leave or restart the chat.

* Chainlit manages the session automatically.
* You can **store variables** within a session `(cl.user_session)`.
* Example: **Tracking user context or preferences**.

### 2. Events

Events in Chainlit refer to different stages in a chatbot's lifecycle. You can listen for these events to modify or extend behavior.

***Common events in Chainlit:***

* `on_message:` Triggered when the user sends a message.
* `on_chat_start:` Triggered when a new chat starts.
* `on_stop:` Triggered when the user stops the chat.

***Example: Handling messages in a chat session***

``` python
import chainlit as cl

@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content=f"Hello, you said: {message.content}").send()
```

### 3. Hooks

Hooks allow you to customize how Chainlit handles different parts of a conversation.

***Example Hooks:***

* @cl.on_message – Handles new user messages.
* @cl.on_chat_start – Runs when a chat session starts.
* @cl.on_stop – Runs when a session stops.

***Example: Logging when a chat starts***

``` python
@cl.on_chat_start
async def start_chat():
    print("Chat session started")
    await cl.Message(content="Welcome to Chainlit!").send()
```
### 4. Decorators

Decorators in Chainlit are special Python functions that modify chatbot behavior.

***Example: Using @cl.on_message***
``` python
@cl.on_message
async def reply_to_user(message: cl.Message):
    response = f"Your message: {message.content}"
    await cl.Message(content=response).send()
```


import chainlit as cl

## **State vs Stateless Conversations in Chainlit**

### 1. Stateless Conversations

A stateless conversation is one where each message is treated independently, without remembering previous interactions. Here's an example:

``` python

import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # Each response is independent of previous messages
    response = f"You said: {message.content}"
    await cl.Message(content=response).send()

```


GitHub Copilot
Let me explain state and stateless conversations in Chainlit:

State vs Stateless Conversations in Chainlit
Stateless Conversations
A stateless conversation is one where each message is treated independently, without remembering previous interactions. Here's an example:

### 2. Stateful Conversations
Chainlit provides state management through `cl.user_session`, allowing you to maintain context across messages. Here's an example:

``` python

import chainlit as cl

@cl.on_chat_start
async def start():
    # Initialize session state
    cl.user_session.set("message_count", 0)

@cl.on_message
async def main(message: cl.Message):
    # Get and update message count
    count = cl.user_session.get("message_count")
    cl.user_session.set("message_count", count + 1)
    
    response = f"Message #{count + 1}: {message.content}"
    await cl.Message(content=response).send()
    
```
### **Key Differences:**

#### **1. State Storage**
* Stateless: No information is stored between messages
* Stateful: Uses `cl.user_session` to store and retrieve data

#### **2. Context Awareness**

* Stateless: Each message is processed independently
* Stateful: Can reference previous interactions and maintain context

#### **3. Memory Usage**

* Stateless: Lower memory usage
* Stateful: Requires memory to maintain session data

#### **4. Use Cases**

* Stateless: Simple echo bots, basic Q&A
* Stateful: Complex conversations, user preferences, multi-turn dialogues

----

## Useful Links 🔗

- **Documentation:** Get started with our comprehensive [Chainlit Documentation](https://docs.chainlit.io) 📚
- **Discord Community:** Join our friendly [Chainlit Discord](https://discord.gg/k73SQ3FyUh) to ask questions, share your projects, and connect with other developers! 💬
- **Github:** Check repo [Github](https://github.com/Chainlit/chainlit)

We can't wait to see what you create with Chainlit! Happy coding! 💻😊

## Welcome screen

To modify the welcome screen, edit the `chainlit.md` file at the root of your project. If you do not want a welcome screen, just leave this file empty.
