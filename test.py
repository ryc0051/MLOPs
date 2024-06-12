"""Module providing a function printing python version."""
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

OpenAPIKey = os.environ.get("OPENAI_API_KEY")


def print_world():
    """Function printing python version."""
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)

if __name__ == "__main__":
    def main():
        "Main function."
    print_world()
