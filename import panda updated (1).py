import pandas as pd #data manipulation and analysis.
import datetime # to get current date
from plyer import notification # to generate notification
import pyttsx3 # to speak written text 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def notifyme(title,msg):
    notification.notify(
                    title = title,
                    message = msg,
                    app_name = "Reminder",
                    app_icon = "D:\\birthday reminder app\\WhatsApp-Image-2022-12-04-at-11.15.21.ico",
                    timeout = 8
                )
df=pd.read_excel("D:\\birthday reminder app\\python project excel sheet.xlsx")           
today=datetime.datetime.now().strftime("%d-%m-")
print(today)
'''
"D:\birthday reminder app\python project excel sheet.xlsx"
'''
for index,item in df.iterrows():
        bd=item["birthday"]
        if today == bd:
            a=item["NAME"]
            notifyme("Birthday Alert","It's "+a+"'s birthday today.")
            speak("Jatin!! It's "+a+"s birthday today")
 





































































