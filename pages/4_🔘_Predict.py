import streamlit as st
import openai

tab1, tab2, tab3 = st.tabs(["Software or Hardware", "Issue Classifier", "Intent Identification"])

with tab1:
   st.title("Software or Hardware")
   col1, col2 = st.columns(2)

   with col1:
      st.image("./Images/3.gif")

   with col2:
      st.header("How to use: ")
      st.write("1. Enter the text")
      st.write("2. Click on 'Predict'.")

   import streamlit as st 
   import pandas as pd 
   import matplotlib.pyplot as plt 
   import matplotlib
   matplotlib.use('Agg')
   import seaborn as sns 
   import altair as alt
   from datetime import datetime

   # Online ML Pkgs
   from river.naive_bayes import MultinomialNB
   from river.feature_extraction import BagOfWords,TFIDF
   from river.compose import Pipeline

   # Training Data
   data = [("my unit test failed","software"),
   ("tried the program, but it was buggy","software"),
   ("i need a new power supply","hardware"),
   ("the drive has a 2TB capacity","hardware"),
   ("unit-tests","software"),
   ("program","software"),
   ("power supply","hardware"),
   ("drive","hardware"),
   ("it needs more memory","hardware"),
   ("check the API","software"),
   ("design the API","software"),
   ("they need more CPU","hardware"),
   ("code","software"),
   ("i found some bugs in the code","software"),
   ("i swapped the memory","hardware"),
   ("i tested the code","software"),
   ("The software is not responding to my inputs", "software"),
   ("The computer is not booting up", "hardware"),
   ("The program is crashing on startup", "software"),
   ("The printer is jamming frequently", "hardware"),
   ("The software is producing unexpected errors", "software"),
   ("The computer is overheating and shutting down", "hardware"),
   ("The program is freezing while in use", "software"),
   ("The printer is producing low-quality prints", "hardware"),
   ("The software is not compatible with my operating system", "software"),
   ("The computer is displaying a blue screen error", "hardware"),
   ("The program is running slowly", "software"),
   ("The printer is not connecting to my computer", "hardware"),
   ("The software is not displaying the correct information", "software"),
   ("The computer is not recognizing my external monitor", "hardware"),
   ("The program is not saving my work", "software"),
   ("The printer is not recognizing the correct ink cartridges", "hardware"),
   ("The software is not loading properly", "software"),
   ("The computer is not recognizing my keyboard input", "hardware"),
   ("The program is not responding to specific actions", "software"),
   ("The printer is not scanning properly", "hardware"),
   ("The software is not displaying images correctly", "software"),
   ("The computer is not recognizing my mouse input", "hardware"),
   ("The program is not generating the expected output", "software"),
   ("The printer is not printing at all", "hardware"),
   ("The software is not working with specific hardware", "software"),
   ("The computer is not recognizing my USB device", "hardware"),
   ("The program is not displaying the correct language", "software"),
   ("The printer is not feeding paper correctly", "hardware"),
   ("The software is not displaying the correct time zone", "software"),
   ("The computer is not recognizing my CD drive", "hardware"),
   ("The program is not recognizing my input devices", "software"),
   ("The printer is not recognizing the correct paper tray", "hardware"),
   ("The software is not detecting my internet connection", "software"),
   ("The computer is not recognizing my graphics driver", "hardware"),
   ("The program is not displaying the correct file type", "software"),
   ("The printer is not printing double-sided correctly", "hardware"),
   ("The software is not recognizing my audio device", "software"),
   ("The computer is not recognizing my Bluetooth device", "hardware"),
   ("The program is not displaying the correct character encoding", "software"),
   ("The printer is not recognizing the correct page size", "hardware"),
   ("The software is not displaying the correct video output", "software"),
   ("The computer is not recognizing my printer", "hardware"),
   ("The program is not saving my files in the correct format", "software"),
   ("The printer is not recognizing the correct ink levels", "hardware"),
   ("The software is not recognizing my scanner", "software"),
   ("The computer is not recognizing my webcam", "hardware"),
   ("The program is not displaying the correct unit of measurement", "software"),
   ("The printer is not printing in color correctly", "hardware"),
   ("The software is not recognizing my touch screen", "software"),
   ("The computer is not recognizing my network adapter", "hardware")]


   # Model Building
   model = Pipeline(('vectorizer',BagOfWords(lowercase=True)),('nv',MultinomialNB()))
   for x,y in data:
      model = model.learn_one(x,y)


   with st.form(key='mlform'):
      col1,col2 = st.columns([2,1])
      with col1:
         message = st.text_area("Enter Text")
         submit_message = st.form_submit_button(label='Predict')

      with col2:
         st.write("Predict Text as Software or Hardware Related")

   if submit_message:
      prediction = model.predict_one(message)
      prediction_proba = model.predict_proba_one(message)
      probability = max(prediction_proba.values())
      st.write(probability)
      st.write(prediction_proba)



