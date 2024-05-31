import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import smtplib
import bs4
import requests
import subprocess
from pyautogui import *
from colorama import Fore, Back, Style
import ytmusic as yt
import pywhatkit as pwa


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 220)
engine.setProperty('volume', 1)
engine.setProperty('voice', voices[1].id)

# for voice in voices:
#     # to get the info. about various voices in our PC 
#     print("Voice:")
#     print("ID: %s" %voice.id)
#     print("Name: %s" %voice.name)
#     print("Age: %s" %voice.age)
#     print("Gender: %s" %voice.gender)
#     print("Languages Known: %s" %voice.languages)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    # speak("Hi Sir! How may I help you ?")


def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.CYAN + "Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(Fore.GREEN + "Recognizing...")    
        query = r.recognize_google(audio, language='en-In')
        print(Fore.YELLOW + f"User said: {query}\n")

    except Exception as e:
            
        print("I am sorry i couldn't get that...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open chrome' in query:
            chrome_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_dir)
            
        elif 'open vlc' in query:
            vlc_dir = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlc_dir)

        elif 'open gmail' in query:
            webbrowser.open("accounts.google.com")

        elif 'open discord' in query:
            webbrowser.open("discord.com")

        elif 'open shit ' in query:
            webbrowser.open("artisticshit.home.blog")  
            
        elif 'internet' in query:
            click(1745,1060)
            moveTo(1522,440,1)
            click()


        # elif 'play music' in query:
        #     music_dir = "C:\\Users\\manch\\Music\\iTunes\\iTunes Media\\Music\\SS Thaman\\Ala Vaikunthapurramuloo (Original Motion" #Change the directory according to your song file location
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))
            
            
        elif 'open project' in query:
            project_dir = "C:\\Users\\manch\\OneDrive\\Desktop\\Assistant" #Change the directory according to your song file location  
            os.startfile(project_dir)

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            #Enter the code directory of this file according to your system

            codePath = "C:\\Users\\manch\\OneDrive\\Desktop\\Assistant\\KKbot.py"
            os.startfile(codePath)
            
        
        elif 'open files' in query:
            #Enter the code directory of this file according to your system

            files_dir = "C:\\Windows\\explorer.exe"
            os.startfile(files_dir)
            
        elif 'weather now in ' in query:
            print('Searching Google...')
            speak('Searching Google...')
            query = query.replace("weather now in ", "")
            url = "https://google.com/search?q=weather+in+" + query
            request_result = requests.get(url)
            soup = bs4.BeautifulSoup( request_result.text , "html.parser" )
            temp = soup.find( "div" , class_='BNeawe' ).text
            print("According to Google")
            speak("According to Google")
            result = "The Weather in " + query + " is around " + temp
            print(result)
            speak(result)
            
        elif 'download video' in query:
            path = 'C:\\Users\\manch\\Videos\\kkbot\\Downloads'
            speak("Please enter video url") 
            #link of the video to be downloaded 
            link = input("Enter URL >> ")
            speak("Please wait")
            os.system('yt-dlp -o  '+ path + ' ' + link)
            speak("Task Completed")
            print("Task Completed!")
            speak("Thanks For using my downloder")
            speak("Opening downloaded directory")
            os.startfile('C:\\Users\\manch\\Videos\\kkbot')
        
        elif 'message' and 'bro' in query:
            query = query.replace("message", "")
            speak("sending message " + query)
            print("sending message " + query)
            pwa.sendwhatmsg_instantly("+917603966646",query)
            
        elif 'message' and 'donkey' in query:
            query = query.replace("message", "")
            speak("sending message " + query)
            print("sending message " + query)
            pwa.sendwhatmsg_instantly("+919346408079",query)
            
        elif 'message' and 'deepu' in query:
            query = query.replace("message", "")
            speak("sending message " + query)
            print("sending message " + query)
            pwa.sendwhatmsg_instantly("+917989924744",query)
            
        elif 'message' and 'daddy' in query:
            query = query.replace("message", "")
            speak("sending message " + query)
            print("sending message " + query)
            pwa.sendwhatmsg_instantly("+919441211211",query)
        
        elif 'message' and 'nikhil' in query:
            query = query.replace("message", "")
            speak("sending message " + query)
            print("sending message " + query)
            pwa.sendwhatmsg_instantly("+917093976715",query)
            
        elif 'message' and 'shiva' in query:
            query = query.replace("message", "")
            speak("sending message " + query)
            print("sending message " + query)
            pwa.sendwhatmsg_instantly("+919940491138",query)
            
        elif 'message' and 'gandhi' in query:
            query = query.replace("message", "")
            speak("sending message " + query)
            print("sending message " + query)
            pwa.sendwhatmsg_instantly("+918309400424",query)
            
        elif 'send image' in query:
            pwa.sendwhats_image("+919940491138",img_path="C:\\Users\\manch\\OneDrive\\Pictures\\Screenshots\\Screenshot (18).jpg")
            
        # elif 'turn Wi-Fi on' in query:
        #     subprocess.run()
        #     MyWish = subprocess.run (['netsh', 'interface', 'set', 'interface', "wi-fi", "ENABLED"])
        #     MyWish
            
        # elif 'turn Wi-Fi off' in query:
        #     subprocess.run()
        #     MyWish = subprocess.run (['netsh', 'interface', 'set', 'interface', "wi-fi", "DISABLED"])
        #     MyWish
        
        elif 'play' in query:
            query = query.replace("play ", "")
            speak('Playing ' + query)
            print('Playing ' + query)
            yt.main(query)
            
        elif 'search' in query:
            query = query.replace("search", "")
            # pwa.playonyt(query)
            # chrome_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            # os.startfile(chrome_dir)
            # write(query)  
            
        elif 'google' in query:
            speak('Searching google...')
            query = query.replace("google", "")
            pwa.search(query)
            
        elif 'exit' in query:
            speak("Thank you, I am always here to help you")
            sys.exit()
