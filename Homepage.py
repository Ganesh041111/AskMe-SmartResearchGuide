import streamlit as st
import PyPDF2
import requests

st.set_page_config(
    page_title="Ask-Me",
    page_icon="📰",
)
st.title("Ask-Me Smart Research Guide")
st.image("./Images/AskMe-intro.gif")
st.sidebar.success("Select a page above.")

# Open the PDF file
pdf_file = st.file_uploader("Choose a file")

# Initialize variables
variable_names=st.text_input("Enter titles mentioned in document: ")

text=""
# Loop through each page of the PDF file
if variable_names and pdf_file is not None:
    variable_names=list(variable_names.split(" "))
    # Read the PDF file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.getNumPages()):
        # Get the text of the current page
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        text=text+" "+page_text

    variable_content=[]
    # Loop through each page of the PDF file
    for i in range(0,len(variable_names)-1):
        # Extract the abstract section
        if variable_names[i] in text:
            t=text
            content = t.split(variable_names[i], 1)[1]
            contentlist=list(content.split(" "))
            content=''
            for j in range(0,len(contentlist)):
                if str(contentlist[j]) == variable_names[i+1]:
                    break
                content=content+" "+str(contentlist[j])
        variable_content.append(content)


    if variable_names[-1] in text:
        t=text
        content = t.split(variable_names[-1], 1)[1]
        variable_content.append(content)


    # Print the different sections of the research article
    for i in range(0,len(variable_names)):
        # print(variable_names[i])
        # print(variable_content[i])
        with st.expander(variable_names[i]):
            st.write("Content: ",variable_content[i])
    pdf_file.close()


    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "XXXXXXXXXXXXXXXXXXXXX"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
	
    output = query({
	    "inputs": text
	
	    })
    st.title("What's in it?")
    st.image("./Images/8.gif")
    with st.expander("Quick Abstract"):
            st.write(output[0]["summary_text"])
