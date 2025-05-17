from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

class LLMWrapper:
    def __init__(self, system_prompt: str = ""):
        """Initialize the LLM with the OpenAI API key."""
        openai_api_key = os.environ.get("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is not set in the environment variables.")
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            openai_api_key=openai_api_key,
            system_prompt=system_prompt
        )

    def new_message(self, human_input: str, ai_prompt: str = ""):
        if ai_prompt:
            chat_prompt = ChatPromptTemplate.from_messages(
                [
                    
                    ("human", human_input),
                    ("ai", ai_prompt)

                ]
            )
        else:
            chat_prompt = ChatPromptTemplate.from_messages(
                [
                    ("human", human_input)
                ]
            )
        # Get the response from the LLM
        response = chat_prompt.invoke()
        return response if response is not None else None


