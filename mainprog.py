import tkinter as tk
import fnmatch
import os
from pygame import mixer


root = tk.Tk()
root.title("Casette MP3 Çalar")
root.iconbitmap('')
root.geometry("640x480")
root.config(bg = "black")

mixer.init

root.mainloop()