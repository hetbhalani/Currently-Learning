import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
microphone = sr.Microphone()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)

if __name__ == "__main__":
    speak("initializing jarvis...")
    
    while True: 
        print("Listening...")
        try:
            with microphone as source:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)

            if(word.lower() == "jarvis"):
                speak("Yes sir!")
                with microphone as source:
                    print("Jarvis Activated!")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)
                            
        except Exception as e:
            print("Error;{0}".format(e))