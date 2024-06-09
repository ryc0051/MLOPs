"""Module providing a function printing python version."""
import os
from langchain_openai import OpenAI
OpenAPIKey = os.environ.get('OPENAI_API_KEY')

def print_world():
    """Function printing python version."""
    llm = OpenAI(model_name="text-ada-001", openai_api_key=OpenAPIKey)
    print(llm("Tell me a joke about data scientist"))

if __name__ == "__main__":
    def main():
        "Main function."
    print_world()
