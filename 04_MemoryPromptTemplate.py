##Integrate OpenAI in our application

import os
from constants import openai_key
from constants import openai_base_url
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
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
history = []

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert English Teacher for primary classes."),
     MessagesPlaceholder("history"),
    ("human", "{input}")
])

chain = prompt | llm

input_text = input("Input your question : ")
history.append(HumanMessage(input_text))

aiMessage = chain.invoke({"input":input_text,"history":history})
history.append(aiMessage.content)

input_text1 = input("Input your question : ")
history.append(HumanMessage(input_text1))
aiMessage1 = chain.invoke({"input":input_text1,"history":history})
history.append(aiMessage1.content)

print(history)
print(aiMessage1.content)