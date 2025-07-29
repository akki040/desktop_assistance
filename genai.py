"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Set the environment variable correctly
os.environ["GOOGLE_API_KEY"] = "api-key"

# Use the correct key to configure the API
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

# Function to convert text to speech
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

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
        

# Get user input for the chat message via speech
user_query = takecommand()

if user_query:
    response = chat_session.send_message(user_query)  # Use the user input here
    say(response.text)  # Output the response as speech