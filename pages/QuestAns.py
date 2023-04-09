import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader
import requests

API_URL = "https://api-inference.huggingface.co/models/GaneshShingre/autotrain-ask-me-40630105428"
headers = {"Authorization": "Bearer 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"}

tab1, tab2, tab3 = st.tabs(["Text-Based", "Document-Based", "Video-Based"])

with tab1:
    st.header("Text-Based Question Answering")


    col1, col2 = st.columns(2)

    with col1:
        st.image("./Images/Learning.gif")

    with col2:
        st.header("How to use: ")
        st.write("1. Enter text in the text-area.")
        st.write("2. Ask your question based on the text.")
        st.write("3. Click on 'Find Answer'.")

    @st.cache(allow_output_mutation=True)
    def query(payload):
        res = requests.post(API_URL, headers=headers, json=payload) 
        return res.json()
        
    

    articles=st.text_area("Please enter your article")
    quest=st.text_input("Ask your question based on text")
    button = st.button("Find Answer.")

    with st.spinner("Finding answer..."):
        if button and articles:
            output = query({
	                 "inputs": {
		            "question": quest,
		            "context": articles
	                },
                    })
            st.success(output)
            st.write("Answer for the question is: ",output["answer"])

with tab2:
    st.header("Document-Based Question Answering")
    col1, col2 = st.columns(2)

    with col1:
        st.image("./Images/docqna.gif")

    with col2:
        st.header("How to use: ")
        st.write("1. Insert the document file in PDF format.")
        st.write("2. Ask your question based on the text.")
        st.write("3. Click on 'Find Answer'.")

    @st.cache(allow_output_mutation=True)
    def query(payload):
        res = requests.post(API_URL, headers=headers, json=payload) 
        return res.json()

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        text=""
        # To read file as string:
        pdf_file=uploaded_file
        # Read the PDF file
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        # Loop through each page of the PDF file
        for page_num in range(pdf_reader.getNumPages()):
        # Get the text of the current page
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()
            text=text+" "+page_text

    
        with st.expander("See text"):
            st.write(text)
    

    quest2=st.text_input("Ask your question based on article")
    button = st.button("Find Answer..")

    with st.spinner("Finding answer..."):
        if button and text:
            output = query({
	                 "inputs": {
		            "question": quest2,
		            "context": text
	                },
                    })
            st.success(output)
            st.write("Answer for the question is: ",output["answer"])

with tab3:
    st.header("Video-Based Question Answering")
    col1, col2 = st.columns(2)

    with col1:
        st.image("./Images/Mediaplayer.gif")

    with col2:
        st.header("How to use: ")
        st.write("1. Enter video url in the text-area.")
        st.write("2. Ask your question based on the video content.")
        st.write("3. Click on 'Find Answer for query'.")

    @st.cache(allow_output_mutation=True)
    def query(payload):
        res = requests.post(API_URL, headers=headers, json=payload) 
        return res.json()

    from youtube_transcript_api import YouTubeTranscriptApi
    youtube_video = st.text_input("Enter YouTube Video Link: ")
    quest3=st.text_input("Ask your question based on video")
    buttonss = st.button("Find Answer for query")




    if buttonss:
        with st.spinner("Finding answer..."):
            video_id = youtube_video.split("=")[1]
            from IPython.display import YouTubeVideo
            YouTubeVideo(video_id)
            YouTubeTranscriptApi.get_transcript(video_id)
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            result = ""
            for i in transcript:
                result += ' ' + i['text']
            with st.expander("See transcript"):
                st.write("Video Transcript: ",result)
        
        output = query({
	                 "inputs": {
		            "question": quest3,
		            "context": result
	                },
                    })
        st.success(output)
        st.write("Answer for the question is: ",output["answer"])
