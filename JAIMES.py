#author@: Justin Cheung
#date: 1/11/2024
#version: 0.2
#purpose: testing the openAI API

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

#USING STREAMING STANDARD of openai API
client = OpenAI(api_key="YOUR API KEY HERE") #client object created
#i need an engine object to use text to speech
import pyttsx3
engine = pyttsx3.init()

new_rate = 180
engine.setProperty('rate', new_rate)
rate = engine.getProperty('rate') 
print(f"Current speech rate: {rate}")
voices = engine.getProperty('voices')

# List all voices and select one that sounds more fluent to you
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name}")

# Set engine voice to the one you want to use based on the index from the list
engine.setProperty('voice', voices[0].id)  # Change the index to the voice you prefer

#function that sends response to openai API
def send(prompt):
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            #print(chunk.choices[0].delta.content, end="")
            response += chunk.choices[0].delta.content + " "
        else:
            print("API closed the connection due to inactivity")
            break
                #turns response into voice output
    engine.say(response)
    engine.runAndWait()


#function that uses microphone to get user input from voice
def get_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            return text
        except:
            print("Sorry could not recognize what you said")
            return None

#function that continuously gets user input from microphone and sends it to the API
def main():
    while True:
        user_input = get_user_input()
        if user_input is not None:
            send(user_input)
main()



