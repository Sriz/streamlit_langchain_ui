# downloading necessary libraries
import streamlit as st
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from pydantic import BaseModel
from rich import print
from langchain.output_parsers import GuardrailsOutputParser
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from loguru import logger
from langchain.callbacks import FileCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# header of the UI
st.title('Code Generator UI')

#creating a text input for OpenAI API from user
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

#using callback to print log
logfile = "output.log"

logger.add(logfile, colorize=True, enqueue=True)
handler = FileCallbackHandler(logfile)

llm = OpenAI()
prompt = PromptTemplate.from_template(text)

chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler], verbose=False)
answer = chain.run(number=2)
logger.info(answer)


def generate_response(text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    result = llm(text)
    print(f"Number of Tokens used: {cb.total_tokens}")
    print(f"Amount Spent: ${cb.total_cost}")
    st.info(result)

def cb(text):
    with get_openai_callback() as cb:
        llm = OpenAI()
        result = llm(text)
        print(f"Number of Tokens used: {cb.total_tokens}")
    
with st.form('my_form'):
    language = st.selectbox("Select a language",('Python','Java','C++'))
    prompt_text = st.text_input("Enter your prompt here", '', 5000, 2000)
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        text = prompt_text +' using '+language
        generate_response(text)
        cb(text)
        
    



