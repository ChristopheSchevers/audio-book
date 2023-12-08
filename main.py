import pyttsx3
import PyPDF2

with open('dummy.pdf', 'rb') as book:
    reader = PyPDF2.PdfReader(book)

    engine = pyttsx3.init()
    engine.setProperty("rate", 100)

    for page in range(len(reader.pages)):
        next_page = reader.pages[page]
        content = next_page.extract_text()

        engine.say(content)
        engine.runAndWait()