# Gemini Pro Chatbot App

This document describes a Streamlit web application that provides a chatbot interface powered by Google's Gemini AI model.

![Gemini AI](images/ai.png)

---

## Functionality

The app allows users to interact with the **Gemini AI model** in a conversational manner. Users can type messages into a **chat input field**, and the app will display both the user's message and the AI's response in a **formatted chat window**. A **typing effect** simulates the AI's response generation. 

### Features:
- **Chat History**: The conversation history is preserved within the user's session.
- **Sidebar Settings**: A sidebar provides options, including a button to **clear the chat history**.
- **Lottie Animations**: Enhances the user experience with animated elements.

---

## Technical Implementation

The application is built using the following technologies:

### **1. Streamlit**
- The primary framework for building the **user interface (UI)**.
- Simplifies the creation of interactive web applications with **Python**.

### **2. Google Generative AI (Gemini)**
- Provides the **conversational capabilities**.
- Uses the **Google Generative AI SDK** to interact with the **Gemini API**.

### **3. Python**
- The programming language used to develop the entire application.

### **4. dotenv**
- Manages **sensitive information** (such as the API key) by loading it from a **`.env`** file.
- Ensures the API key **remains secure** and is not hardcoded into the repository.

### **5. Lottie**
- Used for **animated loading icons** in the sidebar and main display.
- Animations are embedded via **iframes**.

---

## Key Steps in the Application

1. **Loads Environment Variables**  
   - Reads the **Google Cloud API key** from a `.env` file using `load_dotenv()`.  
   - Ensures the API key is not exposed in the code.

2. **Configures Streamlit**  
   - Sets up the **page title, icon, and layout** using `st.set_page_config()`.

3. **Initializes Gemini AI**  
   - Configures the Google Generative AI client using the **loaded API key**.  
   - Selects the `gemini-1.5-flash-latest` model.  
   - A commented-out section is included to **list available models**.

4. **Manages Chat Session**  
   - Uses Streamlit’s **session state (`st.session_state`)** to persist chat history.  
   - Starts a **new chat session** if one doesn’t exist.

5. **Handles User Input**  
   - Captures **user messages** from the chat input field.

6. **Processes Input & Generates Response**  
   - Sends the **user's prompt** to the **Gemini AI model** using `model.send_message()`.  
   - Implements a **typing effect** by displaying the response **character by character**.

7. **Displays Chat Messages**  
   - Renders messages with appropriate **roles** (`"user"` or `"assistant"`) using `st.chat_message()`.

8. **Clears Chat History**  
   - A **button in the sidebar** allows users to **reset the conversation**.

9. **Role Translation**  
   - A helper function (`translate_role_for_streamlit`) ensures **consistent role naming** between the **Gemini API** and **Streamlit's chat message display**.

---

## File Structure

The application consists of a **single Python file** containing all the code. A `.env` file should be created in the **same directory** to store the **GOOGLE_API_KEY**.

├── main.py # Main application code 

## Dependencies

The following Python packages are required:

- `streamlit`
- `google-generativeai`
- `python-dotenv`

### **Installation**
Install the required dependencies using pip:

```bash
pip install streamlit google-generativeai python-dotenv
```

### **Deployment**
To run the application, navigate to the directory containing **`main.py`** and run:

```bash
streamlit run main.py
```
### **Check App live**

**[Gemini Powered AI Chatbot](https://aipoweredchatbot-osamabinadnan.streamlit.app/)**

### **List of all models of Gemini till date**

- models/chat-bison-001
- models/text-bison-001
- models/embedding-gecko-001
- models/gemini-1.0-pro-vision-latest
- models/gemini-pro-vision
- models/gemini-1.5-pro-latest
- models/gemini-1.5-pro-001
- models/gemini-1.5-pro-002
- models/gemini-1.5-pro
- models/gemini-1.5-flash-latest
- models/gemini-1.5-flash-001
- models/gemini-1.5-flash-001-tuning
- models/gemini-1.5-flash
- models/gemini-1.5-flash-002
- models/gemini-1.5-flash-8b
- models/gemini-1.5-flash-8b-001
- models/gemini-1.5-flash-8b-latest
- models/gemini-1.5-flash-8b-exp-0827
- models/gemini-1.5-flash-8b-exp-0924
- models/gemini-2.0-flash-exp
- models/gemini-2.0-flash
- models/gemini-2.0-flash-001
- models/gemini-2.0-flash-lite-001
- models/gemini-2.0-flash-lite
- models/gemini-2.0-flash-lite-preview-02-05
- models/gemini-2.0-flash-lite-preview
- models/gemini-2.0-pro-exp
- models/gemini-2.0-pro-exp-02-05
- models/gemini-exp-1206
- models/gemini-2.0-flash-thinking-exp-01-21
- models/gemini-2.0-flash-thinking-exp
- models/gemini-2.0-flash-thinking-exp-1219
- models/learnlm-1.5-pro-experimental
- models/embedding-001
- models/text-embedding-004
- models/gemini-embedding-exp-03-07
- models/gemini-embedding-exp
- models/aqa
- models/imagen-3.0-generate-002