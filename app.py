# #local  run
# import os
# import pandas as pd
# import streamlit as st
# from main import process_csv, get_langchain_agent

# # Ensure the `data/` directory exists
# os.makedirs("data", exist_ok=True)

# # Add logo above the title
# st.image("./image.png", width=150)  # Replace 'logo.png' with the path to your logo image

# # App title and description
# st.title("Data Whisperer: Interactive Q&A")
# st.write("Upload a CSV file, explore the data, and interact with an AI-powered assistant.")

# # File upload section
# st.header("Upload Your Data")
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# if uploaded_file:
#     # Save the uploaded file
#     file_path = f"data/{uploaded_file.name}"
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     st.success("File uploaded successfully!")

#     # Process CSV
#     try:
#         # Read the CSV
#         df = pd.read_csv(file_path)
#         st.header("Explore Your Data")
#         st.write("Preview of uploaded data:")
#         st.dataframe(df.head())  # Display first few rows

#         # Allow users to select a column and input values
#         st.subheader("Filter Data by Column")
#         selected_column = st.selectbox("Select a column to filter", df.columns)

#         if st.button("Show Unique Values"):
#             unique_values = df[selected_column].unique()
#             st.write("Unique values in column:", unique_values)

#         # Allow the user to input a value to filter
#         filter_value = st.text_input(f"Enter a value to filter rows by '{selected_column}':")

#         if st.button("Filter Data"):
#             if filter_value:
#                 filtered_data = df[df[selected_column].astype(str).str.contains(filter_value, na=False)]
#                 st.write("Filtered data:")
#                 st.dataframe(filtered_data)
#             else:
#                 st.warning("Please enter a value to filter the data.")

#         # Perform operations using LangChain
#         st.header("Interact with AI Assistant")
#         st.write("Ask questions about the data.")

#         agent_executor = get_langchain_agent(file_path)

#         question = st.text_input("Enter your question for the AI Assistant:")
#         if st.button("Ask Question"):
#             response = agent_executor.invoke(question)
#             st.write("AI Bot Response:", response)

#     except Exception as e:
#         st.error(f"Error processing file: {e}")
# else:
#     st.info("Please upload a CSV file to get started.")

#streamlit deploy
import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from main import process_csv, get_langchain_agent

# Load environment variables from .env only if running locally
if not os.getenv("STREAMLIT_ENV"):
    load_dotenv()

# Access the API key from Streamlit secrets or environment variables
api_key = st.secrets.get("general", {}).get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

# Validate the API key
if not api_key:
    st.error("API key not found. Please check your Streamlit secrets or the `.env` file.")
    st.stop()

# Ensure the `data/` directory exists
os.makedirs("data", exist_ok=True)

# Add logo above the title
st.image("./image.png", width=150)  # Replace './image.png' with the path to your logo image

# App title and description
st.title("Data Whisperer: Interactive Q&A")
st.write("Upload a CSV file, explore the data, and interact with an AI-powered assistant.")

# File upload section
st.header("Upload Your Data")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Save the uploaded file
    file_path = f"data/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    # Process CSV
    try:
        # Read the CSV
        df = pd.read_csv(file_path)
        st.header("Explore Your Data")
        st.write("Preview of uploaded data:")
        st.dataframe(df.head())  # Display first few rows

        # Allow users to select a column and input values
        st.subheader("Filter Data by Column")
        selected_column = st.selectbox("Select a column to filter", df.columns)

        if st.button("Show Unique Values"):
            unique_values = df[selected_column].unique()
            st.write("Unique values in column:", unique_values)

        # Allow the user to input a value to filter
        filter_value = st.text_input(f"Enter a value to filter rows by '{selected_column}':")

        if st.button("Filter Data"):
            if filter_value:
                filtered_data = df[df[selected_column].astype(str).str.contains(filter_value, na=False)]
                st.write("Filtered data:")
                st.dataframe(filtered_data)
            else:
                st.warning("Please enter a value to filter the data.")

        # Perform operations using LangChain
        st.header("Interact with AI Assistant")
        st.write("Ask questions about the data.")

        agent_executor = get_langchain_agent(file_path)

        question = st.text_input("Enter your question for the AI Assistant:")
        if st.button("Ask Question"):
            response = agent_executor.invoke(question)
            st.write("AI Bot Response:", response)

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a CSV file to get started.")
