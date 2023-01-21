import tkinter as tk
from queue import Queue

class VoiceModelGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Voice Model GUI")
        self.geometry("300x200")
        self.queue = Queue()
        self.listen_button = tk.Button(self, text="Listen", command=self.listen)
        self.listen_button.pack()
        self.listen_label = tk.Label(self, text="Listening...")
        self.listen_label.pack()
        self.words_label = tk.Label(self, text="")
        self.words_label.pack()

    def listen(self):
        text = voice_model.listen()
        self.words_label.config(text=text)
        self.queue.put(text)

    def speak(self):
        text = self.queue.get()
        voice_model.speak(text)
        self.words_label.config(text="")

    def start(self):
        self.listen_button.config(state="disabled")
        self.listen_label.config(text="Listening...")
        self.after(10000, self.speak)
        self.mainloop()

voice_model = VoiceModel()
gui = VoiceModelGUI()
gui.start()