with tab2:
   import streamlit as st
   import joblib
   import os
   from PIL import Image
   import altair as alt
   import pandas as pd
   import numpy as np
   st.title("Issue Classifier")

   col1, col2 = st.columns(2)

   with col1:
      st.image("./Images/4.gif")

   with col2:
      st.header("How to use: ")
      st.write("1. Enter the text")
      st.write("2. Click on 'Predict'.")


   # Fxn To Load Model
   def load_model(model_file):
      model = joblib.load(open(os.path.join(model_file),"rb"))
      return model

   ISSUE_CLASSIFIER = load_model("G:/sem7/Major Project Features/github_issue_classifier/models/pipe_dt_cv_gh_issue_classifier_27_nov_2021.pkl")

   def plot_prediction_proba(term):
      pred_proba_df = pd.DataFrame({'Probabilities':ISSUE_CLASSIFIER.predict_proba([term])[0],'Classes':ISSUE_CLASSIFIER.classes_})
      c = alt.Chart(pred_proba_df).mark_bar().encode(
         x='Classes',
         y='Probabilities',
         color='Classes'
      )
      st.altair_chart(c)

   def load_image(image_file):
      img = Image.open(image_file)
      st.image(img)



   def main():
      
      

      menu = ["Home","Monitor","About"]
      #choice = st.sidebar.selectbox("Menu",menu)
      cchoice="Home"
      if cchoice == "Home":
         
         # Form
         with st.form(key='myForm'):
            text_issue = st.text_area("Enter Issue Here")
            submit_button = st.form_submit_button(label='predict')


         if submit_button:
            # Layout
            col1,col2 = st.columns(2)
            prediction = ISSUE_CLASSIFIER.predict([text_issue])
            pred_proba = ISSUE_CLASSIFIER.predict_proba([text_issue])
            probabilities = dict(zip(ISSUE_CLASSIFIER.classes_,np.round(pred_proba[0],3)))


            with col1:
               st.info("Original Issue")
               st.text(text_issue)

               st.info("Prediction")
               st.write(prediction[0])
               st.write(probabilities)


            with col2:
               plot_prediction_proba(text_issue)
               # st.help(st.metric)
            # st.metric(label='Accuracy',value='94',delta='0.2%')
            c1,c2,c3 = st.columns(3)
            c1.metric(label="Enhancement",value=probabilities['enhancement'],delta='{}%'.format(probabilities['enhancement']))
            c2.metric(label="Bug",value=probabilities['bug'],delta='{}%'.format(probabilities['bug']))
            c3.metric(label="Question",value=probabilities['question'],delta='{}%'.format(probabilities['question']))
   main()


with tab3:
   st.title("Intent Identification")
   col1, col2 = st.columns(2)

   with col1:
      st.image("./Images/5.gif")

   with col2:
      st.header("How to use: ")
      st.write("1. Insert the text")
      st.write("2. Click on 'Find Intent'.")


   openai.api_key ='XXXXXXXXXXXXXXXXXXXXX'

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


