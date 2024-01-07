import pyttsx3
import PyPDF2

class AudiobookConverter:
    rate = 140
    gender = 'male'

    def __init__(self, target, path):
        self.target = target
        self.path = path

    def convert(self):
        with open(self.target, 'rb') as book:
            reader = PyPDF2.PdfReader(book)

            engine = pyttsx3.init()
            engine.setProperty("rate", self.rate)

            for page in range(len(reader.pages)):
                next_page = reader.pages[page]
                content = next_page.extract_text()

                engine.say(content)
                engine.runAndWait()