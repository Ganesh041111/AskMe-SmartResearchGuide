import streamlit as st
import PyPDF2
import os
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(
    page_title="Ask-Me",
    page_icon="🔍",
)
st.title("Semantic Search")


col1, col2 = st.columns(2)

with col1:
   st.image("./Images/docqna.gif")

with col2:
   st.header("How to use: ")
   st.write("1. Insert path of directory")
   st.write("2. Enter the query.")
   st.write("3. Click on 'Search'.")


pdf_dir = st.text_input("Path of directory")
query = st.text_input("Enter query")
button = st.button("Search")


# Define a function to perform semantic search
def semantic_search(query, tfidf_matrix, lsa_norm_matrix, vectorizer, lsa):
    # Convert the query into a TF-IDF vector
    query_vector = vectorizer.transform([query])

    # Reduce the dimensionality of the query vector using LSA
    query_lsa = lsa.transform(query_vector)

    # Normalize the query vector
    query_norm = normalizer.transform(query_lsa)

    # Compute cosine similarity between the query vector and the documents
    cosine_similarities = cosine_similarity(query_norm, lsa_norm_matrix).flatten()

    # Sort the documents by their cosine similarities with the query vector
    sorted_indices = cosine_similarities.argsort()[::-1]
    sorted_scores = cosine_similarities[sorted_indices]

    # Return the top 2 most similar documents
    top_k = 2
    top_documents = []
    for i in range(top_k):
        index = sorted_indices[i]
        score = sorted_scores[i]
        document = {
            'score': score,
            'text': documents[index]
        }
        top_documents.append(document)

    return top_documents





with st.spinner("Finding intent..."):
    if button and query and pdf_dir:
        # Read all PDF files and store the text in a list
        pdf_files = glob.glob(os.path.join(pdf_dir, "*.pdf"))
        documents = []
        for pdf_file in pdf_files:
        # Use any library to extract text from the PDF file
        # For example, you can use PyPDF2 or pdfminer.six
            with open(pdf_file, 'rb') as f:
                reader = PyPDF2.PdfFileReader(f)
                text = ''
                for page in reader.pages:
                    text += page.extract_text()
                    #text = extract_text_from_pdf(pdf_file)
                    documents.append(text)

        # Create a TF-IDF vectorizer to convert text into a matrix of TF-IDF features
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(documents)
        # Apply LSA to reduce the dimensionality of the TF-IDF matrix
        lsa = TruncatedSVD(n_components=100, algorithm='randomized', random_state=42)
        lsa_matrix = lsa.fit_transform(tfidf_matrix)

        # Normalize the LSA matrix
        normalizer = Normalizer(copy=False)
        lsa_norm_matrix = normalizer.fit_transform(lsa_matrix)

        results = semantic_search(query, tfidf_matrix, lsa_norm_matrix, vectorizer, lsa)
        for i, result in enumerate(results):
            print("Result %d (score=%.2f): %s" % (i+1, result['score'], result['text']))
            st.write("Result %d (score=%.2f): %s" % (i+1, result['score'], result['text']))
