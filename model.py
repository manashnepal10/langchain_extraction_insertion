import os 
from dotenv import load_dotenv 
import boto3
from langchain_aws import ChatBedrock
from schema import CompanyList

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')
AWS_REGION = os.getenv('AWS_REGION')

client = boto3.client(
    service_name = "bedrock-runtime",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
)

llm = ChatBedrock(
    client=client,
    model_id="amazon.nova-lite-v1:0",
)

structured_llm = llm.with_structured_output(schema=CompanyList)
