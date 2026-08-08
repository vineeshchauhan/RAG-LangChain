##Integrate OpenAI in our application

import os
from constants import openai_key
from constants import openai_base_url
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key
os.environ["OPENAI_BASE_URL"]=openai_base_url

## OPENNAI LLMS
llm = ChatOpenAI(
    temperature=0.7,
    model="openai/gpt-5-mini"
)

## Prompt template
first_input_prompt = ChatPromptTemplate.from_template(
    "Tell me about {name}"
)
##RunnableSequence
chain = first_input_prompt | llm

# Streamlit framework
st.title('Celebrity Search Results')
input_text = st.text_input("Search the topic u want")
if input_text:
    response = chain.invoke({"name": input_text})
    st.write(response.content)

