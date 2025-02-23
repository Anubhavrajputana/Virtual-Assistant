import ctypes
import datetime
from distutils import core
from email.mime import audio
from multiprocessing.connection import Client
import os
import shutil
import smtplib
from sqlite3 import apilevel
import sys
import time
# from typing import self
from unicodedata import category
from urllib import response
from urllib.error import URLError
import webbrowser
import pyautogui
import pyttsx3 #!pip install pyttsx3
import requests
import self
import speech_recognition as sr
import json
import pickle
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
import random
import numpy as np
import psutil 
import subprocess
import elevenlabs
import wikipedia
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pyjokes
import wolframalpha
import urlopen
import winshell
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import googlemaps
# from elevenlabs import generate, play 
# from elevenlabs import set_api_key # type: ignore
# from api_key import api_key_data # type: ignore
# set_api_key(api_key_data)

# def engine_talk(query):
#     audio = generate(
#         text=query, 
#         voice='Grace',
#         model="eleven_monolingual_v1"
#     )
#     play(audio)

with open("intents.json") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer=pickle.load(f)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder=pickle.load(encoder_file)
import speech_recognition as sr

def wake_word_detection():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        while True:
            print("Listening...")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print("You said:", text)

                if "wake up" in text.lower():
                    engine.say("Virtual assistant activated!")
                    engine.runAndWait()
                    return True

            except sr.UnknownValueError:
                print("Could not understand audio. Please try again.")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

    
            
    


def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening.......", end="", flush=True)
        r.pause_threshold=1.0
        r.phrase_threshold=0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold=True
        r.operation_timeout=5
        r.non_speaking_duration=0.5
        r.dynamic_energy_adjustment=2
        r.energy_threshold=4000
        r.phrase_time_limit = 10
        # print(sr.Microphone.list_microphone_names())
        audio = r.listen(source)
        
    try:
        print("\r" ,end="", flush=True)
        print("Recognizing......", end="", flush=True)
        query = r.recognize_google(audio, language='en-in')
        print("\r" ,end="", flush=True)
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week

def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = cal_day()

    if(hour>=0) and (hour<=12) and ('AM' in t):
        speak(f"Good morning Sir it's {day} and the time is {t}")
    elif(hour>=12)  and (hour<=16) and ('PM' in t):
        speak(f"Good afternoon Sir it's {day} and the time is {t}")
    else:
        speak(f"Good evening Sir it's {day} and the time is {t}")
    
    
    assname="Thunder"
    speak(f"Sir,I am your Assistant {assname}")
    # speak(assname)
def Myname():
    speak("What should i call you sir")
    myname = command()
    speak(f"Welcome Mister{myname}")
    # speak()
    columns = shutil.get_terminal_size().columns
     
    print(":)".center(columns))
    print("Welcome Mr.", myname.center(columns))
    print("".center(columns))
     
    speak(f"How can i Help you {myname}")
    

   
 
 


