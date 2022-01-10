import tkinter as tk
import fnmatch
import os
from tkinter.constants import  ACTIVE, ANCHOR, END
from pygame import mixer
from tkinter import filedialog

import pygame
from pygame.music import pause


root = tk.Tk()
root.title("Casette MP3 Çalar")
root.iconbitmap('casettev2.ico')
root.geometry("640x480")
root.config(bg = "gray")

pygame.mixer.init()

def sarkilar_birçok_ekle():
     sarki = filedialog.askopenfilename(initialdir='audio/', title="Şarkı seç", filetypes=(("mp3 Files", "*.mp3"), ))

def sarki_ekle():
    sarki = filedialog.askopenfilename(initialdir='audio/', title="Şarkı seç", filetypes=(("mp3 Files", "*.mp3"), ))
    sarki = sarki.replace("C:/Users/baris/Desktop/", "")
    sarki = sarki.replace(".mp3", "")
    
    liste.insert(END, sarki)


   


    for sarki in sarkilar:
        sarki = sarki.replace("C:/Users/baris/Desktop/", "")
        sarki = sarki.replace(".mp3", "")

        liste.insert(END, sarki)


def play():
    sarki = liste.get(ACTIVE)
    sarki = f'C:/Users/baris/Desktop/{sarki}.mp3'

    pygame.mixer.music.load(sarki)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    liste.selection_clear(ACTIVE)


global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:

         pygame.mixer.music.unpause()
         pasused = False
    else:

    pygame.mixer.music.pause()    
    paused = True
     


liste = tk.Listbox(root, bg="black" , fg="white" ,height= 20, width=160, selectbackground="gray", selectforeground="white")
liste.pack(pady=20)

geri_t = tk.PhotoImage(file= 'reverse 50x50.png')
ileri_t = tk.PhotoImage(file= 'forward 50x50.png')
oynat_t = tk.PhotoImage(file= 'play button 50x50.png')
durdur_t = tk.PhotoImage(file= 'pause 50x50 remake.png')

kontrl_pan = tk.Frame(root, bg="gray")
kontrl_pan.pack()

geri = tk.Button(kontrl_pan, bg="gray", image=geri_t, borderwidth= 0, width= 50, height= 50,)
ileri = tk.Button(kontrl_pan, image=ileri_t, bg= "gray", borderwidth= 0, width= 50, height= 50)
oynat = tk.Button(kontrl_pan, image=oynat_t, bg="gray", borderwidth= 0, width= 50, height= 50, command= play)
durdur = tk.Button(kontrl_pan, image=durdur_t, bg="gray", borderwidth= 0, width= 50, height= 50)


geri.grid(row=0, column=0, padx=10)
ileri.grid(row=0, column=3, padx=10)
oynat.grid(row=0, column=1, padx=10)
durdur.grid(row=0, column=2, padx=10)

my_menu = tk.Menu(root)
root.config(menu=my_menu)

add_song_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Şarkı ekle", menu=add_song_menu)
add_song_menu.add_command(label="Bir şarkı ekle", command=sarki_ekle)

add_song_menu.add command(label="Birçok şarkılar ekle", command=sarkilar_birçok_ekle)


root.mainloop()  