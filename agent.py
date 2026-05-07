from database import insert_company
from langchain.agents import create_agent
from model import llm

tools = [insert_company]

agent_executor = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are an agent that inserts company data into a database using the available tool."
)