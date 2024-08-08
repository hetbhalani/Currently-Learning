import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
microphone = sr.Microphone()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("initializing jarvis...")
    
    while True:
        with microphone as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=2)
        
        print("Recognizing...")
        try:
            command = recognizer.recognize_google(audio)
            print(command)
            # Add your command processing logic here
            
            # Example: Exit the loop if the command is "exit"
            if command.lower() == "exit":
                break
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error with the speech recognition service; {0}".format(e))

    speak("Shutting down jarvis...")