#author@: Sam-r-ai
#date: 1/13/2024
#version: 1.1
#purpose: turn Raspbery Pi into a voice assistant using OpenAI API

#INSTALLS
#pip install --upgrade python-dotenv
#pip install --upgrade setuptools
#pip install --upgrade pip
#pip install openai
#pip install speechrecognition
#pip install pyaudio
#pip install pyttsx3

#STEP 1: SETUP API KEY
import openai
from openai import OpenAI
import speech_recognition as sr

import pyttsx3
engine = pyttsx3.init()
import random


#USING STREAMING STANDARD of openai API
client = OpenAI(api_key="YOUR API-KEY HERE") #client object created
#set speech rate
new_rate = 180
engine.setProperty('rate', new_rate)
'''
rate = engine.getProperty('rate') 
print(f"Current speech rate: {rate}")
voices = engine.getProperty('voices')

# List all voices and select one that sounds more fluent to you
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name}")

#Set engine voice to the one you want to use based on the index from the list
engine.setProperty('voice', voices[0].id)  # Change the index to the voice you prefer

'''
recognizer = sr.Recognizer()
microphone = sr.Microphone()

#STEP 3: SETUP FUNCTIONS FOR VOICE INPUT AND OUTPUT

def get_response_from_gpt(prompt):
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content + " "
        else:
            print("API closed the connection due to inactivity")
            break
    engine.say(response)
    engine.runAndWait()

#function that uses microphone to get user input from voice 
delay = 10
def get_user_question(recognizer, microphone):
    with microphone as source:
        print("Listening for question:")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise for better accuracy
        try:
            # Listens for the user's input for up to 'delay' seconds
            audio = recognizer.listen(source, timeout=delay)
            text = recognizer.recognize_google(audio)
            print("You said: {}".format(text))
            return text
        except sr.WaitTimeoutError:
            # Timeout occurs if no speech is detected in 'delay' seconds
            print("No voice input detected.")
            return None
        except sr.UnknownValueError:
            # Speech was detected but could not be understood
            print("Sorry, could not recognize what you said")
            return None
        except Exception as e:
            # Other exceptions
            print(f"An error occurred: {e}")
            return None

#function that uses microphone and listens for wakeword and returns true if wakeword is detected
wakeword = "james"
def listen_for_wakeword(recognizer, microphone):
    with microphone as source:
        print("Listening for ",wakeword,": ")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            if wakeword in text.lower():
                return True
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio in wakeword")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return False

#function that continuously gets user input from microphone and sends it to the API
def main():
    while True:
        if listen_for_wakeword(recognizer, microphone):
            print("wakeword detected")
            #an array of responses to wakeword
            acknowledge = ["yes?", "I'm listening", "how can i help you?"]
            #choose a random response from the array
            response = random.choice(acknowledge)
            engine.say(response)
            engine.runAndWait()
            #get_user_question has a delay of X seconds
            user_input = get_user_question(recognizer, microphone)
            if user_input is not None:
                #loops until user_input is None
                while user_input is not None:
                    #send user_input to API
                    get_response_from_gpt(user_input)
                    #get user_input again
                    user_input = get_user_question(recognizer, microphone)
                    #if user_input is None, break out of loop
                    if user_input is None:
                        break
                #get_response_from_gpt(user_input)
main()

