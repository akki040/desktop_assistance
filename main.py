import speech_recognition as sr
import pyttsx3
import os
import pywhatkit
import wikipedia
import webbrowser
import datetime
import requests
import dictpath
import pyautogui
import random
from config import apikey
import numpy as np

# password protection

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
         exit()
        
    elif (a!=pw):
        print("Try Again")



def say(text):
    engine=pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.say(text)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        say("Good Morning,sir")
    elif hour >12 and hour<=18:
        say("Good Afternoon ,sir")

    else:
        say("Good Evening,sir")

    say("Please tell me, How can I help you ?")

#take voiceinput from user

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio, language="en-in")
            print(f"user said :{query} ")
            return query
        except Exception as e:
            return "facing some error"
        
#search function to call google

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        say("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            say(result)

        except:
            say("No speakable output available")

#search function to call yt

def searchYoutube(query):
    if "youtube" in query:
        say("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        say("Done, Sir")

#search function to call wikipedia

def searchWikipedia(query):
    if "wikipedia" in query:
        say("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        say("According to wikipedia..")
        print(results)
        say(results)

# alarm

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

    
if __name__ == '__main__':
    print('pycharm')
    say("Hey, I'm Akki. Listening...")
    
    while True:
        print("Listening...")
        query = takecommand().lower()
        
        if "wake up" in query:
            greetMe()
        elif "go to sleep" in query:
            say("Ok sir, You can call me anytime")
            break

        ##########################################################

        #password by saying
        elif "change password" in query:
            say("What's the new password")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            say("Done sir")
            say(f"Your new password is{new_pw}")


        ##########################################################

        elif "exit" in query or "quit" in query:
            say("Goodbye, sir. Have a great day!")
            break
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            say(f"Sir, the time is {strTime}")


        # Searching from web

        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)

        # Open and Close apps/websites : Open and close apps like word, paint and various websites.

        elif "open" in query:  #errork
            from Dictpath import openappweb
            openappweb(query)
        elif "close" in query:
            from Dictpath import closeappweb
            closeappweb(query)


        # set a alarm

        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            say("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            say("Done,sir")

       
        # Youtube Controls like Play, Pause , Mute , Volume up and down 

        elif "pause" in query:
            pyautogui.press("k")
            say("video paused")
        elif "play" in query:  # Removed stray character 'e'
            pyautogui.press("k")
            say("video played")
        elif "mute" in query:
            pyautogui.press("m")
            say("video muted")
        elif "volume up" in query:          #error
            from keyboard import volumeup
            say("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:         #error
            from keyboard import volumedown
            say("Turning volume down, sir")
            volumedown()

        # 11 reminder

        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("jarvis","")
            say("You told me to remember that"+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            say("You told me to remember that" + remember.read())

        #12 PLAYLIST (Personalized Playlist)

        elif "play a  song" in query:
            say("Playing your favourite songs, sir")
            a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
            b = random.choice(a)
            if b==1:
                    webbrowser.open("Here put the link of your video")

        

        #15 whatsapp
        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()

        #16 shutdownsystem
        elif "shutdown the system" in query:
            say("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
        
            elif shutdown == "no":
                break

         #news selctionk
        elif "news" in query:
            from NewsRead import latestnews
            latestnews()

        #calculate
        elif "calculate" in query:

            from Calculatenumbers import WolfRamAlpha
            from Calculatenumbers import Calc
            query = query.replace("calculate","")
            query = query.replace("jarvis","")
            Calc(query)

        elif " hey ai" in query:
            from genai import chat_session
            say("Hello, how can I assist you today?")
            while True:
                user_query = takecommand()
                if user_query.lower() in ["exit", "quit"]:
                    say("Goodbye!")
                    break
                response = chat_session.send_message(user_query)
                say(response.text)
                
        elif  "using ai" in query:
            from genai import chat_session
            say("Hello, how can I assist you today?")
            while True:
                user_query = takecommand()
                if user_query.lower() in ["exit", "quit"]:
                    say("Goodbye!")
                    break
                response = chat_session.send_message(user_query)
                say(response.text)



        #finally sleep
        elif "finally sleep" in query:
            say("Going to sleep,sir")
            exit()

        else:
            print("chating........")
            # chat(prompt=query)
            print("NO INPUT FOUND")
            # chat(query)
            # # Add function calls here
            # searchGoogle(query)
            # searchYoutube(query)
            # searchWikipedia(query)
