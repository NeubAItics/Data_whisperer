# Data Whisperer: Interactive Q&A

## Overview

**Data Whisperer** is a Streamlit-based web application that enables users to upload a CSV file, explore the data, and interact with an AI-powered assistant. The assistant leverages LangChain and OpenAI's GPT to answer user queries about the data in real-time.

## Features

- **CSV File Upload**: Easily upload a CSV file for analysis.
- **Data Exploration**: Preview your data, view unique values in columns, and filter rows based on user-defined criteria.
- **AI-Powered Q&A**: Ask questions about the uploaded data and receive answers powered by LangChain and OpenAI GPT.

## Installation 🛠️

### Prerequisites 📋

- Python 3.8 or higher
- Streamlit
- OpenAI API key

### Setup Instructions ⚙️

1. **Clone the Repository** 📂
   ```bash
   git clone https://github.com/your-username/Data-Whisperer.git
   cd Data-Whisperer
   ```

2. **Create and Activate a Virtual Environment** 🌐
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies** 📦
   ```bash
   pip install -r requirements.txt
   ```

### Setup 🔧

1. **Obtain OpenAI API Key** 🔑
   Visit OpenAI's API page to generate your API key.

2. **Configure API Key** 🔐
   Add your API key to the secrets.toml file for secure storage:
   - Create the `.streamlit` directory if it doesn't exist:
     ```bash
     mkdir .streamlit
     ```
   - Create a `secrets.toml` file inside the `.streamlit` directory:
     ```toml
     [general]
     OPENAI_API_KEY = "your_openai_api_key_here"
     ```

3. **Verify `.gitignore`** 📄
   Ensure the `.streamlit/secrets.toml` file is excluded from version control. This is handled in `.gitignore`:
   ```
   # Add this line to .gitignore
   .streamlit/secrets.toml
   ```

### Running the Application 🚀

1. **Start the Streamlit App** 🖥️
   Run the application locally using Streamlit:
   ```bash
   streamlit run app.py
   ```

2. **Access the Application** 🌍
   Open your browser and navigate to the URL provided by Streamlit (e.g., http://localhost:8501).

## Project Structure 📂

```
.
├── data/                     # Directory to store uploaded CSV files
├── image.png                 # Logo for the application
├── app.py                    # Main Streamlit application file
├── main.py                   # Backend logic for processing CSV and LangChain agent
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── secrets.toml          # Secure storage for OpenAI API key
├── .env                      # Environment variables (not included in version control)
└── README.md                 # Documentation
```

## Environment Variables 🌱
The application requires the following environment variables
