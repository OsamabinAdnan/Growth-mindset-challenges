import streamlit as st
import time

##@@@@@@@@@@@@@@@@@@@ To set page config @@@@@@@@@@@@@@@@@@@
st.set_page_config(page_title="Welcome to Streamlit Tutorials", page_icon="random", layout="wide", initial_sidebar_state="auto")

#@@@@@@@@@@@@@@@@@@@ title of the page @@@@@@@@@@@@@@@@@@@
st.title("This is title of the page")

#@@@@@@@@@@@@@@@@@@@ header of the page @@@@@@@@@@@@@@@@@@@
st.header("This is the header of the page")

#@@@@@@@@@@@@@@@@@@@ subheader of the page @@@@@@@@@@@@@@@@@@@
st.subheader("This is the subheader of the page")

#@@@@@@@@@@@@@@@@@@@ text of the page @@@@@@@@@@@@@@@@@@@
#  st.text(): Displays plain text exactly as provided, without formatting or interpretation.
st.text("This is the text of the page")

##@@@@@@@@@@@@@@@@@@@ paragraph of the page @@@@@@@@@@@@@@@@@@@
# st.write(): A versatile function that auto-formats text, numbers, Markdown, DataFrames, and more. It intelligently renders different data types.
st.write("This is the paragraph of the page write with help of st.write()")

#@@@@@@@@@@@@@@@@@@@ Markdown @@@@@@@@@@@@@@@@@@@
# st.markdown() function is used to render Markdown text in Streamlit.
st.subheader("Markdown")
st.markdown("## This is the markdown title")

#@@@@@@@@@@@@@@@@@@@ To make Button @@@@@@@@@@@@@@@@@@@
st.subheader("Button")
if st.button("Click Me!"):
    st.write("Button Clicked, Hello there!")
    st.balloons()
else:
    st.write("Button not clicked")

# https://docs.streamlit.io/develop/api-reference/status | check this link for more status functions like balloons

#@@@@@@@@@@@@@@@@@ Download button @@@@@@@@@@@@@@@@@@@@
# st.download_button allows users to download files directly from a Streamlit app.
# label → Button text (e.g., "Download File").
# data → The content to be downloaded (string, bytes, file, etc.).
# file_name → The name of the downloaded file (e.g., "report.csv").
# mime → (Optional) Specifies the file type (e.g., "text/plain", "image/png", "application/pdf").
st.subheader("Download Button")
data = "OsamabinAdnan"
st.download_button("Click to download", data = data, file_name = "data.txt")

#@@@@@@@@@@@@@@@@@@@ Link Button @@@@@@@@@@@@@@@@@@@
# st.link_button creates a clickable button that redirects users to an external URL.
# label → The text displayed on the button.
# url → The external link where the button redirects when clicked.
st.subheader("Link Button")
st.link_button("Click to go to Google", url = "https://www.google.com")

#@@@@@@@@@@@@@@@@@@@ Page Link @@@@@@@@@@@@@@@@@@@
# st.page_link is used for navigating between multiple pages in a multi-page Streamlit app.
# page → The target page (must be a relative path like "pages/page_name.py").
# label → (Optional) Button text; defaults to the page’s title.
# icon → (Optional) Adds an icon (e.g., "🏠" for home).
st.subheader("Page Link")
st.page_link("app.py", label="Home")

# @@@@@@@@@@@@@@@@ Data Editor @@@@@@@@@@@@@@@@@@@
# st.data_editor provides an interactive, editable table for users to modify data directly in a Streamlit app.
# data → The DataFrame or dictionary to display/edit.
# key → (Optional) Unique key for session state tracking.
# num_rows → "dynamic" (default) allows users to add/remove rows.
# disabled → True makes the table read-only.
# hide_index → True hides the index column.

# st.data_editor("Edit data", data)

# @@@@@@@@@@@@@@@@ Feedback @@@@@@@@@@@@@@@@@@@
# st.feedback allows users to provide feedback directly within a Streamlit app.
# label → The feedback prompt (e.g., "How was your experience?").
# optional_text → (Optional) Custom prompt text (e.g., "How was your experience?").
# rating → (Optional) Default rating ("happy", "neutral", "sad").
# key → (Optional) Unique key for session state tracking.
st.subheader("Feedback")
st.feedback("thumbs")

# @@@@@@@@@@@@@@@@ Pills @@@@@@@@@@@@@@@@@@@
# st.pills creates a set of pill-shaped selectable buttons for users to choose from. It works like a tab selector but with a more compact design.
# options → A list of options for the user to select from.
# index → (Optional) Default selected option (by index, default is 0).
# format_func → (Optional) Function to format display labels.
# key → (Optional) Unique key for session state tracking.
st.subheader("Pills")
st.pills("Tags", ["Sports", "Politics"])

