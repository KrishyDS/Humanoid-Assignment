import speech_recognition as sr
import pyttsx3
import os

#creating class object
class VoiceModel:
    def __init__(self):
        self.r = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=0.2) ## adjusting for noise
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio) ## using google's speech recognition engine for Text to speech
                return text
            except:
                return "Sorry, I didn't understand what you said."

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
