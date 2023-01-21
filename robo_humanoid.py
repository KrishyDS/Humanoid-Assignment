import speech_recognition as sr
import pyttsx3
import os
import tkinter as tk
from queue import Queue
import threading

#creating class
class VoiceModel:
    def __init__(self, gui):
        self.r = sr.Recognizer()
        self.keyword = "robo"
        self.gui = gui

    def listen(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=0.2) ## adjusting for noise
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio) ## using google's speech recognition engine for Text to speech
                if self.keyword in text:
                    self.gui.update_text(text)
                    self.speak(text)
            except:
                self.gui.update_text("Sorry, I didn't understand what you said.")

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

class VoiceModelGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Voice Model GUI")
        self.geometry("300x200")
        self.listen_button = tk.Button(self, text="Listen", command=self.start_listening)
        self.listen_button.pack()
        self.listen_label = tk.StringVar()
        tk.Label(self, textvariable=self.listen_label).pack()

    def start_listening(self):
        self.listen_button.config(state="disabled")
        self.listen_label.set("Listening...")
        thread = threading.Thread(target=voice_model.listen)
        thread.start()

    def update_text(self, text):
        self.listen_label.set(text)
        self.listen_button.config(state="normal")

voice_model = VoiceModel(VoiceModelGUI())
gui = VoiceModelGUI()
gui.mainloop()