import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLib
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
microphone = sr.Microphone()
newsAPI = "6ff2882ba17d42229e809add5c68a6de"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/feed/")
    elif "open youtube" in c.lower(): 
        webbrowser.open("https://www.youtube.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ",1)[1]
        link = musicLib.music[song]
        webbrowser.open(link)
    elif "today's news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=6ff2882ba17d42229e809add5c68a6de")

if __name__ == "__main__":
    speak("initializing Alfred...")
    
    while True: 
        print("Listening...")
        try:
            with microphone as source:
                audio = recognizer.listen(source, timeout=2,phrase_time_limit=3)
                word = recognizer.recognize_google(audio)

            if(word.lower() == "alfred"):
                speak("Yes sir!")
                with microphone as source:
                    print("Jarvis Activated!")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)
                            
        except Exception as e:
            print("Error;{0}".format(e))