import pyttsx3
import PyPDF2
import os
from pathlib import Path

home = str(Path.home())
downloads_folder = os.path.join(home, 'Downloads')

class AudiobookConverter:
    def __init__(self, target, path='', rate=140, gender='male'):
        self.target = target
        self.path = path if path else str(Path.home() / 'Downloads')
        self.rate = rate
        self.gender = gender
        self.filename = 'audiobook.mp3'
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", self.rate)

    def convert(self):
        with open(self.target, 'rb') as book:
            reader = PyPDF2.PdfReader(book)

            for page in range(len(reader.pages)):
                next_page = reader.pages[page]
                content = next_page.extract_text()
                file_path = os.path.join(self.path, self.filename)
                self.engine.save_to_file(content, file_path)
            
            self.engine.runAndWait()