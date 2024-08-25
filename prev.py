import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from browsing_functionalities import *
from API_functionalities import *
from gmail import *


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as data_taker:
        print("Say Something")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        if 'max' in instruct:
            instruct = instruct.replace('max', '')
            print(instruct)
        return instruct

def run_Max():
    instruct = take_command()
    if 'play' in instruct:
        song = instruct.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

         
    elif 'time' in instruct:
        time = datetime.datetime.now().strftime('%I:%M')
        print(time)
        talk('current time is ' + time)
    elif 'who are you' in instruct:
        talk('I am your personal Assistant V')
    elif 'what can you do for me' in instruct:
        talk('I can play songs, tell time, and help you with Wikipedia')
    elif 'open youtube' in instruct:
             webbrowser.open("youtube.com")
    elif 'open whatsapp' in instruct:
             webbrowser.open("web.whatsapp.com")
    elif 'open google' in instruct:
             webbrowser.open("google.com")
    elif 'previous year question' in instruct:
         webbrowser.open("muquestionpapers.com")
        
    elif 'result' in instruct:
         webbrowser.open("mumresults.in")
    elif 'thank you' in instruct:
         talk("You're Welcome!")
    #elif '' in instruct:
    elif 'search' in instruct:
        googleSearch(instruct)
        return
    elif 'distance' in instruct:
        get_map(instruct)
        return
    
    elif 'joke' in instruct:
       joke = get_joke()
       if joke:
         talk(joke)
         done = True
    elif 'news' in instruct:
         news = get_news()
         if news:
            talk(news)
            done = True
    elif 'ip' in instruct:
         ip = get_ip()
         if ip:
              talk(ip)
              done = True
    elif 'internet' in instruct:
        talk("Getting your internet speed, this may take some time")
        speed = get_speedtest()
        if speed:
            talk(speed)
            done = True
    elif 'website' in instruct:
        completed = open_specified_website(instruct)
        if completed:
           done = True




    else:
        talk('I did not understand, can you repeat again')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  


while True: 
    run_Max()