import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
import ssl
import certifi
import time
import os  # to remove created audio files
from PIL import Image
import subprocess
import pyautogui  # screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import requests
# import the library / Import des librairies
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
# initialize the gpio module / initialise le GPIO
# gpio.init()
# setup the port (same as raspberry pi's gpio.setup() function)
# Configure la broche PG7 (equivalent au GPIO21 du Raspberry) comme une sortie
#gpio.setcfg(port.PG7, gpio.OUTPUT)


class Person:
    name = 'Patch'

    def setName(self, name):
        self.name = name


person_obj = Person()
r = sr.Recognizer()


def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source)
        print('Done Listening')
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('Sorry, I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, my speech service is down')
        print(person_obj.name + " : ", voice_data.lower())
        return voice_data.lower()


def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)  # print what app said
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        engine_speak('my name is Myroth')
    if 'what time is it' in voice_data:
        engine_speak(ctime())
    if 'thank you' in voice_data:
        engine_speak('your welcome.')
        exit()
    if 'open door' in voice_data:
        engine_speak('open door')


time.sleep(1)
engine_speak('How can I help you?')
while True:
    voice_data = record_audio()
    respond(voice_data)
