# import streamlit as st
# from main import process_csv, get_langchain_agent

# # App title
# st.title("Data Whisperer: Interactive Q&A with Your Company Data")

# # File upload section
# uploaded_file = st.file_uploader("Upload your data", type=["csv"])

# if uploaded_file:
#     # Save the uploaded file
#     file_path = f"data/{uploaded_file.name}"
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     st.success("File uploaded successfully!")

#     # Process CSV
#     try:
#         df = process_csv(file_path)
#         st.dataframe(df.head())  # Display first few rows

#         # Perform operations using LangChain
#         agent_executor = get_langchain_agent(file_path)

#         # Example operation: Sum of a column
#         column = st.selectbox("Select a column for operations", df.columns)
#         operation = st.selectbox("Select an operation", ["sum", "max", "min", "sort"])

#         if st.button("Perform Operation"):
#             if operation == "sum":
#                 result = df[column].sum()
#             elif operation == "max":
#                 result = df[column].max()
#             elif operation == "min":
#                 result = df[column].min()
#             elif operation == "sort":
#                 result = df.sort_values(by=column)

#             st.write(f"Result of {operation} on column '{column}':", result)

#         # LangChain question
#         question = st.text_input("Ask a question to AI Bot:")
#         if st.button("Ask your query to our AI Bot"):
#             response = agent_executor.invoke(question)
#             st.write("AI Bot Response to your Query:", response)
#     except Exception as e:
#         st.error(f"Error processing file: {e}")

import streamlit as st
from main import process_csv, get_langchain_agent

# Add an image above the title
st.image("D:/NeubAItics/langchainAgent/image.png", width=150)

# App title
st.title("Data Whisperer: Interactive Q&A")

# File upload section
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Save the uploaded file
    file_path = f"data/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    # Process CSV
    try:
        df = process_csv(file_path)
        st.dataframe(df.head())  # Display first few rows

        # Perform operations using LangChain
        agent_executor = get_langchain_agent(file_path)

        # Example operation: Sum of a column
        column = st.selectbox("Select a column for operations", df.columns)
        operation = st.selectbox("Select an operation", ["sum", "max", "min", "sort"])

        if st.button("Perform Operation"):
            if operation == "sum":
                result = df[column].sum()
            elif operation == "max":
                result = df[column].max()
            elif operation == "min":
                result = df[column].min()
            elif operation == "sort":
                result = df.sort_values(by=column)

            st.write(f"Result of {operation} on column '{column}':", result)

        # LangChain question
        question = st.text_input("Ask a question to AI Bot:")
        if st.button("Ask your query to our AI Bot"):
            response = agent_executor.invoke(question)
            st.write("AI Bot Response to your Query:", response)
    except Exception as e:
        st.error(f"Error processing file: {e}")