# @@@@@@@@@@@@@@@@ Radio Button @@@@@@@@@@@@@@@@@@@
# st.radio creates a set of radio buttons for users to choose from.
# options → A list of options for the user to select from.
# index → (Optional) Default selected option (by index, default is 0).
# format_func → (Optional) Function to format display labels.
# key → (Optional) Unique key for session state tracking.
st.subheader("Radio Button")
st.radio("Select", ["Option 1", "Option 2", "Option 3"])

# @@@@@@@@@@@@@@@@ Segment Control @@@@@@@@@@@@@@@@@@@
# st.segmented_control creates a horizontal segmented button group that allows users to select one option at a time. It functions similarly to radio buttons but has a more modern, compact look.
# options → A list of options for selection.
# index → (Optional) Default selected option (by index, default is 0).
# format_func → (Optional) Function to format display labels.
# key → (Optional) Unique key for session state tracking.
st.segmented_control("Filter", ["Open", "Closed", "All"])

#@@@@@@@@@@@@@@@@@ Toggle Button @@@@@@@@@@@@@@@@@@@@
# st.toggle creates an interactive on/off switch (toggle button) that users can switch between True and False.
# label → Text displayed next to the toggle.
# value → (Optional) Default state (False by default).
# key → (Optional) Unique key for session state tracking.
# disabled → (Optional) If True, disables user interaction.
# label_visibility → (Optional) Controls label display ("visible", "hidden", "collapsed").
st.subheader("Toggle Button")
st.toggle("Show/Hide")

# @@@@@@@@@@@@@@@@ Selectbox @@@@@@@@@@@@@@@@@@@
# st.selectbox creates a dropdown menu for users to select from a list of options.
# label → Text displayed above the selectbox.
# options → A list of options for the user to select from.
# index → (Optional) Default selected option (by index, default is 0).
# format_func → (Optional) Function to format display labels.
# key → (Optional) Unique key for session state tracking.
st.subheader("Selectbox")
st.selectbox("Select", ["Option 1", "Option 2", "Option 3"])

# @@@@@@@@@@@@@@@@ Multiselect @@@@@@@@@@@@@@@@@@@
# st.multiselect creates a dropdown menu that allows users to select multiple options from a list.
# label → Text displayed above the multiselect.
# options → A list of options for the user to select from.
# default → (Optional) Default selected options.
# format_func → (Optional) Function to format display labels.
# key → (Optional) Unique key for session state tracking.
st.subheader("Multiselect")
st.multiselect("Select", ["Option 1", "Option 2", "Option 3"])

# @@@@@@@@@@@@@@@@ Slider @@@@@@@@@@@@@@@@@@@
# st.slider creates a slider widget for users to select a numeric value within a specified range.
# label → Text displayed above the slider.
# min_value → Minimum value of the slider.
# max_value → Maximum value of the slider.
# value → (Optional) Default selected value.
# step → (Optional) Step size for the slider.
# format_func → (Optional) Function to format display labels.
# key → (Optional) Unique key for session state tracking.
st.subheader("Slider")
st.slider("Select", 0, 100)

# @@@@@@@@@@@@@@@@ Select Slider @@@@@@@@@@@@@@@@@@@
# st.select_slider creates a slider widget with predefined values for users to select from.
# label → Text displayed above the select slider.
# options → A list of options for the user to select from.
# value → (Optional) Default selected value.
# format_func → (Optional) Function to format display labels.
# key → (Optional) Unique key for session state tracking.
st.subheader("Select Slider")
st.select_slider("Pick a size", ["S", "M", "L"])

# @@@@@@@@@@@@@@@ Checkbox @@@@@@@@@@@@@@@@@@@
# st.checkbox creates a checkbox widget that users can toggle between True and False.
# label → Text displayed next to the checkbox.
# value → (Optional) Default state (False by default).
# key → (Optional) Unique key for session state tracking.
# disabled → (Optional) If True, disables user interaction.
# label_visibility → (Optional) Controls label display ("visible", "hidden", "collapsed").
st.subheader("Checkbox")
st.checkbox("Check")

# @@@@@@@@@@@@@@@ Text Input @@@@@@@@@@@@@@@@@@@
# st.text_input creates a text input widget for users to enter text.
# label → Text displayed above the input box.
# value → (Optional) Default text value.
# disabled → (Optional) If True, disables user interaction.
# key → (Optional) Unique key for session state tracking.
# placeholder → (Optional) Placeholder text displayed when the input box is empty.
# max_chars → (Optional) Maximum number of characters allowed.
# label_visibility → (Optional) Controls label display ("visible", "hidden", "collapsed").
st.subheader("Text Input")
st.text_input("Enter text", placeholder="Enter your text here")