def social_media(command):
    
        
    if 'how are you' in command:
            
            speak("I am fine, Thank you")
            speak(f"How are you")
 
    elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")
    elif "what's your name"in command or "what is your name"in command or "tell me your name" in command:
            assname="Thunder"
            speak(f"My Boss call me {assname}")
    elif 'joke' in command:
            speak(pyjokes.get_joke())       
    
 
    elif 'search' in command or 'play' in command:
             
            s = query.replace("search", "") 
            
            s = query.replace("play", "")  
            speak("ok")    
               
            webbrowser.open(s)
    elif "who i am" in command:
            speak("If you talk then definitely your human.")
 
    elif "why you came to world" in command:
            speak("Thanks to Thunder Thinkers.Further It's a secret.")
    elif 'is love' in command:
            speak("It is 7th sense that destroy all other senses")
 
    elif "who are you" in command:
            speak("I am your virtual assistant created by a Team Thunder Thinkers.")
 
    elif 'reason for you' in command:
            speak("I was created as a Minor project by Thunder Thinkers. ")
   
    elif 'lock window' in command or "hibernate" in command or "sleep" in command:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
    
 
    elif 'shutdown system' in command:
                speak("Hold On a Sec ! Your system is on its way to shut down.")
                subprocess.call('shutdown / p /f')
                 
    elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
    elif "don't listen" in command or "stop listening" in command:
            speak("Remember! start me whenever you need")
            exit()
    elif "restart" in command:
            subprocess.call(["shutdown", "/r"])
 
    elif "log off" in command or "sign out" in command:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(10)
            subprocess.call(["shutdown", "/l"])
    elif "show me a note" in command:
            speak("What should you write sir")
            note = input("write there -> ")
            file = open('jarvisNotes.txt', 'w')
            speak("Sir, Should you include date and time")
            snfm = input("type yes/no -> ")
            if 'yes' in snfm or 'sure' in snfm:
                now = datetime.datetime.now()
                future_time = now + relativedelta(days=1, hours=2)
                formatted_time = future_time.strftime("%Y-%m-%d %H:%M:%S")
                # print(formatted_time)
                file.write(formatted_time)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
    elif "show me a written note" in command:
            speak("Showing Notes")
            file = open("jarvisNotes.txt", "r") 

            print(file.read())
            speak(file.read(6))
    elif "jarvis" in command:
            # wishMe()
            speak("Master in your service")
    elif 'facebook' in command:
        speak("opening your facebook")
        webbrowser.open("https://www.facebook.com/")
    elif 'whatsapp' in command:
        speak("opening your whatsapp")
        webbrowser.open("https://web.whatsapp.com/")
    elif 'discord' in command:
        speak("opening your discord server")
        webbrowser.open("https://discord.com/")
    elif 'instagram' in command:
        speak("opening your instagram")
        webbrowser.open("https://www.instagram.com/")
    elif 'youtube' in command:
        speak("opening your youtube")
        webbrowser.open("https://www.youtube.com/")
    elif 'twitter' in command:
        speak("opening twitter")
        webbrowser.open("https://www.twitter.com/")
    elif 'chat GPT' in command:
        speak("opening chat GPT")
        webbrowser.open("https://www.chatgpt.com/")
    elif "which day it is" in command:
            tellDay()
            
         
    elif "tell me the time" in command:
            tellTime()
    elif "hey Thunder" in command:

        question =speak("what you want to calculate?")
        question=print("what you want to calculate ?")
        question=input("type there : ")
  
# App id obtained by the above steps 
        app_id = 'WKGG5H-7J9QWLR894'
  
# Instance of wolf ram alpha  
# client class 
        client = wolframalpha.Client(app_id) 
  
# Stores the response from  
# wolf ram alpha 
        res = client.query(question) 
  
# Includes only text from the response 
        answer = next(res.results).text 
        print(answer)
    elif "flipkart"in command:
         speak("opening flipkart")
         webbrowser.open("https://www.flipkart.com")   
    elif "amazon"in command:
         speak("opening amazon")
         webbrowser.open("https://www.amazon.com")  
    
    else:
        speak("No result found")
    
     

def schedule():
    day = cal_day().lower()
    speak("Boss today's schedule is ")
    week={
    "monday": "Boss, from 9:30 to 10:30 you have Data Warehouse class, from 10:30 to 11:30 you have Mobile and Adhoc computing class, from 11:30 to 12:30 you have Full stack Development class,from 12:30 to 1:30 you have a IOT and Block Chain class ,from 1:30 to 2:30 you have a break ,from 2:30 to 3:30 you have Q and R class and from 3:30 to 4:30 you have MP and ES class.",
    "tuesday": "Boss, from 9:30 to 11:30 you have VAM class of two hours, from 11:30 to 1:30 you have OOAD lab, from 1:30 to 2:30 you have a lunch break,from 2:30 to 3:30 you have MP and ES class ,from 3:30 to 4:30 you have IOT and Block Chain class .",
    "wednesday": "Boss, from 9:30 to 10:30 you have Q and R class, from 10:30 to 11:30 you have Mobile and Adhoc computing class, from 11:30 to 1:30 you have Minor Project lab,from 1:30 to 2:30 you have a break ,from 2:30 to 3:30 you have Full Stack Development class ,from 3:30 to 4:30 you have OOAD class.",
    "thursday": "Boss, from 9:30 to 10:30 you have Data Warehouse class, from 10:30 to 11:30 you have MP and ES class, from 11:30 to 12:30 you have OOAD class,from 12:30 to 1:30 you have a IOT and Block Chain class ,from 1:30 to 2:30 you have a break ,from 2:30 to 4:30 you have AEC class.",
    "friday": "Boss, from 9:30 to 10:30 you have Mobile and Adhoc computing class, from 10:30 to 11:30 you have Full Stack Development class, from 11:30 to 1:30 you have Full stack Development lab,from 1:30 to 2:30 you have a break ,from 2:30 to 3:30 you have Data Warehouse class and from 3:30 to 4:30 you have OOAD class.",
    "saturday": "Boss, today you are on leave.",
    "sunday": "Boss, today you are on leave."
    }
    if day in week.keys():
        speak(week[day])

