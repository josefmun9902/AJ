from pychorus import find_and_output_chorus
import pygame
import os

# # Populate the database with the songs that we have saved
# database = open("songs.txt", "w")
# for filename in os.listdir("mp3"):
#     # Set the song and modified song names
#     current_song = "mp3/" + filename
#     current_song_m = current_song[:current_song.find(".")] + "-m.mp3"
#     # Get the value for the chorus start
#     chorus_start_sec = find_and_output_chorus(
#         current_song, current_song_m, 15)
#     os.remove(current_song_m)
#     # change to a proportion of the song
#     chorus_end_sec = chorus_start_sec + 30
#     database.write(filename + " " + str(chorus_start_sec) +
#                    " " + str(chorus_end_sec) + "\n")
# database.close()


def change_volume(channel, num):
    channel.set_volume(num-0.01)


pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2**12)
pygame.mixer.set_num_channels(20)

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)

sound1 = pygame.mixer.Sound("mp3\VirgosGroove.mp3")
sound2 = pygame.mixer.Sound("mp3\Despacito.mp3")

channel1.play(sound1)
channel2.play(sound2)
channel1.set_volume(1.0)
channel2.set_volume(0.0)

volume = 1.0
volume2 = 0.0
length = 100000

while channel1.get_busy() or channel2.get_busy():
    pygame.time.wait(2000)

    print(volume)
    print(volume2)
    if(volume < 0):
        channel1.set_volume(0.0)
        # channel1 = pygame.mixer.Sound("mp3\Runaway.mp3")
    if(volume > 0):
        channel1.set_volume(volume)
        volume -= 0.1
        pygame.time.wait(1000)
    if(volume < .15 and volume2 < 1):
        channel2.set_volume(volume2)
        volume2 += 0.15
        pygame.time.wait(1000)
    if(volume2 >= 1):
        channel2.set_volume(volume2)
        volume2 -= 15
        pygame.time.wait(1000)
    if(volume2 > .85 and volume < .15):
        channel1.set_volume(volume)
        volume += .15
        pygame.time.wait(1000)
    pygame.time.Clock().tick()
