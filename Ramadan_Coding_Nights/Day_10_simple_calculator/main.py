# Import the Streamlit library for creating web applications
import streamlit as st

# Configure the page settings for the Streamlit app
st.set_page_config(
    page_title= "Simple Calculator",  # Set the browser tab title
    page_icon= "🧮",                  # Set the browser tab icon
    layout= "centered"                # Center the content on the page
)

def main():
    # Add the main title and description to the app
    st.title("🧮 Simple Calculator 📱")
    st.write("Enter two numbers and an operation to perform the calculation.")

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    # First column: Input field for the first number
    with col1:
        num1 = st.number_input("Enter the first number", value= 0.0, step=10.0)
    
    # Second column: Input field for the second number
    with col2:
        num2 = st.number_input("Enter the second number", value= 0.0,step=10.0)

    # Create a dropdown menu for selecting the operation
    operation = st.selectbox("Choose operation", 
        ["Addition(+)", "Substraction(-)", "Multiplication(x)", "Division(÷)"]
    )

    # Add a button to trigger the calculation
    if st.button("Calculate"):
        try:
            # Perform the selected operation
            if operation == "Addition(+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Substraction(-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication(x)":
                result = num1 * num2
                symbol = "x"
            else: # Division operation
                # Check for division by zero
                if num2 == 0:
                    st.error("Division by zero is not allowed")
                    return
                else:
                    result = num1 / num2
                    symbol = "÷"
            
            # Display the result with success styling
            st.success(f"{num1} {symbol} {num2} = {result}")

        # Handle any unexpected errors
        except Exception as e:
            st.error(f"An error occurred : {str(e)}")

# Python's entry point check
if __name__ == "__main__":
    main()  # Run the main application function