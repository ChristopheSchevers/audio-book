import tkinter as tk
from tkinter import filedialog
from AudiobookConverter import AudiobookConverter

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
    selected_value = slider_var.get()
    audiobook = AudiobookConverter(filename_entry.get(), folder_entry.get())
    audiobook.convert()

    # print("Filename:", filename_entry.get())
    # print("Voice:", selected_voice)
    # print("Slider Value:", selected_value)
    # print("Target Folder:", folder_entry.get())

# Create the main window
root = tk.Tk()
root.title("Data Entry Form")

# Filename entry
filename_label = tk.Label(root, text="Filename:")
filename_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")
filename_entry = tk.Entry(root, width=30)
filename_entry.grid(row=0, column=1, padx=10, pady=5)

# File upload button
upload_button = tk.Button(root, text="Upload File", command=on_file_upload)
upload_button.grid(row=0, column=2, padx=10, pady=5)

# Folder selection entry
folder_label = tk.Label(root, text="Target Folder:")
folder_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
folder_entry = tk.Entry(root, width=30)
folder_entry.grid(row=1, column=1, padx=10, pady=5)

# Folder select button
folder_button = tk.Button(root, text="Select Folder", command=on_folder_select)
folder_button.grid(row=1, column=2, padx=10, pady=5)

# Voice selection dropdown
voice_label = tk.Label(root, text="Voice:")
voice_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")
voice_options = ["Default", "Male", "Female"]
voice_var = tk.StringVar(root)
voice_var.set(voice_options[0])
voice_dropdown = tk.OptionMenu(root, voice_var, *voice_options)
voice_dropdown.grid(row=2, column=1, padx=10, pady=5)

# Slider
slider_label = tk.Label(root, text="Speed:")
slider_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")
slider_var = tk.IntVar(root)
slider = tk.Scale(root, variable=slider_var, from_=0, to=150, orient=tk.HORIZONTAL, length=200)
slider.set(130)
slider.grid(row=3, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()