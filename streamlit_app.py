import streamlit as st
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

st.title('Code Generator UI')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(text))

def get_cb_info(text):
    with get_openai_callback() as cb:
        llm = OpenAI()
        result = llm(text)
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost (USD): ${cb.total_cost}")

with st.form('my_form'):
    language = st.selectbox("Select a language",('Python','Java','C++'))
    prompt_text = st.text_input("Enter your prompt here", '', 5000, 2000)
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        text = prompt_text +' using '+language
        generate_response(text)
        get_cb_info(text)

