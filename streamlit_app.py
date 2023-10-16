import streamlit as st
import guardrails as gd
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from pydantic import BaseModel
from rich import print
from langchain.output_parsers import GuardrailsOutputParser
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI


st.title('Code Generator UI')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(text))

def get_cb_info(text):
    with get_openai_callback() as cb:
        llm = OpenAI()
        result = llm(text)
        print(f"Number of Tokens used: {cb.total_tokens}")
        print(f"Amount Spent: ${cb.total_cost}")

class Input(BaseModel):
    prompt: str
    
class Code(BaseModel):
    """Generated code"""
    language: str
    code: str
    
with st.form('my_form'):
    language = st.selectbox("Select a language",('Python','Java','C++'))
    prompt_text = st.text_input("Enter your prompt here", '', 5000, 2000)
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        text = prompt_text +' using '+language
        generate_response(text)
        guard = gd.Guard.from_pydantic(Code, prompt=text)

        raw_llm_output, validated_output = guard(
            openai.ChatCompletion.create,
            model="gpt-3.5-turbo",
            max_tokens=1024,
            temperature=0.0,
        )
        

