import speech_recognition as sr
import  os
import  pyttsx3
import webbrowser
import time
import os
import pyautogui
from tkinter import *

root = Tk()
root.iconbitmap(r"E:\Photos\icon\englishflag.ico")
root.wm_attributes("-topmost", 1)
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry("150x30+1200+675")

def voiceRecog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('speak......')
        audio = r.listen(source)

        try:

            text = r.recognize_google(audio)

            
            engine = pyttsx3.init()
            print(text)
            engine.say(text)
            engine.runAndWait()

           
            if 'close Brave' in text:
                #pyautogui.click(x=1340,y=3)
                os.system('taskkill /F /im brave.exe')

            elif 'open Chrome' in text:
                os.system('start chrome.exe')

            elif 'close Chrome' in text:
                os.system('taskkill /F /im chrome.exe')

            

            elif 'in youtube' in text.lower():
                text = text.lower()
                text = text.replace(' in youtube',"")
                url = 'https://www.youtube.com/results?search_query='+text
                webbrowser.open(url)
            elif 'youtube' in text.lower():
                url = 'https://www.youtube.com'
                webbrowser.open(url)
            elif 'open facebook' in text.lower():
                url = 'https://www.facebook.com'
                webbrowser.open(url)
            elif 'messenger' in text.lower():
                url = 'https://www.facebook.com/messages/t/hide.me.from.fb'
                webbrowser.open(url)
            elif 'duckduckgo' in text.lower():
                text = text.lower()
                text = text.replace('duckduckgo',"")
                url = 'https://duckduckgo.com/?q='+text
                webbrowser.open(url)

            elif 'in bing' in text.lower():
                text = text.lower()
                text = text.replace(' in bing',"")
                url = 'https://bing.com/?q='+text
                webbrowser.open(url)
                
            else:
                url = 'https://www.google.com/search?q='+text
                webbrowser.open(url)
                time.sleep(2)

        except:
            print('cant hear or recognize')
	    

'''        
while True:
    #input('Press Enter: ')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('speak......')
        audio = r.listen(source)

        try:

            text = r.recognize_google(audio)

            
            engine = pyttsx3.init()
            print(text)
            engine.say(text)
            engine.runAndWait()

            if text == 'stop':
                break
 
            elif 'hello' in text:
                continue
            elif 'close Brave' in text:
                #pyautogui.click(x=1340,y=3)
                os.system('taskkill /F /im brave.exe')

            elif 'open Chrome' in text:
                os.system('start chrome.exe')

            elif 'close Chrome' in text:
                os.system('taskkill /F /im chrome.exe')

            elif 'in youtube' in text.lower():
                text = text.lower()
                text = text.replace(' in youtube',"")
                url = 'https://www.youtube.com/results?search_query='+text
                webbrowser.open(url)
            elif 'youtube' in text.lower():
                url = 'https://www.youtube.com'
                webbrowser.open(url)
            elif 'facebook' in text.lower():
                url = 'https://www.facebook.com'
                webbrowser.open(url)
            elif 'messenger' in text.lower():
                url = 'https://www.facebook.com/messages/t/hide.me.from.fb'
                webbrowser.open(url)
            elif 'duckduckgo' in text.lower():
                text = text.lower()
                text = text.replace('duckduckgo',"")
                url = 'https://duckduckgo.com/?q='+text
                webbrowser.open(url)

            elif 'in bing' in text.lower():
                text = text.lower()
                text = text.replace(' in bing',"")
                url = 'https://bing.com/?q='+text
                webbrowser.open(url)
                
            else:
                url = 'https://www.google.com/search?q='+text
                webbrowser.open(url)
                time.sleep(2)

        except:
            print('cant hear or recognize')

'''
btn = Button(root,text='Speak',command=voiceRecog)
btn.pack()
root.mainloop()
