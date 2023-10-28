import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('listing')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('recognizing...')
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print('not understand...')

def convert(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    rate = engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':
    data1 = voice().lower()
    if "your name" in data1:
        name = "my name is akash"
        convert(name)
