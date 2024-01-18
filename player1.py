from tkinter import Tk, PhotoImage, END, Menu, Listbox, Frame, Button
# from tkinter import *
from tkinter import filedialog
# import pygame
from pygame import mixer

from os import listdir, path

import tkinter.messagebox as tmsg

window = Tk()
window.title('Amogh\'s music player')
window.geometry("500x325+100+100")
window.resizable(False, False)

icon = PhotoImage(file='logo.png')
window.iconphoto(False, icon)

mixer.init()

playlist=[]
paused = False

def loadsong():
    global current_song
    window.directory = filedialog.askdirectory()

    for song in listdir(window.directory):
        name, ext = path.splitext(song)
        if ext=='.mp3':
            playlist.append(song)
            songlist.insert("end", song)
        
    songlist.selection_set(0)
    current_song = playlist[songlist.curselection()[0]]

def playsong():
    global current_song, paused

    if paused:
        mixer.music.unpause()
        paused = False
    else:
        current_song = playlist[songlist.curselection()[0]]
        mixer.music.load(path.join(window.directory, current_song))
        mixer.music.play()

def pausesong():
    global paused
    mixer.music.pause()
    paused = True

def nextsong():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(playlist.index(current_song) + 1)
        current_song = playlist[songlist.curselection()[0]]
        playsong()
    except:
        pass

def prevsong():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(playlist.index(current_song) - 1)
        current_song = playlist[songlist.curselection()[0]]
        playsong()
    except:
        pass

def about():
    tmsg.showinfo("About the player",
                  "This player has been made as a small learning project.\n\nThe player has been made using the OS, Tkinter and Pygame modules in python")

menubar = Menu(window)
window.config(menu = menubar)

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=loadsong)
organise_menu.add_command(label='About', command=about)
menubar.add_cascade(label='Menu', menu=organise_menu)

songlist= Listbox(window, bg="#222222", fg="white",
                  width=100, height=13, font=12, activestyle="none", selectbackground="Green")
songlist.pack()

play = PhotoImage(file='play.png')
pause = PhotoImage(file='pause.png')
prev = PhotoImage(file='prev.png')
next = PhotoImage(file='next.png')

buttonframe = Frame(window)
buttonframe.pack()

play_btn = Button(buttonframe, image=play, borderwidth=0, command=playsong)
pause_btn = Button(buttonframe, image=pause, borderwidth=0, command=pausesong)
prev_btn = Button(buttonframe, image=prev, borderwidth=0, command=prevsong)
next_btn = Button(buttonframe, image=next, borderwidth=0, command=nextsong)

play_btn.grid(padx=7, pady=5, row=0, column=1)
pause_btn.grid(padx=7, pady=5, row=0, column=2)
prev_btn.grid(padx=7, pady=5, row=0, column=0)
next_btn.grid(padx=7, pady=5, row=0, column=3)

window.mainloop()