import streamlit as st
import requests

def get_random_jokes():
    """Fetch a random joke from the API"""
    try:
        # Make the GET request to joke API
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            joke_data = response.json()
            # Return formatted joke with setup and punchline (dictionary keys)
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
            
        else:
            # Return error message if API call fails
            return "Failed to fetch joke from the API"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def main():
    """Main function to run the Streamlit app"""
    # Set Streamlit page configuration
    st.set_page_config(
        page_title="Random Jokes",
        page_icon="🃏",
        layout="centered",
    )
    # Display app title
    st.title("Random Jokes Generator")

    # Add instruction
    st.write("Click the button below to generate a random Joke")

    # Create button and handle click
    if st.button("Tell me a Joke"):
        # Get random joke when button clicked
        joke = get_random_jokes()
        # Display joke with success styling
        st.success(joke)
    
    # Add horizontal line
    st.divider()

    # Footer using HTML, displaying text in the center
    st.markdown(
        """
        <div style='text-align:center;'>
            <p>😜 Joke from Official Joke API 😜</p>
            <p>Build with ❤️ by <a href='https://github.com/OsamabinAdnan'>Osama bin Adnan</a> using Streamlit</p>
        </div>
        """, unsafe_allow_html=True # Because we are rendering native HTML which has written inside the python
    )

if __name__ == "__main__":
    main()
        