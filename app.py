import streamlit as st
from langchain_community.llms import Ollama
import pandas as pd
from pandasai import SmartDataFrame

llm = Ollama(model="llama3")


st.title("Data Analisis with PandasAI")

uploader_file = st.file_uploader("Upload a CSV file",type =["csv"])

if uploader_file is not None:
    data = pd.read_csv(uploader_file)
    st.write(data.head(3))
    df = SmartDataFrame(data, config={"llm":llm})
    prompt = st.text_area("Enter your Prompt:")

    if st.button("Generate:"):
        if prompt:
            with st.spinner(("Generative response...")):
                st.write(df.chat(prompt))
        else:
            st.warning("Please enter a prompt!")        
