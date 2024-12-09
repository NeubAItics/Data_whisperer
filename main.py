import os
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LangChain with OpenAI key
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is not set in the environment file.")

def process_csv(file_path):
    """Processes the given CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    
    df = pd.read_csv(file_path)
    return df

def get_langchain_agent(file_path):
    """Creates a LangChain agent for interacting with the CSV file."""
    llm = ChatOpenAI(temperature=0.5)
    agent_executor = create_csv_agent(
        llm, 
        file_path, 
        verbose=True, 
        allow_dangerous_code=True
    )
    return agent_executor
