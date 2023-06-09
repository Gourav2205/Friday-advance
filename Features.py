import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
from pydictionary import PyDictionary
import os
import pyautogui
from bs4 import BeautifulSoup
import requests
import playsound
import datetime
import pywhatkit

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[3].id)
Assistant.setProperty('rate', 180)

Diction = PyDictionary()

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()
    
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
    
def YtSearch():
    Speak("Ok Boss, This Is What I Found For Your Search!")
    query = query.replace("friday","")
    query = query.replace("youtube search","")
    web = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(web)    
    Speak("Done Boss!")
    
def GoogleSearch():
    import wikipedia as googleScrap
    query = query.replace("friday","")     
    query = query.replace("google search","")     
    query = query.replace("google","")
    Speak("This is What I found On The Web")
    pywhatkit.search(query)
    
    try:
        result = googleScrap.summary(query,3) 
        Speak(result)
        
    except:
        Speak("No Speakable Data Available!")  
    
def Website():
    Speak("Ok Boss, This Is What I Found For Your Search!")
    query = query.replace("friday","")
    query = query.replace("website","")
    query = query.replace(" ","")
    web1 = query.replace("open","")
    web2 = 'https://www.' + web1 + '.com'
    webbrowser.open(web2)
    Speak("Launched...")
    
def Wikipedia():
    Speak("Searching Wikipedia....")
    query = query.replace("friday","")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=2)
    Speak("According To Wikipedia") 
    Speak(results)
    
def Dict():
    Speak("Activated Dictionary")
    Speak("Tell Me The Problem")
    prb = takecommand()
    
    if 'meaning' in prb:
        prb = prb.replace("what is the","")
        prb = prb.replace("friday","")
        prb = prb.replace("of","")
        prb = prb.replace("meaning of","")
        results = Diction.meaning(prb)
        Speak(f"The Meaning For {prb} is {results}")
        
    elif 'synonym' in prb:
        prb = prb.replace("what is the","")
        prb = prb.replace("friday","")
        prb = prb.replace("of","")
        prb = prb.replace("synonym of","")
        results = Diction.synonym(prb)
        Speak(f"The Synonym For {prb} is {results}")
        
    elif 'antonym' in prb:
        prb = prb.replace("what is the","")
        prb = prb.replace("friday","")
        prb = prb.replace("of","")
        prb = prb.replace("antonym","")
        results = Diction.antonym(prb)
        Speak(f"The Antonym For{prb} is {results}")
        print(prb)
        
    Speak("Excited Dictionary!")
    
def screenshot():
    Speak("Ok Boss, What Should I Name That File?")
    path = takecommand()
    path1name = path + ".png" 
    path1 = "E:\\Coding\\PythonCourse\\Jarvis\\ScreenShots\\"+ path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("E:\\Coding\\PythonCourse\\Jarvis\\ScreenShots")
    Speak("Here Is Your Screenshot")
    
def Temp():
    search = "temperature in kolkata"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    Speak(f"The Temperature Is {temperature}")
    
def Alarm():
    Speak("Tell Me The Time!")
    Speak("Time in hour")
    
    time = input(": Enter The Tine :")   
    while True:
        Time_Ac = datetime.datetime.now()
        now = Time_Ac.strftime("%H:%M:%S")
        
        if now == time:
            Speak("Time To Wake Up Boss!")
            playsound('E:\\Coding\\PythonCourse\\Jarvis\\ring.mp3')
            Speak("Alarm Closed!")
            
        elif now>time:
            break
        
