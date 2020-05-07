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

def wishMe():
    print("Made by TAHSIN AHMED TUSHAR. ALL RIGHTS RESERVED")
    print(f"How may I help you, sir?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Command: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        #EXIT    
        elif 'exit' in query:
            speak("Ok sir. I am going offline.")
            sys.exit()
        

        #Mail
        elif 'send a mail' in query:
            speak("Getting ready to send mail")
            smail = "F:\\JARVIS\\sendmail.py"
            os.startfile(smail)
            sys.exit()

        #Local server        
        elif 'open router control panel' in query:
            webbrowser.open("http://192.168.16.1/")

        elif 'open localhost' in query:
            speak('Opening Localhost, sir.')
            webbrowser.open("http://localhost/")
        
        elif 'open database' in query:
            speak('Opening Localhost, sir.')
            webbrowser.open("http://localhost/phpmyadmin")

        elif 'local server' in query:
            speak("Opening local server....")
            xampp = "F:\\XAMPP\\xampp-control.exe"
            os.startfile(xampp)
        elif 'turn off local server' in query:
            os.system('TASKKILL /F /IM xampp-control.exe')
            speak("Closed firefox browser successfullly, sir.") 

        #browsers
        elif 'open chrome' in query:
            speak("Opening chrome browser, sir.")
            chromeloc = "C:\\Users\\Elias\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe"
            os.startfile(chromeloc)
        elif 'close chrome' in query:
            os.system('TASKKILL /F /IM chrome.exe')
            speak("Closed chrome browser successfullly, sir.")

        elif 'open firefox' in query:
            speak("Opening firefox browser, sir")
            firefoxloc = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefoxloc)
        elif 'close firefox' in query:
            os.system('TASKKILL /F /IM firefox.exe')
            speak("Closed firefox browser successfullly, sir.")

        #sites
        elif 'open stackoverflow' in query:
            speak('Opening Stackoverflow, sir.')
            webbrowser.open("https://stackoverflow.com")
        elif 'my website' in query:
            speak('Opening your website, sir')
            webbrowser.open('https://tahsintushar.blogspot.com/')
        elif 'open whatsapp' in query:
            speak('Opening WhatsApp, sir')
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open business software' in query:
            speak('Opening business software, sir')
            webbrowser.open('https://hisab.tusharelectronics.com/')
        elif 'coronavirus' in query:
            speak('Showing coronavirus stastics, sir')
            webbrowser.open('https://www.worldometers.info/coronavirus/country/bangladesh/')
        
        #google
        elif 'open google' in query:
            speak('Opening Google, sir.')
            webbrowser.open("https://google.com")
        
        elif 'open gmail' in query:
            speak('Opening Gmail, sir.')
            webbrowser.open("https://mail.google.com")
        elif 'open mailbox' in query:
            speak('Opening mailbox, sir.')
            webbrowser.open("https://mail.google.com/mail/u/2/#inbox")

        elif 'in google' in query:
                stopwords = ['find','in','google','search','this']
                querywords = query.split()

                resultwords  = [word for word in querywords if word.lower() not in stopwords]
                result = ' '.join(resultwords)

                def my_gsearch(gsearch):
                    speak("Searching in Google, sir.")
                    webbrowser.open("https://google.com/search?q=" + gsearch)
                my_gsearch(result)

        elif 'on google' in query:
                stopwords = ['find','on','google','search','this']
                querywords = query.split()

                resultwords  = [word for word in querywords if word.lower() not in stopwords]
                result = ' '.join(resultwords)

                def my_gsearch(gsearch):
                    speak("Searching in Google, sir.")
                    webbrowser.open("https://google.com/search?q=" + gsearch)
                my_gsearch(result)

        elif 'find my mobile' in query:
            speak('Finding your mobile, sir.')
            webbrowser.open("https://www.google.com/android/find?hl=en-BD&u=0")
        
        elif 'open translator' in query:
            speak("Opening google translator, sir")
            webbrowser.open("https://translate.google.com/")

        #YouTube
        elif 'open youtube' in query:
            speak('Opening YouTube, sir.')
            webbrowser.open("https://youtube.com")
        elif 'my youtube channel' in query:
            speak('Opening your YouTube channel, sir.')
            webbrowser.open("https://www.youtube.com/channel/UCgNa8Y_ucsbb6Iqgbh4-l9Q")

        elif 'in youtube' in query:
                stopwordsyt = ['find','in','youtube','search','this']
                querywordsyt = query.split()

                resultwordsyt  = [word for word in querywordsyt if word.lower() not in stopwordsyt]
                resultyt = ' '.join(resultwordsyt)

                def my_ytsearch(ytsearch):
                    speak("Searching in YouTube, sir.")
                    webbrowser.open("https://www.youtube.com/results?search_query=" + ytsearch)
                my_ytsearch(resultyt)
        elif 'on youtube' in query:
                stopwordsyt = ['find','on','youtube','search','this']
                querywordsyt = query.split()

                resultwordsyt  = [word for word in querywordsyt if word.lower() not in stopwordsyt]
                resultyt = ' '.join(resultwordsyt)

                def my_ytsearch(ytsearch):
                    speak("Searching in YouTube, sir.")
                    webbrowser.open("https://www.youtube.com/results?search_query=" + ytsearch)
                my_ytsearch(resultyt)

        #Facebook
        elif 'open facebook' in query:
            speak('Opening Facebook, sir.')
            webbrowser.open("https://facebook.com")
        elif 'my facebook profile' in query:
            speak('Opening your Facebook profile, sir.')
            webbrowser.open("https://facebook.com/tushariar")
        elif 'my facebook page' in query:
            speak('Opening your Facebook page, sir.')
            webbrowser.open("https://facebook.com/hi.tahsintushar")
        elif 'open messenger' in query:
            speak('Opening Messenger, sir.')
            webbrowser.open("https://messenger.com")
        elif 'in facebook' in query:
                stopwordsfb = ['find','in','facebook','search']
                querywordsfb = query.split()

                resultwordsfb  = [word for word in querywordsfb if word.lower() not in stopwordsfb]
                resultfb = ' '.join(resultwordsfb)

                def my_fbsearch(fbsearch):
                    speak("Searching in Facebook, sir.")
                    webbrowser.open("https://www.facebook.com/search/top/?q=" + fbsearch)
                my_fbsearch(resultfb)
        elif 'on facebook' in query:
                stopwordsfb = ['find','on','facebook','search']
                querywordsfb = query.split()

                resultwordsfb  = [word for word in querywordsfb if word.lower() not in stopwordsfb]
                resultfb = ' '.join(resultwordsfb)

                def my_fbsearch(fbsearch):
                    speak("Searching in Facebook, sir.")
                    webbrowser.open("https://www.facebook.com/search/top/?q=" + fbsearch)
                my_fbsearch(resultfb)
        elif 'video on facebook' in query:
                stopwordsfbw = ['find','in','facebook','search','of','video','videos','watch','on']
                querywordsfbw = query.split()

                resultwordsfbw  = [word for word in querywordsfbw if word.lower() not in stopwordsfbw]
                resultfbw = ' '.join(resultwordsfbw)

                def my_fbsearchw(fbsearchw):
                    speak("Searching in Facebook, sir.")
                    webbrowser.open("https://www.facebook.com/watch/search/?q=" + fbsearchw)
                my_fbsearchw(resultfbw)
        elif 'video in facebook' in query:
                stopwordsfbw = ['find','in','facebook','search','of','video','videos','watch','on']
                querywordsfbw = query.split()

                resultwordsfbw  = [word for word in querywordsfbw if word.lower() not in stopwordsfbw]
                resultfbw = ' '.join(resultwordsfbw)

                def my_fbsearchw(fbsearchw):
                    speak("Searching in Facebook, sir.")
                    webbrowser.open("https://www.facebook.com/watch/search/?q=" + fbsearchw)
                my_fbsearchw(resultfbw)

        
        #Softwares
        elif 'open sublime text' in query:
            speak("Opening Sublime Text 3, sir....")
            sublime_dir = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublime_dir)
        elif 'close sublime text' in query:
            os.system('TASKKILL /F /IM sublime_text.exe')
            speak("Closed sublime text 3 successfullly, sir.")

        elif 'open visual studio' in query:
            speak("Opening Visual studio code, sir....")
            vs_dir = "F:\\VS\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_dir)
        elif 'close visual studio' in query:
            os.system('TASKKILL /F /IM code.exe')
            speak("Closed visual studio successfullly, sir.")
        elif 'open calculator' in query:
            speak("Opening calculator, sir")
            os.startfile("calc.exe")
        elif 'close calculator' in query:
            os.system("TASKKILL /F /IM calc.exe")   
        #Pirate-bay
        elif 'open pirate bay' in query:
            speak("Opening the pirate bay, sir.")
            webbrowser.open("https://thepirate-bay.org/")
        elif 'in the pirate bay' in query:
                stopwordspb = ['find','in','pirate','search','this','bay','the']
                querywordspb = query.split()

                resultwordspb  = [word for word in querywordspb if word.lower() not in stopwordspb]
                resultpb = ' '.join(resultwordspb)

                def my_pbsearch(pbsearch):
                    speak("Searching in the Pirate bay, sir.")
                    webbrowser.open("https://www.pirate-bay.net/search?q=" + pbsearch)
                my_pbsearch(resultpb)
        
        #W3 School
        elif 'open w3school' in query:
            speak('Opening W3 School, sir.')
            webbrowser.open("https://w3schools.com")
        elif 'open php tutorials' in query:
            speak('Opening php tutorials W3 School, sir.')
            webbrowser.open("https://www.w3schools.com/php/default.asp")
        elif 'open html tutorials' in query:
            speak('Opening html tutorials in W3 School, sir.')
            webbrowser.open("https://www.w3schools.com/html/default.asp")
        elif 'open python tutorials' in query:
            speak('Opening Python tutorials in W3 School, sir.')
            webbrowser.open("https://www.w3schools.com/python/default.asp")

        #faq
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        elif 'thank you' in query:
            speak("It's my pleasure")
        elif 'are you listening' in query:
            speak('Yeah! I am listening')

        #ENVIRONMENT-CODING:
        elif 'deactivate coding' in query:
            os.startfile("F:\\JARVIS\\deactivate-coding.py")

        elif 'activate coding' in query:
            os.startfile("F:\\JARVIS\\activate-coding.py")
        #Entertainment
        elif 'music player' in query:
            os.startfile("F:\\JARVIS\\music.py")
            sys.exit()
            
        #about
        elif 'about you' in query:
            #don't remove this credit.
            speak("I am JARVIS. Tahsin Ahmed Tushar has developed me after being inspired by watching IRON MAN movie.")
            print("I am JARVIS. Tahsin Ahmed Tushar has developed me after being inspired by watching IRON MAN movie")   