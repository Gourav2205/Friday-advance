import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
from googletrans import Translator
import keyboard
import pyjokes
from pywikihow import search_wikihow
import os
from pynput.keyboard import Key, Controller
from pydictionary import PyDictionary
from whatsapp import *
from openApp import *
from closeApps import *
from speedTest import *
from Auto import *
from Features import *
from PdfReader import *


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[3].id)
Assistant.setProperty('rate', 180)

keyboard1 = Controller()

Diction = PyDictionary()

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

def wishme():
        hr = int(datetime.datetime.now().hour)
        if hr>=0 and hr<12:
            Speak("Good Morning Boss!")
        
        elif hr>=12 and hr<17:
            Speak("Good Afternoon Boss!")
        
        else:
            Speak("Good Evening Boss!")
            
        # Speak("I Am Friday. Your Personal AI Assistant. Please Tell Me How Can I Help You?")

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try:
            print("Recognizng.....")
            query = command.recognize_google(audio,language='en-in')
            
        except:
            return "none"
        
        return query.lower()
    
def takecommand_hindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try:
            print("Recognizng.....")
            query = command.recognize_google(audio,language='hi')
            
        except:
            return "none"
        
        return query.lower()

def TaskExe():
    wishme()
    def Music():
        Speak("Tell Me The Name Of The Song!")
        musicName = takecommand()
        if 'chere jeyona' in musicName:
            os.startfile('C:\\Users\\GOURAV\\Music\\Resso Music\\Chere Jeyona.mp3')
            
        elif 'oviman' in musicName:
            os.startfile('C:\\Users\\GOURAV\\Music\\Resso Music\\Oviman.mp3')
            
        else:
            pywhatkit.playonyt(musicName)
            Speak("Your Song Has Been Started!, Enjoy Boss..")
            
    def Whatsapp():
        Whatsappp()
    
    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)
        
            try:
                print("Recognizng.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")
            
            except:
                return "none"
        
            return query.lower() 
    
    def Tran():
        Speak("Tell Me The Line")
        line = TakeHindi()
        trans = Translator()
        result = trans.translate(line)
        Text = result.text
        Speak(Text)
    
    while True:
        query = takecommand()
        
        if 'hello' in query:
            Speak("Hello Boss, I Am friday. Your Personal AI Assistant. How May I Help You?")
            
        elif 'how are you' in query:
            Speak("I Am Fine Boss!, Whats About You?")
            
        elif 'you need a break' in query:
            Speak("Ok Boss, You Can Call Me Anytime!")
            quit()
            
        elif 'bye' in query:
            Speak("Ok Boss, Bye!")
            quit()
            
        elif 'quit' in query:
            query = query.replace("friday","")
            Speak("Ok Boss, Bye!")
            quit()
            
        elif'youtube search' in query:
            YtSearch()
            
        # elif 'google search' in query:
        #     Speak("Ok Boss, This Is What I Found For Your Search!")
        #     query = query.replace("friday","")
        #     query = query.replace("google search","")
        #     pywhatkit.search(query)
        #     Speak("Done Boss!")
            
        elif 'website' in query:
            Website()
            
        elif 'music' in query:
            Music()
            
        elif 'wikipedia' in query:
            Wikipedia()
            
        elif 'send whatsapp message' in query:
            Whatsapp()
            
        elif 'screenshot' in query:
            screenshot()
            
        elif 'open code' in query:
            OpenAppss(query)
            
        elif 'open whatsapp' in query:
            OpenAppss(query)
            
        elif 'open bluestacks' in query:
            OpenAppss(query)
            
        elif 'open r studio' in query:
            OpenAppss(query)
            
        elif 'open sql' in query:
            OpenAppss(query)
            
        elif 'open word' in query:
            OpenAppss(query)
            
        elif 'open excel' in query:
            OpenAppss(query)
            
        elif 'open powerpoint' in query:
            OpenAppss(query)
            
        elif 'open facebook' in query:
            OpenAppss(query)
            
        elif 'open instagram' in query:
            OpenAppss(query)
            
        elif 'open youtube' in query:
            OpenAppss(query)
            
        elif 'open flipkart' in query:
            OpenAppss(query)
            
        elif 'open chrome' in query:
            OpenAppss(query)
            
        elif 'open map' in query:
            OpenAppss(query)
            
        elif 'close code' in query:
            CloseCode()
            
        elif 'close map' in query:
            CloseMap()
            
        elif 'close bluestacks' in query:
            CloseBluestacks()
            
        elif 'close r studio' in query:
            CloseRstudio()
            
        elif 'close sql' in query:
            CloseSql()
            
        elif 'close word' in query:
            CloseWord()
            
        elif 'close excel' in query:
            CloseExcel()
            
        elif 'close powerpoint' in query:
            ClosePowerpoint()
            
        elif 'close facebook' in query:
            CloseFacebook()
            
        elif 'close youtube' in query:
            CloseYoutube()
            
        elif 'close instagram' in query:
            CloseInstagram()
            
        elif 'close flipkart' in query:
            ClosFlipkart()
            
        elif 'close chrome' in query:
            CloseChrome()
            
        elif 'close whatsapp' in query:
            CloseWhatsapp()
            
        elif 'pause' in query:
            keyboard.press('k')
            
        elif 'play' in query:
            keyboard.press('k')
            
        elif 'restart' in query:
            keyboard.press('0')
            
        elif 'mute' in query:
            keyboard.press('m')
            
        elif 'skip' in query:
            keyboard.press('l')
            
        elif 'back' in query:
            keyboard.press('j')
            
        elif 'full screen' in query:
            keyboard.press('f')
            
        elif 'default' in query:
            keyboard.press('f')
            
        elif 'film mode' in query:
            keyboard.press('t')
            
        elif 'youtube tools' in query:
            YtAuto()
            
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
            
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
            
        elif 'current location' in query:
            keyboard1.press(Key.ctrl)   
            keyboard1.press(Key.shift)   
            keyboard1.press('l') 
            keyboard1.release(Key.ctrl)  
            keyboard1.release(Key.shift)  
            keyboard1.release('l')  
            
        elif 'search in map' in query:
            Speak("Please tell me your search")
            mm = takecommand()
            keyboard.write(mm)
            keyboard.press('enter')
            
        elif 'chrome atumation' in query:
            ChromeAuto()
            
        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
            
        elif 'repeat my word' in query:
            Speak("Speak Boss!")
            my_words = takecommand()
            Speak(f"You Said : {my_words}")    

        elif 'dictionary' in query:
            Dict()
            
        elif 'alarm' in query:
            Alarm()

        elif 'translator' in query:
            Tran()
            
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = query.replace("friday","")
            Speak("You Tell Me To Remind You That :"+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()
            
        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            Speak("You Tell Me That"+remember.read())
        
        elif 'google search' in query:
            GoogleSearch()   

        elif 'temperature' in query:
            Temp()

        elif 'read book' in query:
            Reader()

        elif 'internet speed' in query:
            SpeedTest(query)
            
        elif 'upload speed' in query:
            Query = query.replace("speed","")
            SpeedTest(Query)
            
        elif 'download speed' in query:
            Query = query.replace("speed","")
            SpeedTest(Query)
        
        elif 'how to' in query:
            Speak("Getting Data From The Internet!")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
        
TaskExe()