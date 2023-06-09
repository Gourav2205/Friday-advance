import os
import PyPDF2
import playsound
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[3].id)
Assistant.setProperty('rate', 180)

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


def Reader():
    Speak("Tell Me The Name Of The Book!")
    name = takecommand()
    
    if 'methods of data collection' in name:
        os.startfile('E:\\Coding\\PythonCourse\\Jarvis\\books\\Methods Of Data Collection.pdf')
        book = open('E:\\Coding\\PythonCourse\\Jarvis\\books\\Methods Of Data Collection.pdf','rb')
        pdfreader = PyPDF2.PdfFileReader(book)    
        pages = pdfreader.getNumPages()
        Speak(f"Number Of Pages In This Books Are {pages}")
        Speak("From Which Page I Have To Start Reading?")
        # numPage = int(input("Enter The Page Number :"))
        numPage = int(takecommand())
        page = pdfreader.getPage(numPage)
        text = page.extractText()
        Speak("In Which Language, I have To Read?")
        lang = takecommand()
    
        if 'hindi' in lang:
            trans1 = Translator()
            textHin = trans1.translate(text, 'hi')
            textm = textHin.text
            speech = gTTS(text = textm)
            
            try:
                speech.save('book.mp3')
                playsound('book.mp3')
                
            except:
                playsound('book.mp3')
        
        else:
            Speak(text)
            
        book.close()
    
    elif 'sql' in name:
        os.startfile('E:\\Coding\\PythonCourse\\Jarvis\\books\\SQL.pdf')
        book = open('E:\\Coding\\PythonCourse\\Jarvis\\books\\SQL.pdf','rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.getNumPages()
        Speak(f"Number Of Pages In This Books Are {pages}")
        Speak("From Which Page I Have To Start Reading?")
        # numPage = int(input("Enter The Page Number :"))
        numPage = int(takecommand())
        page = pdfreader.getPage(numPage)
        text = page.extractText()
        Speak("In Which Language, I have To Read?")
        lang = takecommand()
        
        if 'hindi' in lang:
            trans1 = Translator()
            textHin = trans1.translate(text, 'hi')
            textm = textHin.text
            speech = gTTS(text = textm)
            
            try:
                speech.save('book1.mp3')
                playsound('book1.mp3')
                
            except:
                playsound('book1.mp3')
                
        else:
            Speak(text)