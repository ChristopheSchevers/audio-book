import pyttsx3
import PyPDF2
import os
from pathlib import Path

class AudiobookConverter:
    def __init__(self, target, path='', rate=140, voice=''):
        self.target = target
        self.path = path if path else str(Path.home() / 'Downloads')
        self.rate = rate
        self.voice = voice
        self.filename = 'audiobook.mp3'
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", self.rate)

        if self.voice:
            self.engine.setProperty("voice", self.voice)

    def convert(self):
        if not self.target:
            return False
        with open(self.target, 'rb') as book:
            reader = PyPDF2.PdfReader(book)

            for page in range(len(reader.pages)):
                next_page = reader.pages[page]
                content = next_page.extract_text()
                file_path = os.path.join(self.path, self.filename)
                file_path = file_path.replace('\\','/')
                self.engine.save_to_file(content, file_path)
                self.engine.say(content)
            
            self.engine.runAndWait()

    def getVoicesDict(self):
        voices = self.engine.getProperty('voices')
        return {voice.name: voice.id for voice in voices}

    def setVoice(self, name):
        if name == "":
           return name
        
        voices = self.getVoicesDict()
        return self.engine.setProperty('voice', voices[name])

    def setRate(self, rate):
        self.rate = rate
        return self.engine.setProperty('rate', self.rate)