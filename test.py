"""Module providing a function printing python version."""
import os
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

OpenAPIKey = os.environ.get("OPENAI_API_KEY")


def print_world():
    """Function printing python version."""
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")

llm = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=  OpenAPIKey,temperature=0)
chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many employees are there"})
print(response)

if __name__ == "__main__":
    def main():
        "Main function."
    print_world()
