
import streamlit as st
from streamlit_option_menu import *
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import json as js
import time
import gtts
from gtts import gTTS
import os
import requests
import pandas as pd
import os 
from dotenv import load_dotenv , find_dotenv
from inference import OPEN_AI
import pymongo as pm
from textblob import TextBlob 



#__________________________________________________________


class language_ai :

    def method(self):
        st.set_page_config(page_title='Language AI Project By Praveen', layout="wide")
        
        # Object for OPEN_AI
        response = OPEN_AI()

        with st.sidebar:  # Navbar
            selected = option_menu(
                menu_title="Language AI",
                options=['Intro',"Sentiment Analysis", "Language Translator",'Speech Synthesis', 'Summarization','Table Question Answering System','Question Answering System'
                         ,'Feedback'],
                icons=['mic-fill', 'emoji-heart-eyes-fill', 'translate', 'megaphone-fill', 'text-paragraph',"table","question-square-fill",'envelope-at-fill'],
                menu_icon='code-square',
                default_index=0,
            )
        
            
        # Load Animation Files 
        def lottie(filepath):
            with open(filepath, 'r') as file:
                return js.load(file)
            
       
        if selected == 'Sentiment Analysis':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            col1, col2 ,col3= st.columns([4,7 ,3])

            col2.markdown(
                "<h1 style='font-size: 75px;'><span style='color: cyan;'>Sentiment</span> <span style='color: white;'>Analysis</span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col1, col2, col3, col4 = st.columns([10, 10, 10, 10])
            with col1:
                file = lottie("smile_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=350,
                    key=None
                )
            col3.write("")
            col3.write('')
            with col2:
                file = lottie("angry_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=350,
                    key=None
                )
            col3.write("")
            with col3:
                file = lottie("sad.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=250,
                    key=None
                )
            with col4:
                file = lottie("love_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=340,
                    key=None
                )
            col1.write("")
            col1.write("")
            col1.write("")
            col1, col2, col3 = st.columns([3, 7, 3])

            # Sentiment analyszer
            with col2:
                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color: white;'>Enter </span><span style='color: cyan;'>   Review</span>  </h1>",
                    unsafe_allow_html=True)
                Text = st.text_input("")

            col1, col2, col3 = st.columns([8.5, 7, 3])
            if col2.button('Proceed'):
              
                # Chain of thoughts and few shot learning
                prompt = f"""
                Instruction :

                1. You should act responsible Sentiment Analyser.

                2. Find What is the sentiment of the following Text,\
                which is delimited with triple backticks?

                3. Give your answer as a single word, either "Positive" \
                or "Negative" or "Neutral

                Example :
                Q: he is a good boy 
                A: Positive

                Q: she is okay now
                A: Neutral

                Q: she has wrost behavior
                A: Negative

                Q: she is a coder
                A: Neutral

                Text: '''{Text}'''
                """
                sentiment = response.get_completion(prompt=prompt)
                col1, col2, col3 = st.columns([5, 9, 3])
                col2.write("")
                col2.write("")
                col2.write('')  
                col2.write('')

                if str(sentiment) == 'Negative' :
                    col2.markdown(

                        f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Negative </span><span style='color: white;'> Text : </span> <span style='color: white;'>{Text}</span></h1>",
                        unsafe_allow_html=True)
                elif str(sentiment) == 'Positive':
                    col2.markdown(  
                        f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Positive </span><span style='color: white;'> Text : </span> <span style='color: white;'> {Text}</span></h1>",
                        unsafe_allow_html=True)
                elif str(sentiment) == 'Neutral':
                    col2.markdown(

                        f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Neutral </span><span style='color: white;'> Text : </span> <span style='color: white;'> {Text}</span></h1>",
                        unsafe_allow_html=True)

                else :
                    col2.markdown(
                        f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Neutral </span><span style='color: white;'> Text : </span> <span style='color: white;'>{Text}</span></h1>",
                        unsafe_allow_html=True)
