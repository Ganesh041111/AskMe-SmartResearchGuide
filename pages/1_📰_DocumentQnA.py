import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="Ask-Me",
    page_icon="📰",
)

st.title("Document QnA")



col1, col2 = st.columns(2)

with col1:
   st.image("./Images/docqna.gif")

with col2:
   st.header("How to use: ")
   st.write("1. Insert the document file in PDF format.")
   st.write("2. Ask your question based on the text.")
   st.write("3. Click on 'Find Answer'.")

@st.cache(allow_output_mutation=True)
def load_model():
    model=pipeline("question-answering")
    return model






uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # To read file as string:
    file=uploaded_file
    # pdfFileObject = open(file, "rb")
    # pdfReader=PyPDF2.PdfFileReader(pdfFileObject)
    #print(f"No of pages: {pdfReader.numPages}")
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()


    ###
    # text=""
    # numpg=int(PdfReader.numPages)
    # for i in range(0,numpg):
    #     pageObject=PdfReader.getPage(i)
    #     text=text+" "+pageObject.extractText()
    
    with st.expander("See text"):
        st.write(text)
    





qa= load_model()

quest=st.text_input("Ask your question based on article")
button = st.button("Find Answer")

with st.spinner("Finding answer..."):
    if button and text:
        answers=qa(question=quest, context=text)
        st.success(answers)
        st.write("Answer for the question is: ",answers["answer"])