import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our app
st.set_page_config(page_title="📀 Data Sweeper", layout="wide")
st.title("📀_Data Sweeper")
st.write("Transform your files 📂 between CSV and Excel formats")

# file upload
uploaded_file = st.file_uploader("Upload your files here (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

# logic
if uploaded_file:  # This is fine
    for file in uploaded_file:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read our file in pandas data frame
        if file_ext == ".csv":
            # Handle different encodings for CSV files
            file_content = file.getvalue()
            buffer = BytesIO(file_content)
            encodings = ['utf-8', 'latin1', 'cp1252', 'iso-8859-1', 'utf-16']
            df = None
            for encoding in encodings:
                try:
                    buffer.seek(0)  # Reset buffer position
                    df = pd.read_csv(buffer, encoding=encoding)
                    break
                except UnicodeDecodeError:
                    continue
            if df is None:
                st.error(f"Could not read {file.name} with common encodings. Please check the file encoding.")
                continue
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: format{file_ext}")
            continue

        # Display info about the file
        st.write(f"📁 File Name 📁: {file.name}")
        st.write(f"File Size: {file.size/1024} KB")

        # Show 5 rows of our data frame (df)
        st.write("Preview the head of the 📊 dataframe:")
        st.dataframe(df.head())

        # Option for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            # with is a contact manager
            with col1:
                # Add button to remove duplicates
                if st.button(f"Remove Duplicates from {file.name}"):
                    # pandas builtin function to drop duplicates
                    df.drop_duplicates(inplace=True) #inplace alter the state of original data frame
                    st.write("Duplicates Removed Successfully!")
            with col2:
                # Fill missing values
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    # fillna allow us to fill missing values with a specific value N/A or NaN
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values filled successfully!")
        # Choose specific columns to keep or convert
        st.subheader("Select Columns to Convert!")
        # Multi-select box to choose columns
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Create some visualizations
        st.subheader("📈 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])
        
        # Convert the file -> CSV or Excel and Excel to CSV
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Covert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Covert {file.name}"):
            # Bytes IO, it converts the data from you file into binary and store it in your memory for short term
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            # Download button
            st.download_button(
                label=f"🔻 Download {file.name} as {conversion_type}",
                data = buffer,
                file_name = file_name,
                mime = mime_type
            )
st.success("🎉 All files processed!")