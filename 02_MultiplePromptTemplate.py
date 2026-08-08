##Integrate OpenAI in our application

import os
from constants import openai_key
from constants import openai_base_url
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
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

## Prompt template
second_input_prompt = ChatPromptTemplate.from_template(
    "What is DOB of {person}"
)

##RunnableSequence
parser = StrOutputParser()
first_chain = first_input_prompt | llm | parser
second_chain = second_input_prompt | llm | parser

# Streamlit framework
st.title('Celebrity Search Results')
input_text = st.text_input("Search the topic u want")
if input_text:
    person = first_chain.invoke({"name": input_text})
    dob = second_chain.invoke({"person": person})
    st.write(person)
    st.write(dob)

