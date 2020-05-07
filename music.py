import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import sys
today = str(datetime.datetime.now().strftime("%d-%m"))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0]).id
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Opened music player.")
    music_dir= 'D:\\MUSIC\\Favourites'
    songs = os.listdir(music_dir)
    print(songs)
    speak("Which song do you want to play?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        print(e)    
        print("Didn't found the song")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()        
        
        #Music Player
        if 'attention' in query:
            os.startfile("D:\\MUSIC\\Favourites\\Attention.mp3")   
        elif 'give me some sunshine' in query:
            os.startfile("D:\\MUSIC\\Favourites\\Give me some sunshine.mp3")
        elif 'let me love you' in query:
            os.startfile("D:\\MUSIC\\Favourites\\Let Me Love You.mp3")
        elif 'perfect' in query:
            os.startfile("D:\\MUSIC\\Favourites\\Perfect.mp3")
        elif 'see you again' in query:
            os.startfile("D:\\MUSIC\\Favourites\\See You Again.mp3")
        elif 'minimise' in query:
            os.startfile("F:\\JARVIS\\jarvis-home.py")
            sys.exit()
        elif 'stop playing' in query:
            os.system('TASKKILL /F /IM vlc.exe')
            os.startfile("F:\\JARVIS\\jarvis-home.py")
            sys.exit()
        elif 'exit' in query:
            sys.exit()
        