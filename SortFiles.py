import os
import shutil
import tkinter as tk
from tkinter import filedialog, Text, Label


def browse_button():
    global folder_path
    folder_path = filedialog.askdirectory()
    label = Label(root, text=folder_path).grid(row=1, column=3)


def Sort():
    list_ = os.listdir(folder_path)

    for file_ in list_:
        name, ext = os.path.splitext(file_)

        ext = ext[1:]

        if ext == '':
            continue

        if os.path.exists(folder_path + '/' + ext):
            shutil.move(folder_path + '/' + file_, folder_path + '/' + ext + '/' + file_)

        else:
            os.makedirs(folder_path + '/' + ext)
            shutil.move(folder_path + '/' + file_, folder_path + '/' + ext + '/' + file_)



# GUI

root = tk.Tk()
root.lift
root.title("Sort Files")
root.minsize(300, 100)
browseB = tk.Button(root, text="Browse", command=browse_button, height=1, width=7).grid(row=1, column=1, padx=5, pady=5)
labelN = tk.Label(root, text="Location to sort: ").grid(row=1, column=2)
startB = tk.Button(root, text="Start", command=Sort, height=1, width=7).grid(row=3, column=1, padx=5, pady=5)
root.mainloop()