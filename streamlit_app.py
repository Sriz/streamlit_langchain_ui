import streamlit as st
from langchain.llms import OpenAI

st.title('Code Generator UI')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(prompt_text))

with st.form('my_form'):
    language = st.selectbox("Select a language",('Python','Java','C++'))
    prompt_text = st.text_input("Enter your prompt here", '', 5000, 2000)
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        text = prompt_text +' using '+language
        generate_response(text)
