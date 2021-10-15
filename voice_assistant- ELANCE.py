import pyttsx3 # TTS library (text-to-speech conversion library)
import datetime # supplies classes to work with date and time
import speech_recognition as sr #this also requires PyAudio because it uses the Microphone class
import wikipedia #Python library that makes it easy to access and parse data from Wikipedia.
import smtplib #defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import webbrowser as wb #provides a high-level interface to allow displaying Web-based documents to users.
import os
import pyautogui #cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.
import psutil 
""" psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system 
utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process 
resources and management of running processes. """
import pyjokes #One line jokes for programmers

engine = pyttsx3.init() #initialises the pyttsx3 modules

""" VOICE """
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice',voices[1].id) #changing index, changes voices. 1 for female

""" RATE """
rate = engine.getProperty('rate') #getting details of current speaking rate
newVoiceRate = 150 
engine.setProperty('rate',newVoiceRate) #setting up new voice rate

""" VOLUME """
volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H : %M : %S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year) #extracts the current year from now function
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Loading your AI personal assistant - Elance")
    speak("Welcome Back !")
    hour = datetime.datetime.now().hour

    if hour >=6 and hour<=12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<=24:
        speak("Good evening")
    else:
        speak("Good night")
    
    speak("Elance at your service. How I can help you? ")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: # use the default microphone as the audio source
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) # listen for the first phrase and extract it into audio data

    try:
        print("Recognizing...")
        query = r.recognize_google(audio) # recognize speech using Google Speech Recognition
        print("You said " + query)
    except Exception as e: # speech is unintelligible
        print(e)
        speak("Could not understand audio...")

        return "None"
    
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587) #need to also specify port number; 587- default mail submission port
    server.ehlo()
    server.starttls() #predefined function to send mail
    server.login("bstanushree@gmail.com","harshini")
    server.sendmail("bstanushree@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:/PROJECTS/ss.png")

def cpu():
    usage = str(psutil.cpu_percent)
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery #will return as a list
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__" :

    wishme()

    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            speak("Going offline! Thanks for using me, Have a good day ahead!")
            quit()

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2) #it speaks out two sentences from the result of query
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "adarshc4714@gmail.com"
                sendmail(to, content)
                speak("The mail was sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com") #to open chrome new tab

        elif "log out" in query:
            os.system("shutdown - l")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")
        
        elif "play songs" in query:
            songs_dir = "C:/Users/Tanu Shetty/Music"
            songs = os.listdir(songs_dir) #gives out the list of songs on my system at that directory
            os.startfile(os.path.join(songs_dir, songs[0])) #it will play the first song

        elif "remember that" in query:
            speak("What should I remember?")
            data = takecommand() #will take the input from user
            speak("You said me to remember that " + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("You said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done taking the screenshot! ")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()
        
        elif "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.exe"
            os.startfile(npath)

        


        

        




    