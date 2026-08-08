##Integrate OpenAI in our application

import os
from constants import openai_key
from constants import openai_base_url
from langchain_openai import ChatOpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key
os.environ["OPENAI_BASE_URL"]=openai_base_url

## OPENNAI LLMS
llm = ChatOpenAI(
    temperature=0.7,
    model="openai/gpt-5-mini"
)


# Streamlit framework
st.title('Langchain Demo with Open API')
input_text = st.text_input("Search the topic u want")
if input_text:
    st.write(llm.invoke(input_text))

