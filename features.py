import datetime
import pyttsx3
import speech_recognition as sr
import features as f
import file_handling as fh
import wikipedia


engine = pyttsx3.init('sapi5')      #used to take voices from google
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)   #set the voice
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand(): #it takes input for microphone and returns output or do task
    r = sr.Recognizer()  #helps to recognize the command
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source, timeout=10, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        speak("Say that again please")
        return "None"
    
    return query

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    fh.append_data("./database/history.txt", "VOICY", f"current time is : {time}" )
    print(time)
    f.speak('current time is : ' + time)

def date():
    date = datetime.date.today().strftime("%d/%m/%Y")
    fh.append_data("./database/history.txt", "VOICY", f"Todays date is : + {date}")
    print(date)
    f.speak('Todays date is : ' + date)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    
    elif hour>=12 and hour<18:
        speak("good afternoon sir")

    else: speak("good evening sir")

    speak("I am voicy, How can I help you")

def wikiPedia(query):
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    f.speak("According to wikipedia")
    print(results)
    f.speak(results)
    fh.append_data("./database/history.txt", "VOICY", results)