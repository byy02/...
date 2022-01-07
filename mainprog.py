import tkinter as tk
import fnmatch
import os
from pygame import mixer
from tkinter import filedialog


root = tk.Tk()
root.title("Casette MP3 Çalar")
root.iconbitmap('casettev2.ico')
root.geometry("640x480")
root.config(bg = "gray")

mixer.init()

def sarkı_ekle():
    sarkı = filedialog.askopenfilename(initialdir='audio/',  )


liste = tk.Listbox(root, bg="black" , fg="white" ,height= 20, width=160)
liste.pack(pady=20)

geri_t = tk.PhotoImage(file= 'reverse 50x50.png')
ileri_t = tk.PhotoImage(file= 'forward 50x50.png')
oynat_t = tk.PhotoImage(file= 'play button 50x50.png')
durdur_t = tk.PhotoImage(file= 'pause 50x50 remake.png')

kontrl_pan = tk.Frame(root, bg="gray")
kontrl_pan.pack()

geri = tk.Button(kontrl_pan, bg="gray", image=geri_t, borderwidth= 0, width= 50, height= 50,)
ileri = tk.Button(kontrl_pan, image=ileri_t, bg= "gray", borderwidth= 0, width= 50, height= 50)
oynat = tk.Button(kontrl_pan, image=oynat_t, bg="gray", borderwidth= 0, width= 50, height= 50)
durdur = tk.Button(kontrl_pan, image=durdur_t, bg="gray", borderwidth= 0, width= 50, height= 50)


geri.grid(row=0, column=0, padx=10)
ileri.grid(row=0, column=3, padx=10)
oynat.grid(row=0, column=1, padx=10)
durdur.grid(row=0, column=2, padx=10)

root.mainloop()