# @@@@@@@@@@@@@@@@ Number Input @@@@@@@@@@@@@@@@@@@
# st.number_input creates a numeric input widget for users to enter numbers.
# label → Text displayed above the input box.
# value → (Optional) Default numeric value.
# min_value → (Optional) Minimum allowed value.
# max_value → (Optional) Maximum allowed value.
# step → (Optional) Step size for the numeric input.
# format → (Optional) Format string for numeric values.
# key → (Optional) Unique key for session state tracking.
# disabled → (Optional) If True, disables user interaction.
# placeholder → (Optional) Placeholder text displayed when the input box is empty.
st.subheader("Number Input")
st.number_input("Pick a number", 0, 10)

# @@@@@@@@@@@@@@@@ File Uploader @@@@@@@@@@@@@@@@@@@
# st.file_uploader creates a file uploader widget that allows users to upload files to a Streamlit app.
# label → Text displayed above the file uploader.
# type → (Optional) File type filter (e.g., "csv", "png").
# key → (Optional) Unique key for session state tracking.
# accept_multiple_files → (Optional) If True, allows multiple files to be uploaded.
# disabled → (Optional) If True, disables user interaction.
# label_visibility → (Optional) Controls label display ("visible", "hidden", "collapsed").
st.subheader("File Uploader")
st.file_uploader("Upload file")

# @@@@@@@@@@@@@@@@ Audio Input @@@@@@@@@@@@@@@@@@@
# st.audio creates an audio player widget for users to play audio files.
# data → The audio data to be played.
# format → (Optional) Format of the audio data (e.g., "audio/mp3", "audio/wav").
# start_time → (Optional) Start time of the audio playback (in seconds).
# sample_rate → (Optional) Sample rate of the audio data.
st.subheader("Audio Input")
st.audio_input("Record a voice message")

# @@@@@@@@@@@@@@@@ Camera Input @@@@@@@@@@@@@@@@@@@
# st.camera creates a camera widget that allows users to take photos or record video.
# label → Text displayed above the camera widget.
# key → (Optional) Unique key for session state tracking.
st.subheader("Camera Input")
st.camera_input("Take a picture")

# @@@@@@@@@@@@@@@@ Color Picker @@@@@@@@@@@@@@@@@@@
# st.color_picker creates a color picker widget for users to select colors.
# label → Text displayed above the color picker.
# value → (Optional) Default color value.
# key → (Optional) Unique key for session state tracking.
# disabled → (Optional) If True, disables user interaction.
st.subheader("Color Picker")
st.color_picker("Pick a color")

# @@@@@@@@@@@@@@@@ Sidebar @@@@@@@@@@@@@@@@@@@
# st.sidebar creates a sidebar container that allows users to interact with widgets independently of the main app content.
# The st.sidebar module in Streamlit allows you to place UI elements (like buttons, sliders, and select boxes) in a collapsible sidebar instead of the main page.

# Sidebar elements
st.sidebar.title("Sidebar Menu")
option = st.sidebar.selectbox("Choose an option:", ["Home", "Dashboard", "Settings"])
slider_value = st.sidebar.slider("Select a value:", 0, 100, 50)

# Main page
st.write(f"You selected: {option}")
st.write(f"Slider value: {slider_value}")

# @@@@@@@@@@@@@@@@ Progress Bar @@@@@@@@@@@@@@@@@@@
# st.progress creates a progress bar widget that displays the progress of a task.
# value → The current progress value (between 0 and 1).
# key → (Optional) Unique key for session state tracking.
st.subheader("Progress Bar")
st.progress(0.5,  "Loading...")

# @@@@@@@@@@@@@@@@ Spinner @@@@@@@@@@@@@@@@@@@
# st.spinner creates a spinner widget that indicates a task is in progress.
# key → (Optional) Unique key for session state tracking.
st.subheader("Spinner")
with st.spinner("Loading..."):
    time.sleep(5)
    st.success("Done!")

# @@@@@@@@@@@@@@@@ Video @@@@@@@@@@@@@@@@@@@
# st.video creates a video player widget for users to play video files.
# data → The video data to be played.
# format → (Optional) Format of the video data (e.g., "video/mp4", "video/webm").
# start_time → (Optional) Start time of the video playback (in seconds).
st.subheader("Video")
st.video("https://www.youtube.com/watch?v=6tkb9HZ2-xk")

