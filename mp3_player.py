import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

def play():
    pygame.mixer.music.load(play_list.get(tkinter.ACTIVE))
    var.set(play_list.get(tkinter.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

if __name__ == "__main__":
    music_player = tkinter.Tk()
    music_player.title("Lance's MP3 Player")
    music_player.geometry("450x350")

    directory = askdirectory()
    os.chdir(directory)
    song_list = os.listdir()

    play_list = tkinter.Listbox(music_player, font="Helvetica 12 bold", bg="red", selectmode=tkinter.SINGLE)

    for item in song_list:
        pos = 0
        play_list.insert(pos, item)
        pos += 1

    pygame.init()
    pygame.mixer.init()

    Button1 = tkinter.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
    Button2 = tkinter.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
    Button3 = tkinter.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
    Button4 = tkinter.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

    var = tkinter.StringVar()
    song_title = tkinter.Label(music_player,font="Helvetica 12 bold", textvariable=var)

    song_title.pack()
    Button1.pack(fill="x")
    Button2.pack(fill="x")
    Button3.pack(fill="x")
    Button4.pack(fill="x")
    play_list.pack(fill="both", expand="yes")

    music_player.mainloop()
