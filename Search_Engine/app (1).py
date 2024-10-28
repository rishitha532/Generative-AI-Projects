import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

## Used the inbuilt tool of wikipedia
api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250) ## By default, it will return the page summaries of the top-k results. It limits the Document content by doc_content_chars_max.
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=1, documents_content_chars_max=250)
arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search=DuckDuckGoSearchRun(name='Search')

st.title("🔎 LangChain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

## Sidebar for settings

st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key:", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant", "content":"Hi, I'm a Chatbot who can search on the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if prompt:=st.chat_input(placeholder="What is Natural Language Processing?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm=ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
    tools=[search, arxiv, wiki]

    search_agent=initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parse_errors=True)

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
        response=search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant',"content":response})
        st.write(response)





## In Simple Words:

## StreamlitCallbackHandler: This is a special tool that helps show the steps or "thoughts" the chatbot agent goes through while answering a question. Think of it as a tool that provides a behind-the-scenes look at how the chatbot thinks and decides what to do next.

## st.container(): This is a part of the Streamlit app where content can be displayed. By using st.container(), we are telling Streamlit to create a space on the app's page where these "thoughts" or steps will be shown.

## expand_new_thoughts=True: This setting means that every time the chatbot takes a new step or makes a new decision, it will automatically expand and display the details of that step in the app. This makes it easier for users to see and understand each decision the chatbot is making in real-time.
