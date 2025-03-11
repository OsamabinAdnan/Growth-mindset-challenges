import streamlit as st  # Import Streamlit for building the web app
import random  # Import random to select random questions
import time  # Import time for adding delays
from questions import questions  # Import the list of questions from an external file

# ---- 🏆 Page Configuration ----
st.set_page_config(
    page_title="Quiz App",  # Set the page title
    page_icon="📝",  # Set an emoji as the page icon
    layout="centered",  # Center the layout
)

# ---- 📝 Title ----
st.title("📝 Quiz App ✍")  # Display the main title

# ---- 🔢 Set max questions limit ----
MAX_QUESTIONS = 10  # Define the maximum number of quiz questions

# ---- 📊 Initialize Session State Variables ----
if "score" not in st.session_state:
    st.session_state.score = 0  # Initialize score tracking

if "questions_count" not in st.session_state:
    st.session_state.questions_count = 0  # Initialize question count tracking

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)  # Pick a random question initially

if "answered" not in st.session_state:
    st.session_state.answered = False  # Initialize answer tracking

# ---- ⏳ Progress Bar ----
progress = st.progress(st.session_state.questions_count / MAX_QUESTIONS)  # Display progress bar

# ---- ✅ Check if quiz is completed ----
if st.session_state.questions_count >= MAX_QUESTIONS:
    st.success(f"✅ Quiz Completed! You scored {st.session_state.score} out of {MAX_QUESTIONS} questions.")  # Show final score
    st.balloons()  # Display balloons animation
    st.button("Restart Quiz", on_click=lambda: st.session_state.clear())  # Restart button
    st.stop()  # Stop further execution

# ---- ❓ Get the current question ----
question = st.session_state.current_question  # Retrieve the current question

# ---- 🎯 Display the Question ----
st.subheader(f"Question {st.session_state.questions_count + 1}: {question['question']}")  # Show the question number and text

# ---- 🎭 Create answer options ----
selected_option = st.radio("Choose your answer:", question['options'], key='answer')  # Display answer options

# ---- 🚀 Submit Answer Logic ----
if st.button("Submit Answer", disabled=st.session_state.answered):  # When the Submit button is clicked and Disable button after one click
    if selected_option == question['answer']:  # Check if the answer is correct
        st.success("✅ Correct Answer!")  # Show success message
        st.session_state.score += 1  # Increment the score
    else:
        st.error(f"❌ Incorrect Answer! The correct answer is: {question['answer']}")  # Show correct answer
    
    # Mark this question as answered to prevent multiple clicks
    st.session_state.answered = True

    # ---- 🔄 Update Question Count & Progress Bar ----
    st.session_state.questions_count += 1  # Increment question count
    progress.progress(st.session_state.questions_count / MAX_QUESTIONS)  # Update progress bar
    
    # ---- ⏳ Pause for 2 seconds ----
    time.sleep(2)
    
    # ---- 🎲 Select a new random question ----
    st.session_state.current_question = random.choice(questions)  # Get a new random question

    # Reset answered state for the next question
    st.session_state.answered = False
    
    # ---- 🔄 Rerun the app to display the next question ----
    st.rerun()  # Refresh the page
