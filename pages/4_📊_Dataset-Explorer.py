import streamlit as st
from transformers import pipeline
import pandas as pd
import torch
import json



st.set_page_config(
    page_title="Ask-Me",
    page_icon="📰",
)

st.title("Dataset Analyzer")
# st.image("./Images/Data_report.gif")


col1, col2 = st.columns(2)

with col1:
   st.image("./Images/Data_report.gif")

with col2:
   st.header("How to use: ")
   st.write("1. Enter json formatted data in the text-area.")
   st.write("2. Ask your question based on the data.")
   st.write("3. Click on 'Find Answer'.")

#////
# tqa=pipeline(task="table-question-answering", model= "google/tapas-base-finetuned-wtq")
# # uploaded_file = st.file_uploader("Choose a file")

# table = pd.read_csv("pages/data.csv")
# table = table.astype(str)
# query = "Who has scored the highest runs?"
# st.write(tqa(table=table, query=query)["answer"])
#////

# table=pd.read_csv(uploaded_file)
# table=table.astype(str)

# query="who has scored highest runs?"
# st.write((tqa(table=table, query=query)["answer"]))

import requests

API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
headers = {"Authorization": "Bearer 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"}

# response="hhh"
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    response=response.json()
    with st.expander("Formatted Data"):
        st.write(payload)
    #st.write(payload)
    st.write("Query: ", payload["inputs"]["query"])
    st.write("Answer: ", response["answer"])
	# return 

tab=st.text_area("Enter data in json format: ")
que=st.text_input("Enter your query related with database:")


if tab and que is not None:
	tj=json.loads(tab)
	output = query({
		"inputs": {
			"query": que,
			"table": tj
		},
	})