def openApp(command):
    
    if "calculator" in command:
        speak("opening calculator")
        os.startfile('C:\\Windows\\System32\\calc.exe')
        
    
    elif "notepad" in command:
        speak("opening notepad")
        # os.startfile('c:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2408.12.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe')
        os.startfile('c:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2409.9.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe')
    elif "paint" in command:
        speak("opening paint")
        os.startfile('c:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2408.30.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe')
    elif "mail" in command:
        speak("opening mail")
        os.startfile('c:\\Program Files\\WindowsApps\\Microsoft.OutlookForWindows_1.2024.1009.100_x64__8wekyb3d8bbwe\\olk.exe')
    elif "word"in command:
        speak("opening ms word")
        os.startfile('c:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
    elif "camera" in command:    
        speak("opening camera")  
        os.startfile('c:\\Program Files\\WindowsApps\\Microsoft.WindowsCamera_2024.2408.1.0_x64__8wekyb3d8bbwe\\WindowsCamera.exe')
    elif "excel" in command:
        speak("opening ms excel")  
        os.startfile('c:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE')
    elif "calendar" in command:
       speak("opening calendar")  
       os.startfile('c:\\Program Files\\WindowsApps\\64885BlueEdge.OneCalendar_2024.717.1.0_x64__8kea50m9krsh2\\CalendarApp.Gui.Win10.exe')
    elif "vs code"in command:
        speak("opening vs code ")
        os.startfile('c:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')    
    elif "task manager"in command:
        speak("opening task manager ")
        os.startfile("c:\\Windows\\System32\\Taskmgr.exe")
    elif "file explorer"in command:
         speak("opening file explorer")
         os.startfile("c:\\Windows\\explorer.exe")
    
        
  

def closeApp(command):
    
    
    if "file explorer" in command:
        speak("closing file explorer")
        os.system("taskkill /f /im explorer.exe")
    elif "task manager" in command:
        speak("closing task manager")
        os.system("taskkill /f /im Taskmgr.exe")
    elif "calculator" in command:
        speak("closing calculator")
        os.system("taskkill /f /im calc.exe")
    elif "notepad" in command:
        speak("closing notepad")
        os.system('taskkill /f /im Notepad.exe')
    elif "paint" in command:
        speak("closing paint")
        os.system('taskkill /f /im mspaint.exe')
    elif "mail" in command:
        speak("closing your mail")
        os.system('taskkill /f /im msedgewebview2.exe')
    elif "camera" in command:
        speak("closing your camera")
        os.system('taskkill /f /im WindowsCamera.exe')
    elif "word" in command:
        speak("closing your ms word")
        os.system('taskkill /f /im WINWORD.exe')
    elif "excel" in command:
        speak("closing your ms excel")
        os.system('taskkill /f /im EXCEL.EXE')
    elif "calendar" in command:
        speak("closing your calendar")
        os.system('taskkill /f /im CalendarApp.Gui.Win10.exe')
    elif "vs code" in command:
        speak("closing your visual studio code")
        os.system('taskkill /f /im Code.exe')
    
    

def browsing(query):
    if 'google' in query:
        speak("Boss, what should i search on google..")
        s = command().lower()
        webbrowser.open(f"{s}")
    elif 'map' in query:
        speak("Boss, what should i search on map")
        s = command().lower()
        webbrowser.open(f"{s}")
    
    elif 'chrome' in query:
        speak("opening chrome..")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
       
    elif 'edge' in query:
        speak("opening your microsoft edge")
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

def condition():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percentage")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Boss our system have {percentage} percentage battery")

    if percentage>=80:
        speak("Don't worry Boss I have enough charging.Continue our communication....")
        
    elif percentage>40 and percentage<60:
        speak("Boss you should connect me to charging point to charge my battery..")
        
        
    else:
        speak("Sorry Boss I have very low power, please connect me to charging otherwise I'll be off. you've to shut down your computer in any how.")
        speak("Sir do u want to switch off the computer ?")
        take = input("type yes/no : ")
        choice = take
        if choice == 'yes':

		
		# Shutting down
	        # print("Shutting down the computer")
            speak("Shutting down the computer")
            os.system("shutdown /s /t 30")
        if choice == 'no':
            speak("Thank u sir,Continue...")
# Method to self shut down system

def tellDay():
     
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
     
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
 
 
def tellTime():
     
    # This method will give the time
    t = time.strftime("%I:%M:%p")
     
   
    speak(f"The time is {t} ")    
 
