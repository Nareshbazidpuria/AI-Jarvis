import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
        
    else:
        speak("Good Evening Sir!")
        
    speak('I am Jarvis, Please tell me how may I help you.')
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening ...')
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print('Recognizing ...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except:
        speak('Sorry Sir, I did not understand. please say that again please ...')
        return 'None'
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia ...')
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences = 2)
                results = results.encode('utf-8')
                speak('Acording to Wikipedia')
                speak(results)
            except:
                speak("Sir, it's not in wikipedia, please try another")
        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com/')
        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')
        elif 'naresh' in query:
            webbrowser.open('https://nareshbazidpuria.github.io/NB-React/')
        elif 'play music' in query:
            music_dir = "C:\\Users\\Naresh Bazidpuria\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[20]))
        elif 'hello jarvis' in query:
            speak('Hello Sir , how may I help you')
        elif 'hi jarvis' in query:
            speak('Hello Sir , how may I help you')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")
        elif 'quit' in query:
            speak('Okay sir , quiting')
            exit()