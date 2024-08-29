import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Function to generate documentation
def generate_documentation(logs):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("No API key found. Make sure OPENAI_API_KEY is set.")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    # Specify model and message to generate the documentation
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': f'Generate detailed documentation from the following deployment log: {logs}'}
        ],
        'max_tokens': 1000
    }
    # POST request for OpenAI API
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
    
    response_json = response.json()
    if 'choices' not in response_json or not response_json['choices']:
        raise Exception(f"Unexpected API response format: {response_json}")
    
    return response_json['choices'][0]['message']['content']

# Script block
if __name__ == "__main__":
    log_file_path = os.path.join(os.getcwd(), "deployment_log.txt")
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"The log file {log_file_path} does not exist.")
    
    with open(log_file_path, "r") as log_file:
        logs = log_file.read()
    
    documentation = generate_documentation(logs)
    
    with open("deployment_documentation.md", "w") as doc_file:
        doc_file.write(documentation)