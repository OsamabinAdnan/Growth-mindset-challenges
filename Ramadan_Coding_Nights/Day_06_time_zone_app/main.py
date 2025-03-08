# Import required libraries
import streamlit as st  # Streamlit is used for creating interactive web apps
import streamlit.components.v1 as com # streamlit.components.v1 is used for embedding Lottie animations
from datetime import datetime  # datetime is used for handling date and time operations
from zoneinfo import ZoneInfo  # zoneinfo is used for working with time zones
import time

# Set up the Streamlit app configuration
st.set_page_config(
    page_title="Time Zone Converter App",  # Title of the webpage
    page_icon="⌚",  # Icon of the webpage
    layout="centered",  # Layout setting
    initial_sidebar_state="auto"  # Sidebar behavior
)

# Embed a Lottie animation using the com.iframe function
com.iframe("https://lottie.host/embed/f5e47b1a-c4a4-4569-8833-73e62b676b75/G666l1OwXH.lottie")

# Dictionary mapping display names to actual timezone keys
# The keys are user-friendly names with country information, 
# and the values are valid timezone identifiers recognized by ZoneInfo
Time_Zones = {
    "🌍 UTC": "UTC",
    "🇵🇰 Karachi": "Asia/Karachi",
    "🇺🇸 New York": "America/New_York",
    "🇬🇧 London": "Europe/London",
    "🇯🇵 Tokyo": "Asia/Tokyo",
    "🇦🇺 Sydney": "Australia/Sydney",
    "🇺🇸 Los Angeles": "America/Los_Angeles",
    "🇩🇪 Berlin": "Europe/Berlin",
    "🇦🇪 Dubai": "Asia/Dubai",
    "🇮🇳 Kolkata": "Asia/Kolkata",
    "🇺🇸 Honolulu": "Pacific/Honolulu",
    "🇺🇸 Chicago": "America/Chicago",
    "🇺🇸 Denver": "America/Denver",
    "🇺🇸 Phoenix": "America/Phoenix",
    "🇨🇦 Toronto": "America/Toronto",
    "🇮🇸 Reykjavik": "Atlantic/Reykjavik",
    "🇳🇿 Auckland": "Pacific/Auckland",
    "🇺🇸 Midway": "Pacific/Midway",
    "🇧🇷 Sao Paulo": "America/Sao_Paulo",
    "🇦🇷 Buenos Aires": "America/Argentina/Buenos_Aires",
    "🇺🇸 Anchorage": "America/Anchorage",
    "🇺🇸 Juneau": "America/Juneau",
}

# Display the app title
st.title("⏲️ Time Zone Converter App ⌛")

# 🌍 **Select Multiple Time Zones**
# Users can choose multiple time zones to view the current time in each
selected_time_zone = st.multiselect(
    "Select Time Zone",  # Dropdown label
    list(Time_Zones.keys()),  # Display user-friendly names
    default=["🌍 UTC", "🇵🇰 Karachi"]  # Default selected options
)

# Section to display the current time for selected time zones
st.subheader("Selected Time Zones:")

# Loop through each selected time zone and display the current time
for tz_display in selected_time_zone:
    tz_key = Time_Zones[tz_display]  # Get the actual timezone key from the dictionary
    current_time = datetime.now(ZoneInfo(tz_key)).strftime("%d-%m-%Y %I:%M:%S %p")  # Format in 12-hour format with AM/PM
    st.write(f"**{tz_display}**: {current_time}")  # Display time with user-friendly name

# 🌍 **Time Conversion Section**
st.subheader("Convert Time between Time Zones")

# Create an input field for selecting the time to convert
current_time = st.time_input(
    "Current Time of (From) Zone",  # Label for input field
    value=datetime.now().time()  # Default value set to the current system time
)

# **Select source (From) time zone**
from_tz_display = st.selectbox(
    "From Time Zone",  # Label for dropdown
    list(Time_Zones.keys()),  # Use user-friendly names
    index=0  # Default to UTC
)

# **Select destination (To) time zone**
to_tz_display = st.selectbox(
    "To Time Zone",  # Label for dropdown
    list(Time_Zones.keys()),  # Use user-friendly names
    index=1  # Default to Asia/Karachi (Pakistan)
)

# **Convert Button**
if st.button("Convert Time"):
    with st.spinner("Converting Time..."):  # Show a loading spinner
        time.sleep(2)  # Simulate a delay for demonstration purposes
        from_tz_key = Time_Zones[from_tz_display]  # Get the valid timezone key
        to_tz_key = Time_Zones[to_tz_display]  # Get the valid timezone key

        # Combine the selected time with today's date and assign the source time zone
        dt = datetime.combine(datetime.today(), current_time).replace(tzinfo=ZoneInfo(from_tz_key))

        # Convert the time to the destination time zone
        converted_time = dt.astimezone(ZoneInfo(to_tz_key)).strftime("%d-%m-%Y %I:%M:%S %p")

        # Display the converted time in a success message
        st.success(f"Converted Time in {to_tz_display} : {converted_time}")
