import streamlit as st
import openai


st.set_page_config(
    page_title="Ask-Me",
    page_icon="🔘",
)
st.title("Intent Detection")


col1, col2 = st.columns(2)

with col1:
   st.image("./Images/docqna.gif")

with col2:
   st.header("How to use: ")
   st.write("1. Insert the text")
   st.write("2. Click on 'Find Intent'.")


openai.api_key ='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

prompt=st.text_input("Insert text here")
button = st.button("Find Intent")

with st.spinner("Finding intent..."):
    if button and prompt:
        response = openai.Completion.create(
          model="davinci:ft-personal-2023-03-13-15-40-35",
          prompt=prompt+"\n\nIntent:\n\n",
          max_tokens=5,
          temperature=0,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          stop=[" END"]
        )
        #st.success(response)
        st.write("Intent is: ",response['choices'][0]['text'])


