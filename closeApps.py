import os
import keyboard

def CloseCode():
    os.system("TASKKILL /F /im code.exe")
    
def CloseBluestacks():
    os.system("TASKKILL /F /im HD-Player.exe")
    
def CloseRstudio():
    os.system("TASKKILL /F /im rstudio.exe")
    
def CloseSql():
    os.system("TASKKILL /F /im MySQLWorkbench.exe")
    
def CloseWord():
    os.system("TASKKILL /F /im WINWORD.EXE")
    
def CloseExcel():
    os.system("TASKKILL /F /im EXCEL.EXE")
    
def ClosePowerpoint():
    os.system("TASKKILL /F /im POWERPNT.EXE")
    
def CloseFacebook():
    keyboard.press_and_release('ctrl + w')
    
def CloseYoutube():
    keyboard.press_and_release('ctrl + w')
    
def CloseInstagram():
    keyboard.press_and_release('ctrl + w')
    
def ClosFlipkart():
    keyboard.press_and_release('ctrl + w')
    
def CloseChrome():
    os.system("TASKKILL /F /im chrome.exe")
    
def CloseWhatsapp():
    keyboard.press_and_release('ctrl + w')
    
def CloseMap():
    keyboard.press_and_release('ctrl + w')