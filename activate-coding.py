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

speak("Activating coding environment, sir")
xampp = "F:\\XAMPP\\xampp-control.exe"
os.startfile(xampp)
sublime_dir = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
os.startfile(sublime_dir)
webbrowser.open("http://localhost/phpmyadmin")
webbrowser.open("https://stackoverflow.com")
webbrowser.open("https://w3schools.com")
#you can add more websites
speak("Activated coding environment successfully, sir")
os.startfile("F:\\JARVIS\\jarvis-home.py")
sys.exit()