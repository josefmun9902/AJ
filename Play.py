import pygame
import time
import os
from tkinter import *

root = Tk()
root.title("AJ - Automated Jockey")
# root.iconbitmap()
# change
root.geometry("400x400")

pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2**12)

global chan_num
chan_num = 0
channel_queue = []
sound_queue = []


def add_song_to_queue(song_name, chan_num):
    sound_queue.append(pygame.mixer.Sound("mp3\\" + song_name + "-m.mp3"))
    channel_queue.append(pygame.mixer.Channel(chan_num))
    channel_queue[chan_num].set_volume(1.0)


# Populate the playlist
queue = []
playlist = open('C:\\Users\\josef\\Downloads\\Playlist.txt', 'r')
queue = playlist.readlines()
playlist.close()

for song in queue:
    song = song.replace("\n", "")
    print(song)
    add_song_to_queue(song, chan_num)
    chan_num += 1

first = True
first2 = True

channel_queue[0].play(sound_queue[0])

for i in range(len(channel_queue)):
    start = time.time()
    if i > 0:
        start -= 10

    volume1 = 1.03
    volume2 = 0.0

    while(channel_queue[i].get_busy()):
        end = time.time()

        delta_time = end - start
        print(delta_time)
        if(delta_time >= 20 and delta_time < 21 and first2):
            channel_queue[i+1].play(sound_queue[i+1])
            channel_queue[i+1].set_volume(0.0)
            first2 = False
        if(delta_time >= 21):
            volume1 -= 0.1
            channel_queue[i].set_volume(volume1)

            volume2 += 0.1
            channel_queue[i +
                          1].set_volume(volume2)

            pygame.time.wait(1000)
    first2 = True