#___________________________________________________________________________________________________________________________________________
        elif selected == 'Language Translator':

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([4.5, 10, 3])
            col2.markdown(
                "<h1 style='font-size: 69px;'><span style='color: white;'>Language</span> <span style='color: cyan;'>Translator</span> </h1>",
                unsafe_allow_html=True)
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            col1, col2 = st.columns([10, 10])
            col1.markdown(
                "<h1 style='font-size: 30px;'><span style='color: white;'>Provide</span> <span style='color: cyan;'>Text</span> </h1>",
                unsafe_allow_html=True)
            col2.markdown(
                "<h1 style='font-size: 28px;'><span style='color: white;'>Select </span> <span style='color: cyan;'> Language</span> </h1>",
                unsafe_allow_html=True)

            col1, col2 = st.columns([10, 10])

            
            with open('languages.txt','r',encoding='utf-8') as file :
                languages_name = file.read()
                languages_name = languages_name.split('\n')
            
            selected_lan = col2.selectbox('', languages_name)

            text = col1.text_input(" ")

            prompt = f"""
            # Translate the following English text to {selected_lan}:
            Text :{text}
            """

            col1, col2, col3 = st.columns([18, 10, 10])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")  
            if col2.button('Convert'):
                
                with st.spinner('Converting...'):
                    time.sleep(3)

                response = response.get_completion(prompt=prompt)#

                col3, col1, col2, col4 = st.columns([9, 45, 20, 7])
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                # col2.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.markdown(
                    f"<h1 style='font-size: 30px;'><span style='color: cyan;'>Provided Text : </span> <span style='color: white;'>{text}</span></h1>",
                    unsafe_allow_html=True)

                col2.markdown(
                    f"<h1 style='font-size: 30px;'><span style='color: cyan;'>Converted Text : </span><span style='color: white;'>{response}</span></h1>",
                    unsafe_allow_html=True)
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
# #___________________________________________________________________________________________________________________________________________
        elif selected == 'Speech Synthesis':

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)


            col1, col2, col3 = st.columns([4, 7, 3])

            col2.markdown(
                "<h1 style='font-size: 69px;'><span style='color: cyan;'>Speech</span> <span style='color: white;'>Synthesis</span> </h1>",
                unsafe_allow_html=True)
           
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            col4, col1, col2= st.columns([3, 10, 3])
            
            with col1:
                file = lottie("speech.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=800,
                    key=None
                )

            col1, col2, col3 = st.columns([4, 7, 4.3])
            col2.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide</span> <span style='color: white;'>Text</span> </h1>",
                unsafe_allow_html=True)

            input = col2.text_input("")
            with col2:
                if st.button('Proceed'):
                    # English Language Specified Here
                    language = 'en'

                    # Object Creation for gTTS Class
                    text_to_speech = gTTS(text=input, lang=language, slow=False)

                    # Save Audio File
                    text_to_speech.save("output.mp3")

                    # os.system("start output.mp3")
                    col2.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Audio</span> <span style='color: white;'>File :</span> </h1>",
                unsafe_allow_html=True)
                    st.write("")
                    st.audio("output.mp3")
