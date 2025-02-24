import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our app
st.set_page_config(page_title="📀 Data Sweeper", layout="wide")
st.title("📀_Data Sweeper")
st.write("Transform your files 📂 between CSV and Excel formats")

# File upload
uploaded_file = st.file_uploader("Upload your files here (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

# Logic
if uploaded_file:  # Check if files are uploaded
    for file in uploaded_file:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read the file into a pandas DataFrame
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
        st.write(f"File Size: {file.size / 1024:.2f} KB")

        # Show 5 rows of the DataFrame
        st.write("Preview the head of the 📊 dataframe:")
        st.dataframe(df.head())

        # Option for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            # Remove duplicates
            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed Successfully!")

            # Fill missing values
            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    if not numeric_cols.empty:  # Check if there are numeric columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.write("Missing values filled successfully!")
                    else:
                        st.warning("No numeric columns found to fill missing values.")

        # Choose specific columns to keep or convert
        st.subheader("Select Columns to Convert!")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        
        # Handle empty columns selection
        if not columns:  # If no columns are selected
            st.warning("No columns selected. Using all columns by default.")
            columns = df.columns  # Use all columns
        
        df = df[columns]  # Subset the DataFrame

        # Create some visualizations
        st.subheader("📈 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            numeric_df = df.select_dtypes(include="number")
            if not numeric_df.empty:  # Check if there are numeric columns
                st.bar_chart(numeric_df.iloc[:, :2])  # Show the first two numeric columns
            else:
                st.warning("No numeric columns found for visualization.")

        # Convert the file -> CSV or Excel and Excel to CSV
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
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
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("🎉 All files processed!")