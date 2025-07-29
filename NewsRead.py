import requests
import json
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  #cd4e2d43ab1b483387ac25d0983ec9c8


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
        

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cd4e2d43ab1b483387ac25d0983ec9c8",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cd4e2d43ab1b483387ac25d0983ec9c8",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cd4e2d43ab1b483387ac25d0983ec9c8",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cd4e2d43ab1b483387ac25d0983ec9c8",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cd4e2d43ab1b483387ac25d0983ec9c8",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cd4e2d43ab1b483387ac25d0983ec9c8"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    print("listening.....")
    field = takecommand().lower()
    # field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        

        process=takecommand().lower()
        # a = input("[press 1 to cont] and [press 2 to stop]")
        if str(process) == "continue":
            pass
        elif str(process) == "stop":
            break
        
    speak("thats all")
