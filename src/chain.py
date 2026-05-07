from src.model import structured_llm
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system", 
        """You are an expert at extracting company information.
            Extract ALL companies mentioned in the text — there may be more than one.
            For each company extract name, founding date, and founders.
            If only year is given, default to January 1st of that year.
            If year and month given, default to 1st of that month.
            If no company is mentioned, return empty list.
            IMPORTANT: If founding date is unknown or not mentioned, you MUST return null (not the string 'null', not 'None', but actual null/None value)."""
    ),
    (
        "human", "{paragraph}"
    )
])

extraction_chain = prompt | structured_llm