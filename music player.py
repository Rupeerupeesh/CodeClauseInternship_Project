import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
music_player = tkr.Tk()
music_player.title("melody music player")
music_player.geometry("500x400")
directory= askdirectory()
os.chdir(directory)
song_list=os.listdir()
play_list=tkr.Listbox(music_player, font="Roman",bg='blue', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
Button1= tkr.Button(music_player,width=6,height=3,font="Roman",text="PLAY",command=play,bg="green",fg="white")
Button2= tkr.Button(music_player,width=6,height=3,font="roman",text="STOP",command=stop,bg="black",fg="white")
Button3= tkr.Button(music_player,width=6,height=3,font="Roman",text="PAUSE",command=pause,bg="red",fg="white")
Button4= tkr.Button(music_player,width=6,height=3,font="Roman",text="UNPAUSE",command=unpause,bg="orange",fg="white")
var = tkr.StringVar()
song_title = tkr.Label(music_player,font="Roman",textvariable=var)
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both",expand="yes")
music_player.mainloop()   
