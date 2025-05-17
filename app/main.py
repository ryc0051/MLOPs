"""Module providing a function printing a translation using ChatOpenAI."""
import os
from app.llm.llm import LLMWrapper
from tools.pdfreader import PDFReader
import logging
logging.basicConfig(level=logging.INFO)
OpenAPIKey = os.environ.get("OPENAI_API_KEY")

if __name__ == "__main__":
    llm = LLMWrapper(system_prompt= 
                  """
                  You are a representive of a local government in New Zealand Otago.
                  You have a task of answering question  from the public on the Annual Plan 
                  and Long Term Plan. You are not allowed to give any legal advice.
                  """
                  )
    pdf_reader = PDFReader()
    pdf_reader.load_file("app/llm/annual_plan.pdf")
    
    
    