"""Module providing a function printing a translation using ChatOpenAI."""
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

OpenAPIKey = os.environ.get("OPENAI_API_KEY")


def print_world():
    """Function that translates text using ChatOpenAI."""
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
    result = chain.invoke(
        {
            "input_language": "English",
            "output_language": "German",
            "input": "I love programming.",
        }
    )
    return result


if __name__ == "__main__":
    print(print_world())  