# #___________________________________________________________________________________________________________________________________________
        elif selected == "Summarization":
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            col1, col2, col3 = st.columns([3, 7, 2])


            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color: cyan;'>Summarization</span> <span style='color: white;'>Process</span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col4, col1, col2 = st.columns([9.5, 10, 10])

            with col1:
                file = lottie("summarization.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=500,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
           
            col1, col2, col3 = st.columns([3, 7, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                col2.markdown(
                    "<h1 style='font-size: 50px;'><span style='color: cyan;'>Provide</span> <span style='color: white;'>Text</span> </h1>",
                    unsafe_allow_html=True)
                text = st.text_area("")

                col2.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Total Words</span> <span style='color: white;'>Count</span> </h1>",
                    unsafe_allow_html=True)

                no_of_words = st.number_input("", min_value=0, max_value=100, value=30, step=1)
                col2.write("")

                if st.button('Proceed'):
                    

                    prompt = f"""
                    Summarize the given text in the triple backticks ''' into {no_of_words} words
                    '''{text}'''
                    """

                                    
                    response = response.get_completion(prompt=prompt)

                    col2.write("")
                    col2.write("")
                    col2.write("")

                    col2.markdown(
                    f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Summary </span> <span style='color: cyan;'>Text :</span> </h1>",
                    unsafe_allow_html=True)

                    col2.markdown(
                    f"<h1 style='font-size: 30px;'><span style='color: white;'>{response}</span> <span style='color: white;'></span> </h1>",
                    unsafe_allow_html=True)         
# #_____________________________________________________________________________________________________________________________________
        elif selected == 'Table Question Answering System':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 7, 1])

            col2.markdown(
                "<h1 style='font-size: 63px;'><span style='color: cyan;'>Table </span> <span style='color: white;'>Questioning </span><span style='color: white;'>Answering </span><span style='color: cyan;'> System</span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            data = {
                "name": ["praveen", "thambey", "shabarinath", 'viswanathan', 'anna lakshmi', 'pavan', 'vigesh',
                         'vengatesh', 'nivas'],
                "age": ["21", "30", "38", '21', '45', '25', '25', '25', '26'],
                "height": ["170", "160", "159", '168', '159', '168', '176', '180', '160'],
                "skills": [ 
                    "NLP , Python , Ml", "Ml", "Python", "ML", "DL", "Ml", "Python", "ML", "DL"
                ]
            }
            col1, col2, col3 = st.columns([1, 7, 1])
            with col2:
                st.table(data)

            col2.markdown(
                "<h1 style='font-size: 40px;'><span style='color: white;'>Provide </span><span style='color:cyan;'>Question</span></h1>",
                unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 7, 1])
            
            with col2 :
                text = st.text_input('')
            with col2:
                    if st.button("Proceed"):

                        # Chain of Thought 
                        prompt = f"""
                        Table Provided :
                        {data}

                        Instruction :
                        1. You should act responsible table question and answering system.
                        2. Based on user provided question which is delimited with triple backticks.
                        3. Send answer within 10 words 

                        '''{text}'''
                        """
                        
                        response = response.get_completion(prompt=prompt)

                        col2.write("")
                        col2.write("")
                        col2.write("")

                        col2.markdown(
                        f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Completion :</span> <span style='color: white;'></span> </h1>",
                        unsafe_allow_html=True)

                        col2.markdown(
                        f"<h1 style='font-size: 30px;'><span style='color: white;'>{response}</span> <span style='color: white;'></span> </h1>",
                        unsafe_allow_html=True)           
