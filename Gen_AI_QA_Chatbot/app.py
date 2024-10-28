import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

## Langsmith Tracking

os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]= "Q&A Chatbot with OPENAI"


## Prompt Template

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user", "{question}")
    ]
)


def generate_response(question,api_key,engine,temperature,max_tokens):
    openai.api_key=api_key

    llm=ChatOpenAI(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer


## Title of the App

st.title("GenAI Q&A Chatbot with OpenAI")

# SIDEBAR FOR SETTINGS

st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

## Drop down to select various OpenAI models
engine = st.sidebar.selectbox("Select an OpenAI model", ["gpt-4o", "gpt-4-turbo","gpt-4"])

## Drop down to select various OpenAI models

temperature =st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7) ## value is default value, temperature=0.0  model is not creative, gives same answer every time you ask the same question
max_tokens =st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=175)

## Main Interface for user input
st.write("What do you want to know about Today, Ask me")
user_input=st.text_input("You:")



if user_input and api_key:
    response=generate_response(user_input,api_key,engine,temperature, max_tokens)
    st.write(response)

else:
    st.write("Please provide all the required user inputs")