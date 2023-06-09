import pyttsx3
import speech_recognition as sr
import pywhatkit

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

def Whatsappp():
    Speak("Tell Me The Name Of the Person!")
    name = takecommand()
    
    if 'sonu' in name:
        Speak("Tell Me The Messege!")
        msg = str(takecommand())
        Speak("Tell Me THe Time Boss!")
        Speak("Time In Hour")
        hour = int(takecommand())
        Speak("Time In Minutes!")
        min = int(takecommand())
        Speak("Ok Boss, Sending Whatsapp Messege!")
        pywhatkit.sendwhatmsg("+919883632781", msg, hour, min, 15, True, 3)
        Speak("Boss, Your Messege Send Successfully!")
        
    else:
        Speak("The name doesn't match any name in your contact")
        Speak("Please tell Me The Number!")
        phone = takecommand()
        ph = str("+91") + phone
        Speak("Tell Me The Messege!")
        msg = takecommand()
        Speak("Tell Me THe Time Boss!")
        Speak("Time In Hour")
        hour = int(takecommand())
        Speak("Time In Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg(ph,msg,hour,min,20,True,5)
        Speak("Ok Boss, Sending Whatsapp Messege!")
        
