import pyttsx3
import PyPDF2
import os
from pathlib import Path

home = str(Path.home())
downloads_folder = os.path.join(home, 'Downloads')

class AudiobookConverter:
    def __init__(self, target, path='', rate=140, gender='male'):
        self.target = target
        self.path = path if path else downloads_folder
        self.rate = rate
        self.gender = gender
        self.filename = 'audiobook.mp3'

    def convert(self):
        with open(self.target, 'rb') as book:
            reader = PyPDF2.PdfReader(book)

            engine = pyttsx3.init()
            engine.setProperty("rate", self.rate)

            for page in range(len(reader.pages)):
                next_page = reader.pages[page]
                content = next_page.extract_text()

                # engine.say(content)
                file_path = self.path + '/' + self.filename if self.path else self.filename
                engine.save_to_file(content, file_path)
                engine.runAndWait()