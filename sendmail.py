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
    
    print("I am ready to send email, sir. Are you ready?")
    speak("I am ready to send email, sir. Are you ready?")


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

def sendEmail(to, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    #message = f'Subject: {subject} \n \n {content}'
    server.sendmail('youremail@gmail.com', to, message)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        
        
        #Mail
        if 'yes' in query:
            try:
                print("Whom do you want to send the mail, sir?")
                speak("Whom do you want to send the mail, sir?")
                maillist = {
                            "Contact Name1":"contactemail1@gmail.com","contact Name1":"contactemail1@gmail.com",
                            "Contact Name2":"contactemail2@gmail.com","contact Name2":"contactemail2@gmail.com"
                            #Look that I've written the same contact name and address twice
                            #because sometimes it can get the Capital letter or sometimes small one
                            }
                to = (maillist[takeCommand()])
                #print (to)
                print("What will be the subject, sir?")
                speak("What will be the subject, sir?")
                subject = takeCommand()
                print(subject)
                speak("What do you want to mail, sir?")
                content = takeCommand()
                print(content)
                message = f'Subject: {subject}\n\n{content}'
                sendEmail(to, message)
                webbrowser.open("https://mail.google.com/mail/u/2/#sent")
                speak("Your email has been sent, successfully, sir!")
                speak("Do you want to send another mail?")   
            except Exception as e:
                print(e)
                speak("Sorry Tushar sir. I couldn't send the mail. Will I try again?")
        elif 'no' in query:
            os.startfile("F:\\JARVIS\\jarvis-home.py")
            sys.exit()
        elif 'exit' in query:
            os.startfile("F:\\JARVIS\\jarvis-home.py")
            sys.exit()