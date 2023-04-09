import streamlit as st
from transformers import pipeline


st.set_page_config(
    page_title="Ask-Me",
    page_icon="📰",
)
st.title("Ask-Me Smart Research Guide")
st.title("Main Page")
st.sidebar.success("Select a page above.")


col1, col2 = st.columns(2)

with col1:
   st.image("./Images/Learning.gif")

with col2:
   st.header("How to use: ")
   st.write("1. Enter text in the text-area.")
   st.write("2. Ask your question based on the text.")
   st.write("3. Click on 'Find Answer'.")

@st.cache(allow_output_mutation=True)
def load_model():
    model=pipeline("question-answering")
    return model

qa= load_model()

articles=st.text_area("Please enter your article")
quest=st.text_input("Ask your question based on article")
button = st.button("Find Answer")

with st.spinner("Finding answer..."):
    if button and articles:
        answers=qa(question=quest, context=articles)
        st.success(answers)
        st.write("Answer for the question is: ",answers["answer"])