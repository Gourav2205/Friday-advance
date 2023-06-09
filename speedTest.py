import speedtest
import pyttsx3

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[2].id)
Assistant.setProperty('rate', 180)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

speed = speedtest.Speedtest()

def SpeedTest(term):
    Speak("Checking Speed....")
    uploading = speed.upload()
    correctUp = int(uploading/800000)
    downloading = speed.download()
    correctDown =  int(downloading/800000)  
    if 'upload' in term:
        Speak(f"The Uploading Speed Is {correctUp} mbp s")
        
    elif 'download' in term:
        Speak(f"The Downloading Speed Is {correctDown} mbp s")
    
    else :
        Speak(f"The Downloading Speed Is {correctDown} mbp s and The Uploading Speed Is {correctUp} mbp s")
        
    