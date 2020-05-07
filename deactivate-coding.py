import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import re
import smtplib
import sys
today = str(datetime.datetime.now().strftime("%d-%m"))
#wishTime = datetime.datetime.now().strftime("%I:%M:%S")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0]).id
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Deactivating coding environment, sir")
os.system('TASKKILL /F /IM sublime_text.exe')
os.system('TASKKILL /F /IM chrome.exe')
os.system('TASKKILL /F /IM xampp-control.exe')
speak("Deactivated coding environment successfully, sir")
os.startfile("F:\\JARVIS\\jarvis-home.py")
sys.exit()