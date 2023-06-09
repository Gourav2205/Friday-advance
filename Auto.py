import keyboard
import pyttsx3
import speech_recognition as sr

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

def YtAuto(): 
    Speak("Whats Your Command?")
    comm = takecommand()
     
    if 'pause' in comm:
        keyboard.press('k')
        
    elif 'play' in comm:
        keyboard.press('k')
        
    elif 'restart' in comm:
        keyboard.press('0')
        
    elif 'mute' in comm:
        keyboard.press('m')
        
    elif 'skip' in comm:
        keyboard.press('l')
        
    elif 'back' in comm:
        keyboard.press('j')
        
    elif 'full screen' in comm:
        keyboard.press('f')
        
    elif 'default' in comm:
        keyboard.press('f')
        
    elif 'film mode' in comm:
        keyboard.press('t')
        
    Speak("Done Boss!") 
        
def ChromeAuto():
    Speak("Chrome Automation Started")   
    
    command = takecommand()
    
    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')
        
    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')
        
    elif 'history' in command:
        keyboard.press_and_release('ctrl + h')
        
    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')   
        
    elif 'current location' in command:
        keyboard.press_and_release('ctrl + shift, l')   
        
    elif 'search' in command:
        Speak("Please tell me your search")
        mm = takecommand()
        keyboard.write(mm)
        keyboard.press('enter')