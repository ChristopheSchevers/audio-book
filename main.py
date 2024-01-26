import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from AudiobookConverter import AudiobookConverter

audiobook = AudiobookConverter('')

def on_file_upload():
    file_path = filedialog.askopenfilename(title="Select a file")
    filename_entry.delete(0, tk.END)
    filename_entry.insert(0, file_path)

def on_folder_select():
    folder_path = filedialog.askdirectory(title="Select a folder")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def on_submit():
    selected_voice = voice_var.get()
    selected_rate = slider_var.get()
    audiobook.target = filename_entry.get()
    audiobook.path = folder_entry.get()
    audiobook.voice = audiobook.setVoice(selected_voice)
    audiobook.rate = audiobook.setRate(selected_rate)
    audiobook.convert()

# Create the main window
root = ctk.CTk()
root.title("Audio book converter")

frame = ctk.CTkFrame(master=root)
frame.grid(row=0, column=0, padx=20, pady=20, rowspan=5)

# Filename entry
filename_label = ctk.CTkLabel(master=frame, text="Filename:")
filename_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")
filename_entry = ctk.CTkEntry(master=frame)
filename_entry.grid(row=0, column=1, padx=10, pady=5, sticky='nesw')

# File upload button
upload_button = ctk.CTkButton(master=frame, text="Upload File", command=on_file_upload)
upload_button.grid(row=0, column=2, padx=10, pady=5)

# Folder selection entry
folder_label = ctk.CTkLabel(master=frame, text="Target Folder:")
folder_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
folder_entry = ctk.CTkEntry(master=frame)
folder_entry.grid(row=1, column=1, padx=10, pady=5, sticky='nesw')

# Folder select button
folder_button = ctk.CTkButton(master=frame, text="Select Folder", command=on_folder_select)
folder_button.grid(row=1, column=2, padx=10, pady=5)

# Voice selection dropdown
voice_label = ctk.CTkLabel(master=frame, text="Voice:")
voice_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")
voice_options = list(audiobook.getVoicesDict().keys())
voice_var = tk.StringVar(root)
voice_var.set(voice_options[0])
voice_dropdown = ctk.CTkOptionMenu(master=frame, variable=voice_var, values=voice_options)
voice_dropdown.grid(row=2, column=1, padx=10, pady=5)

# Slider
slider_label = ctk.CTkLabel(master=frame, text="Speed:")
slider_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")
slider_var = tk.IntVar(root)
slider = ctk.CTkSlider(master=frame, variable=slider_var, from_=0, to=150, orientation=tk.HORIZONTAL, width=200)
slider.set(130)
slider.grid(row=3, column=1, padx=10, pady=5)

# Submit button
submit_button = ctk.CTkButton(master=frame, text="Submit", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
