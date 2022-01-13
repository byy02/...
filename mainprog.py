import tkinter as tk
import fnmatch
import os
from tkinter.constants import  ACTIVE, ANCHOR, BOTTOM, END, GROOVE, HORIZONTAL, VERTICAL, W, X
from pygame import mixer
from tkinter import Frame, Label, filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

import pygame



root = tk.Tk()
root.title("Casette MP3 Çalar")
root.iconbitmap('casettev2.ico')
root.geometry("1280x720")
root.config(bg = "gray")

pygame.mixer.init()


def oynatma_süresi():
    if stopped:
        return

    anlik_sarki= liste.curselection()
    sarki = liste.get(anlik_sarki)
    

    sarki = f'C:/Users/baris/Desktop/{sarki}.mp3'
    song_mut = MP3(sarki)

    global sarki_uzunlugu
    sarki_uzunlugu = song_mut.info.length

    don_uzunlugu = time.strftime('%H:%M:%S', time.gmtime(sarki_uzunlugu))

    anlik_süre = pygame.mixer.music.get_pos() / 1000
    status_bar.config(text=anlik_süre)
    sarki_süresi = time.strftime('%H:%M:%S', time.gmtime(anlik_süre))
    anlik_süre +=1
    
    if int(slider.get()) == int(sarki_uzunlugu):
        status_bar.config(text=f'{don_uzunlugu} / {don_uzunlugu} ')
    
    elif paused:
        pass


    
    elif int(slider.get()) == int(anlik_süre):
        slider_position = int(sarki_uzunlugu)
        slider.config(to= slider_position, value = int(anlik_süre))
    
    else:
        slider_position = int(sarki_uzunlugu)
        slider.config(to= slider_position, value = int(slider.get()))
        status_bar.config(text=f'{sarki_süresi} / {don_uzunlugu} ')
        sarki_süresi = time.strftime('%H:%M:%S', time.gmtime(int(slider.get())))
        sonraki_süre = int(slider.get()) + 1
        slider.config(value = sonraki_süre) 
    #status_bar.config(text=f'{sarki_süresi} / {don_uzunlugu} ')
    #slider.config(value = int(anlik_süre))
    
    status_bar.after(1000, oynatma_süresi)
    
       

  


def sarki_ekle():
    sarki = filedialog.askopenfilename(initialdir='audio/', title="Şarkı seç", filetypes=(("mp3 Files", "*.mp3"), ))
    sarki = sarki.replace("C:/Users/baris/Desktop/", "")
    sarki = sarki.replace(".mp3", "")
    
    liste.insert(END, sarki)



global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False

    else:
        pygame.mixer.music.pause()
        paused = True



def play():
    global stopped
    stopped = False
    sarki = liste.get(ACTIVE)
    sarki = f'C:/Users/baris/Desktop/{sarki}.mp3'

    pygame.mixer.music.load(sarki)
    pygame.mixer.music.play(loops=0)

    oynatma_süresi()
    #slider_position = int(sarki_uzunlugu)
    #slider.config(to= slider_position, value = 0)

def sonraki_sarki():
    status_bar.config(text='')
    slider.config(value=0)
    sonraki= liste.curselection()
    sonraki= sonraki[0]+1
    sarki = liste.get(sonraki)
    print(sarki)
    sarki = f'C:/Users/baris/Desktop/{sarki}.mp3'

    pygame.mixer.music.load(sarki)
    pygame.mixer.music.play(loops=0)

    liste.selection_clear(0, END)
    liste.activate(sonraki)
    liste.selection_set(sonraki, last=None)


def önceki_sarki():
    status_bar.config(text='')
    slider.config(value=0)
    önceki = liste.curselection()
    önceki=önceki[0]-1
    sarki = liste.get(önceki)
    print(sarki)
    sarki = f'C:/Users/baris/Desktop/{sarki}.mp3'

    pygame.mixer.music.load(sarki)
    pygame.mixer.music.play(loops=0)

    liste.selection_clear(0, END)
    liste.activate(önceki)
    liste.selection_set(önceki, last=None)

def sarki_sil():
    stop()
    liste.delete(ANCHOR)
    pygame.mixer.music.stop()


def liste_temizle():
    stop()
    liste.delete(0, END)
    pygame.mixer.music.stop()


global stopped
stopped = False
def stop():

    status_bar.config(text='')
    slider.config(value=0)

    pygame.mixer.music.stop()
    liste.selection_clear(ACTIVE)
    status_bar.config(text='')

    global stopped
    stopped = True


def slide(X):
    
    #slider_label.config(text=f'{int(slider.get())} / {int(sarki_uzunlugu)}')
    sarki = liste.get(ACTIVE)
    sarki = f'C:/Users/baris/Desktop/{sarki}.mp3'

    pygame.mixer.music.load(sarki)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))

def ses(X):
    pass


master_frame = tk.Frame(root, bg="gray")
master_frame.pack(pady=20)

liste = tk.Listbox(master_frame, bg="black" , fg="white" ,height= 20, width=140, selectbackground="gray", selectforeground="white")
liste.grid(row=0, column=0)

geri_t = tk.PhotoImage(file= 'reverse 50x50.png')
ileri_t = tk.PhotoImage(file= 'forward 50x50.png')
oynat_t = tk.PhotoImage(file= 'play button 50x50.png')
durdur_t = tk.PhotoImage(file= 'pause 50x50 remake.png')

kontrl_pan = tk.Frame(master_frame, bg="gray")
kontrl_pan.grid(row=2, column=0, pady=0)

geri = tk.Button(kontrl_pan, bg="gray", image=geri_t, borderwidth= 0, width= 50, height= 50, command= önceki_sarki)
ileri = tk.Button(kontrl_pan, image=ileri_t, bg= "gray", borderwidth= 0, width= 50, height= 50, command = sonraki_sarki)
oynat = tk.Button(kontrl_pan, image=oynat_t, bg="gray", borderwidth= 0, width= 50, height= 50, command= play)
durdur = tk.Button(kontrl_pan, image=durdur_t, bg="gray", borderwidth= 0, width= 50, height= 50, command= lambda: pause (paused))

ses_frame = ttk.LabelFrame(root, text="SES DÜZEYİ")
ses_frame.grid(row=5, column=0)
geri.grid(row=0, column=0, padx=10)
ileri.grid(row=0, column=3, padx=10)
oynat.grid(row=0, column=1, padx=10)
durdur.grid(row=0, column=2, padx=10)

my_menu = tk.Menu(root)
root.config(menu=my_menu)

add_song_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Şarkı ekle", menu=add_song_menu)
add_song_menu.add_command(label="Bir şarkı ekle", command=sarki_ekle)

delete_s_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Şarkı çıkar", menu=delete_s_menu)
delete_s_menu.add_command(label="Oynatma listesinden bir şarkı çıkar", command=sarki_sil)
delete_s_menu.add_command(label="Oynatma listesini temizle", command=liste_temizle)

status_bar = Label(root, text='', bd=0,bg="gray",fg="white", relief=GROOVE, anchor=W)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command= slide, length=800)
slider.grid(row=1, column=0,pady=40)

#slider_label = Label(root, text="0")
#slider_label.pack(pady=10)

ses_slider = ttk.Scale(ses_frame, from_=0, to=1, orient=VERTICAL, value=1, command= ses, length=50)
slider.pack()


root.mainloop()  