from pydantic import BaseModel, Field, field_validator
from typing import List 
from datetime import date

class CompanyInfo(BaseModel):
    company_name: str = Field(description="The full official name of the company")
    founded_in: date | None = Field(
        default=None,
        description="""The date the company was founded. 
        If only year is given, default to January 1st of that year.
        If year and month are given, default to the 1st of that month.
        If founding date is unknown or not mentioned, return null — never return the string 'null' or 'None'."""
    ) 
    founded_by: List[str] = Field(description="List of founder names. If no founders, return an empty list.")

    @field_validator('founded_in', mode='before')
    @classmethod
    def handle_null_date(cls, v):
        if v in ('null', '', 'None', 'unknown'):
            return None
        return v


class CompanyList(BaseModel):
    companies: List[CompanyInfo] = Field(description="List of ALL companies mentioned in the paragraph. Return empty list if none found.")