import streamlit as st

st.set_page_config(
    page_title="Ask-Me",
    page_icon="📰",
)

st.title("FAQ Generator")
# st.image("./Images/Examsqna.gif")


col1, col2 = st.columns(2)

with col1:
   st.image("./Images/Examsqna.gif")

with col2:
   st.header("How to use: ")
   st.write("1. Enter text in the text-area.")
   st.write("3. Click on 'Generate Questions'.")

st.warning("Work in Progress :)")

########## 1st method 

# import numpy as np
# import nltk as nlp

# class SubjectiveTest:

#     def __init__(self, data, noOfQues):

#         self.question_pattern = [
#             "Explain in detail ",
#             "Define ",
#             "Write a short note on ",
#             "What do you mean by "
#         ]

#         self.grammar = r"""
#             CHUNK: {<NN>+<IN|DT>*<NN>+}
#             {<NN>+<IN|DT>*<NNP>+}
#             {<NNP>+<NNS>*}
#         """
#         self.summary = data
#         self.noOfQues = noOfQues
    
#     @staticmethod
#     def word_tokenizer(sequence):
#         word_tokens = list()
#         for sent in nlp.sent_tokenize(sequence):
#             for w in nlp.word_tokenize(sent):
#                 word_tokens.append(w)
#         return word_tokens
    
#     def create_vector(answer_tokens, tokens):
#         return np.array([1 if tok in answer_tokens else 0 for tok in tokens])
    
#     def cosine_similarity_score(vector1, vector2):
#         def vector_value(vector):
#             return np.sqrt(np.sum(np.square(vector)))
#         v1 = vector_value(vector1)
#         v2 = vector_value(vector2)
#         v1_v2 = np.dot(vector1, vector2)
#         return (v1_v2 / (v1 * v2)) * 100
    
#     def generate_test(self):
#         sentences = nlp.sent_tokenize(self.summary)
#         cp = nlp.RegexpParser(self.grammar)
#         question_answer_dict = dict()
#         for sentence in sentences:
#             tagged_words = nlp.pos_tag(nlp.word_tokenize(sentence))
#             tree = cp.parse(tagged_words)
#             for subtree in tree.subtrees():
#                 if subtree.label() == "CHUNK":
#                     temp = ""
#                     for sub in subtree:
#                         temp += sub[0]
#                         temp += " "
#                     temp = temp.strip()
#                     temp = temp.upper()
#                     if temp not in question_answer_dict:
#                         if len(nlp.word_tokenize(sentence)) > 20:
#                             question_answer_dict[temp] = sentence
#                     else:
#                         question_answer_dict[temp] += sentence
#         keyword_list = list(question_answer_dict.keys())
#         question_answer = list()
#         for _ in range(int(self.noOfQues)):
#             rand_num = np.random.randint(0, len(keyword_list))
#             selected_key = keyword_list[rand_num]
#             answer = question_answer_dict[selected_key]
#             rand_num %= 4
#             question = self.question_pattern[rand_num] + selected_key + "."
#             question_answer.append({"Question": question, "Answer": answer})
#         que = list()
#         ans = list()
#         while len(que) < int(self.noOfQues):
#             rand_num = np.random.randint(0, len(question_answer))
#             if question_answer[rand_num]["Question"] not in que:
#                 que.append(question_answer[rand_num]["Question"])
#                 ans.append(question_answer[rand_num]["Answer"])
#             else:
#                 continue
#         st.write(que)
#         st.write(ans)
#         return que, ans


# #inputText=st.text_area("Please enter your article")


# inputText="""Diwali is the season to celebrate with joy and cheer. It was the day when king Rama destroyed the evil forces and reached home to a rousing welcome by his subjects. Diwali has long been associated with bursting crackers, which is not in the true spirits of the festival. The main motive of the festival is to spread happiness with your loved ones. Festivals have been made to reinforce strong bonds between families and friends, and Diwali is the best example. Everyone goes home for Diwali and celebrates it with their families. It is a national holiday, so everyone enjoys the festival without worrying about work. It gets more exciting at night because lots of sky-lanterns are released into the air that flies high and lights up the night sky. Diwali teaches us to be patient for good things in life. Children keep waiting for many days to enjoy that bite of their favourite sweet. The houses are thoroughly cleaned to clean them of dirt. Cleanliness is very important as it would determine your wellness and health. It has been a part of Hindu culture for a very long time and fosters the moral lesson of “Good people always win over bad ones."""
# noOfQues=5

# subjective_generator = SubjectiveTest(inputText,noOfQues)
# question_list, answer_list = subjective_generator.generate_test()



########## 2nd method 
# from pprint import pprint

# from Questgen import main

# qe= main.BoolQGen()
# payload = {
#             "input_text": "Sachin Ramesh Tendulkar is a former international cricketer from India and a former captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket. He is the highest run scorer of all time in International cricket."
#         }
# output = qe.predict_boolq(payload)
# st.write(output)
# pprint (output)



