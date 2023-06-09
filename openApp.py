import os
import webbrowser

def OpenAppss(term):
    if 'open code' in term:
        os.startfile("C:\\Users\\GOURAV\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            
    elif 'open bluestacks' in term:
        os.startfile("C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe")
        
    elif 'open r studio' in term:
        os.startfile("C:\\Program Files\\RStudio\\bin\\rstudio.exe")

    elif 'open sql' in term:
        os.startfile("C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe")
        
    elif 'open word' in term:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        
    elif 'open excel' in term:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        
    elif 'open powerpoint' in term:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
        
    elif 'open chrome' in term:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
    elif 'open facebook' in term:
        webbrowser.open('https://www.facebook.com/')
        
    elif 'open map' in term:
        webbrowser.open('https://www.google.com/maps/')

    elif 'open youtube' in term:
        webbrowser.open('https://www.youtube.com/')
        
    elif 'open instagram' in term:
        webbrowser.open('https://www.instagram.com/')
        
    elif 'open flipkart' in term:
        webbrowser.open('https://www.flipkart.com/')
        
    elif 'open whatsapp' in term:
        webbrowser.open('https://web.whatsapp.com/')
    
    