# #_______________________________________________________________________________________________________________________________________
        elif selected == 'Question Answering System':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1.5, 7, 1])

            col2.markdown(
                "<h1 style='font-size: 67px;'><span style='color: cyan;'></span> <span style='color: cyan;'>Questioning </span><span style='color: white;'>Answering </span><span style='color: cyan;'> System</span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
         

            col1, col2, col3 = st.columns([1, 7, 1])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color: cyan;'>Provide </span> <span style='color: white;'>Content </span> </h1>",
                    unsafe_allow_html=True)
                content = st.text_area("")
                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color: cyan;'>Provide </span> <span style='color: white;'>Question</span> </h1>",
                    unsafe_allow_html=True)
                
                question = st.text_input("")
                if st.button("Proceed"):
                                        
                    prompt = f"""
                    Information: 
                    {content}

                    question : 
                    {question}

                    Instruction :
                    1. You should act responsible question and answering system.
                    2. Based on user provided information and  question which is enclosed with curly braces.
                    3. Answer should be given from provided information only.
                    4. Send answer within 20 words
                    """ 
                    response = response.get_completion(prompt=prompt)

                    col2.write("")
                    col2.write("")
                    col2.write("")

                    col2.markdown(
                    f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Answer :</span> <span style='color: cyan;'></span> </h1>",
                    unsafe_allow_html=True)

                    col2.markdown(
                    f"<h1 style='font-size: 30px;'><span style='color: white;'>{response}</span> <span style='color: white;'></span> </h1>",
                    unsafe_allow_html=True)   
        #______________________________________________________________________________________________________________________________________
        elif selected == 'Intro':

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            # Start Intro
            col1, col2 = st.columns([11, 8.5])
            with col1:
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")

                st.markdown(
                    "<h1 style='font-size: 59px;'><span style='color:white;'>Howdy ,</span> <span style='color: white;'>I'm </span><span style='color: cyan;'> Praveen</span> </h1>",
                    unsafe_allow_html=True)

                # keyboard_to_url(key="P", url="https://www.linkedin.com/in/praveen-n-2b4004223/")

            with col2:
                file = lottie("intro1.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=600,
                    key=None
                )

            st.write("")
            st.write('')
            st.write("")
            st.write("")
            with col1:
                file = lottie("sound.json")
                st_lottie(
                    file,
                    speed=1,
                    
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=240,
                    width=600,
                    key=None
                )

            col1,col2,col3 = st.columns([6.5,12,2])
            with col2:
               st.markdown(
                    "<h1 style='font-size: 30px;'><span style='color:white;'> I'm a </span> <span style='color: cyan;'> AI Application Innovator </span> <span style='color: white;'> From India </span></h1>",
                    unsafe_allow_html=True)

            col2.write("")
            col2.write("")
            col2.write("")
            st.write("")
            st.markdown(
                    "<h1 style='font-size: 65px;'><span style='color:white;'>About </span> <span style='color:cyan;'>Language AI </span></h1>",
                    unsafe_allow_html=True)


            col1, col2, col3 = st.columns([2, 10, 2])
            # col2.write("")
            # col2.write("")
            # col2.write("")
            with col2:
                file = lottie("lang_ai.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=650,
                    width=800,
                    key=None
                )

            st.markdown(
                "<h1 style='font-size: 80px;'><span style='color:white;'>Understanding </span> <span style='color:cyan;'>NLP </span></h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")

            col1, col2, col3 = st.columns([2, 15, 2])
            col2.write("")
            col2.write("")
            col2.markdown(
                "<h1 style='font-size: 60px;'><span style='color: white;'>Process of Training</span> <span style='color: cyan;'>Language Models:</span><span style='color: white;'></span> </h1>",
                unsafe_allow_html=True)
            col1, col2, col3 = st.columns([5, 15, 2])

            with col2:
                file = lottie("model_training.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=600,
                    width=800,
                    key=None
                )
            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 70;'><span style='color: cyan;'>Initialization </span><span style='color: white;'>(Birth)</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("parameter'.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=600,
                    key=None
                )
            with col1:
                file = lottie("baby.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=600,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 25px;'><span style='color: cyan;'>( </span><span style='color: white;'>Baby is born with a brain ready to learn</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 25px;'><span style='color: cyan;'>( </span><span style='color: white;'>Model is initialized with random parameters</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.write('')
            st.write("")
            # ________________________________________________________________________________________________________________________

            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 60px;'><span style='color: cyan;'>Exposure to </span><span style='color: white;'> Language</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("ml_learn.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=600,
                    key=None
                )
            with col1:
                file = lottie("baby_1.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=600,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 20px;'><span style='color: cyan;'>( </span><span style='color: white;'>Listening to caregivers and observing their surroundings</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 20px;'><span style='color: cyan;'>( </span><span style='color: white;'>Exposed to vast amounts of text data in   multiple languages</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)

            # ___________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write('')
            st.write("")

            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 60px;'><span style='color: cyan;'>Learning </span><span style='color: white;'> Patterns</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("ml_pattern.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=600,
                    key=None
                )
            with col1:
                file = lottie("babypattern.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=600,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 20px;'><span style='color: cyan;'>( </span><span style='color: white;'>Learns grammar and vocabulary through interaction</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 20px;'><span style='color: cyan;'>( </span><span style='color: white;'>Language patterns and  semantics from the data it processes</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            # ________________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write('')
            st.write("")

            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 60px;'><span style='color: cyan;'>Feedback </span><span style='color: white;'> Correction</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("ml_learn_2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=600,
                    key=None
                )
            with col1:
                file = lottie("baby_cry_2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=600,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 15px;'><span style='color: cyan;'>( </span><span style='color: white;'>Feedback from caregivers, corrects mistakes, and refines language skills over time</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 16px;'><span style='color: cyan;'>( </span><span style='color: white;'>Correcting errors, and improving translation accuracy based on training data</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            # ________________________________________________________________________________________________________________________

            st.write("")
            st.write("")
            st.write('')
            st.write("")

            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 60px;'><span style='color: cyan;'>Practice and </span> <span style='color: white;'> Improvement</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("ml_practice.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=600,
                    key=None
                )
            with col1:
                file = lottie("baby_last.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=500,
                    width=600,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 17.5px;'><span style='color: cyan;'>( </span><span style='color: white;'>Continually practices speaking and listening to improve language skills</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 19px;'><span style='color: cyan;'>( </span><span style='color: white;'>Continuously fine-tunes and updates the model with more data</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col1, col2, col3, = st.columns([5,10,5])

            col2.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'> </span> </h1>",
                unsafe_allow_html=True)

        


            colored_header(
                label="",
                description="",
                color_name="blue-green-70"
            )
# #____________________________________________________________________________________________________________________________________
        elif selected == 'Feedback':
            praveen_1 = pm.MongoClient(
                'mongodb://praveen:praveenroot@ac-cd7ptzz-shard-00-00.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-01.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-02.lsdge0t.mongodb.net:27017/?ssl=true&replicaSet=atlas-ac7cyd-shard-0&authSource=admin&retryWrites=true&w=majority')
            db = praveen_1['Feedback_prompt_ai']
            collection = db['comment']

            st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3, = st.columns([3, 8, 3])

            with col2:
                selected_1 = option_menu(
                    menu_title="OPINION BOX",
                    options=['CHOOSE OPTION', 'Your Feedback', "Explore User Thoughts"],
                    icons=['arrow-down-circle-fill', 'envelope-plus-fill', 'people-fill'],
                    default_index=0)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            if selected_1 == 'CHOOSE OPTION':
                # animation

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3, col4 = st.columns([15, 15, 15, 15])
                with col2:
                    file = lottie("angry_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col1:
                    file = lottie("smile_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col3:
                    file = lottie("calm_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col4:
                    file = lottie("love_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )


            elif selected_1 == 'Your Feedback':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])
                col2.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:white;'>Your</span> <span style='color:cyan;'>Feedback</span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                # animation

                st.write("")

                st.write("")

                st.write("")
                col1, col2, col3 = st.columns([15, 30, 5])
                with col2:
                    file = lottie("star_before_fb.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=600,
                        key=None
                    )

                col1, col2, col3, = st.columns([3, 8, 3])

                with col2:
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:white;'>Enter</span> <span style='color:cyan;'>Comment</span> <span style='color: white;'>Here ⬇️</span> </h1>",
                        unsafe_allow_html=True)
                    Comment = st.text_input('   ')
                    st.write(Comment)
                    if st.button('Save Comment'):
                        collection.insert_one({'comment of user': Comment})
                        st.write("")
                        st.write("")
                        senti = TextBlob(Comment)
                        value = senti.polarity
                        if value>=0.5:
                            review = "Positive Review"
                        elif value <0.0:
                            review = 'Negative Review'
                        else:
                            review = 'Neutral Review'



                        col1, col2, col3, = st.columns([5, 8, 5])
                        col2.markdown(
                        f"<h1 style='font-size: 40px;'><span style='color:cyan;'>{review}</span>  </h1>",
                        unsafe_allow_html=True)
                        col1, col2, col3, = st.columns([5, 8, 5])
 
                        st.success('Your Valuable Comment Saved Thankyou!', icon="✅")
                        col1, col2, col3 = st.columns([10, 30, 10])
                        
                        with col2:
                            file = lottie("star.json")
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                # renderer='svg',
                                height=100,
                                width=500,
                                key=None
                            )
                        
                    

                col1, col2, col3, = st.columns([3, 8, 3])
                with col2:
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )


            elif selected_1 == 'Explore User Thoughts':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])

                with col2:

                    file = lottie("down_arrow.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=800,
                        key=None
                    )
                col2.markdown(
                    "<h1 style='font-size: 70px;'><span style='color:white;'>Explore</span> <span style='color:cyan;'>User Thoughts </span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                col2.write("")
                col2.write("")

                with col2:

                    file = lottie("thoughts.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=800,
                        key=None
                    )
                st.write("")
                st.write("")
                st.write("")
                col1, col2, col3, = st.columns([3.6, 10, 3])
                with col2:
                    res = [i['comment of user'] for i in collection.find()]
                    st.write("")
                    with st.spinner('Wait for it...'):
                        time.sleep(5)

                    colored_header(
                        label="Comments By Users ⬇",
                        description="",
                        color_name="blue-green-70", )
                    for i in res:
                        print(st.code(i))

                    col1, col2, col3 = st.columns([1, 10, 1])
                    col2.write("")
                    col2.write('')
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:cyan;'>Press</span> <span style='color:white;'>'G'</span> <span style='color:cyan;'>On Keyboard To Explore More Project</span> </h1>",
                        unsafe_allow_html=True)
                    with col2:
                        keyboard_to_url(key="G", url="https://github.com/praveendecode")

                    def lottie(filepath):
                        with open(filepath, 'r') as file:  # 'G' On Keyboard To Explore More Project
                            return js.load(file)

                    with col2:
                        file = lottie("click2.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=100,
                            width=200,
                        )

                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )  
#_________________________________________________________________________________________________________________________________________________

# Obj ect Creation
object = language_ai()
object.method()