def process_wikipedia_query(query):
    try:
        if "wikipedia" in query:
            print("Checking Wikipedia")
            search_term = query.replace("wikipedia", "").strip()
            result = wikipedia.summary(search_term, sentences=20)  # Adjust sentences as needed
            speak("According to Wikipedia:")
            print(result)
            # Replace with your actual text-to-speech function
            speak(result)
        else:
            print("Query does not contain 'wikipedia'")
    except wikipedia.exceptions.PageNotFound:
        print("Wikipedia page not found")
    except Exception as e:
        print("An error occurred:", e)
def changing_name_command(command):
    if "change your name to" in command:
        new_name = command.replace("change your name to", "").strip()
        speak(f"Thanks for naming me {new_name}!")
    elif "change your name" in command:
        print("Please specify a new name, e.g., 'change your name to Alex'")









# ---------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    while True: 

        if wake_word_detection():
            # Perform actions after wake word is detected
            print("Thunder is ready to assist you!")
            break
    
    wishMe()
    Myname()
#  ---------------------------------------------------------------------------------------------------------------------------------------------
    
    while True:
        query = command().lower()
        # query  = input("Enter your command-> ")
        
        if("what is your name"in query)or("tell me your name"in query)or('flipkart' in query) or('amazon' in query) or("hey Thunder" in query)or('facebook' in query) or ('discord' in query) or ('whatsapp' in query) or ('instagram' in query)or ('youtube' in query)or ('twitter' in query)or ('chat GPT' in query)or("which day it is" in query)or("tell me the time" in query)or("how are you" in query)or ('fine' in query)or ('good' in query)or ("what's your name" in query)or ('What is your name' in query)or ('joke' in query)or ('search' in query)or ('play' in query)or ('who i am' in query)or ('why you came to world' in query)or ('is love' in query)or ('who are you' in query)or ('reason for you' in query)or ('lock window' in query)or ('shut down system' in query)or ('empty recycle bin' in query)or ("don't listen" in query)or ('stop listening' in query)or ('restart' in query)or ('sleep' in query)or ('hibernate' in query)or ('log off' in query)or ('sign out' in query)or ('show me a note' in query)or ('show me a written note' in query)or ('jarvis' in query):
            social_media(query)
        
        
        elif ("university time table" in query) or ("schedule" in query):
            schedule()
        elif ("volume up" in query) or ("increase the volume" in query):
            pyautogui.press("volumeup")
            speak("Volume increased")
        elif ("volume down" in query) or ("decrease the volume" in query):
            pyautogui.press("volumedown")
            speak("Volume decrease")
        elif ("volume mute" in query) or ("mute the sound" in query):
            pyautogui.press("volumemute")
            speak("Volume muted")
        elif ("unmute the sound" in query):
            pyautogui.press("volumeunmute")
            speak("Volume unmuted")
        elif("open file explorer"in query) or("open task manager"in query) or("open vs code"in query) or("open calculator" in query) or ("open notepad" in query) or ("open paint" in query)or ("open mail" in query)or ("open camera" in query)or ("open word" in query)or ("open excel" in query)or ("open calendar" in query):
            openApp(query)
        elif("close file explorer"in query) or("close task manager"in query) or("close vs code"in query) or("close calculator" in query) or ("close notepad" in query) or ("close paint" in query)or ("close mail" in query)or ("close camera" in query)or ("close word" in query)or ("close excel" in query)or ("close calendar" in query):
            closeApp(query)
        elif("wikipedia"in query):
            process_wikipedia_query(query)
        elif("change your name to"in query)or("what is your new name" in query):
             changing_name_command(query)
        
                
                
        # elif("close news"in query)or("close power point" in query )or("close setting" in query )or("close file explorer"in query) or("close task manager"in query) or("close vs code"in query) or ("close calculator" in query) or ("close notepad" in query) or ("close paint" in query)or ("close mail" in query)or ("close camera" in query)or ("close word" in query)or ("close excel" in query)or ("close calendar" in query):
            # closeApp(query)
        elif ("what" in query) or ("who" in query) or ("how" in query) or ("hi" in query) or ("thanks" in query) or ("hello" in query):
                padded_sequences = pad_sequences(tokenizer.texts_to_sequences([query]), maxlen=20, truncating='post')
                result = model.predict(padded_sequences)
                tag = label_encoder.inverse_transform([np.argmax(result)])

                for i in data['intents']:
                    if i['tag'] == tag:
                        speak(np.random.choice(i['responses']))
        elif ("open google" in query) or ("open edge" in query)or("open chrome"in query):
            browsing(query)
        elif ("system condition" in query) or ("condition of the system" in query) or ("check my system" in query):
            speak("checking the system condition")
            condition()
        
        elif "exit" in query:
            speak("I'm exiting.")
            sys.exit()
