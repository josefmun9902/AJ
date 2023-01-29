from pychorus import find_and_output_chorus
from pydub import AudioSegment
import pygame
import os
import time

channel_num = 2

# Populate the database with the songs that we have saved
database = open("songs.txt", "w")
for filename in os.listdir("mp3"):
    # Set the song and modified song names
    current_song = "mp3\\" + filename
    current_song_m = current_song[:current_song.find(".")] + "-m.mp3"
    # Check if the song has already been cut
    if not os.path.exists(current_song_m) and not current_song[current_song.find("-"):] == "-m.mp3":
        # Get the value for the chorus start
        chorus_start_sec = find_and_output_chorus(
            current_song, current_song_m, 15)
        os.remove(current_song_m)
        # Change database value to a proportion of the song
        chorus_end_sec = chorus_start_sec + 30
        database.write(filename + " " + str(chorus_start_sec) +
                       " " + str(chorus_end_sec) + "\n")
        # Output the preprocessed motion
        print(current_song)
        sound = AudioSegment.from_mp3(current_song)
        start_time = chorus_start_sec*1000
        end_time = chorus_end_sec*1000
        extract = sound[start_time:end_time]
        extract.export(current_song_m, format="mp3")

database.close()

# pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2**12)

# channel1 = pygame.mixer.Channel(0)
# channel2 = pygame.mixer.Channel(1)

# sound1 = pygame.mixer.Sound("mp3\VirgosGroove.mp3")
# sound2 = pygame.mixer.Sound("mp3\Despacito.mp3")


# channel2.play(sound2)

# channel1.set_volume(1.0)
# channel2.set_volume(0.0)

# volume = 1.0
# volume2 = 0.0
# length = 100000

# queue_channels = []
# queue_sounds = []


# def transition_between_songs(channel1, channel2, wait_time):
#     if(volume < 0):
#         channel1.set_volume(0.0)
#         # channel1 = pygame.mixer.Sound("Runaway.mp3")
#     if(volume > 0):
#         channel1.set_volume(volume)
#         volume -= 0.1
#         pygame.time.wait(wait_time)
#     if(volume < .15 and volume2 < 1):
#         channel2.set_volume(volume2)
#         volume2 += 0.15
#         pygame.time.wait(wait_time)
#     if(volume2 >= 1):
#         channel2.set_volume(volume2)
#         volume2 -= .15
#         pygame.time.wait(wait_time)
#     if(volume2 > .85 and volume < .15):
#         channel1.set_volume(volume)
#         volume += .15
#         pygame.time.wait(wait_time)
#     pygame.time.Clock().tick()


# pygame.mixer.set_num_channels(20)


# def add_song_to_queue(song_name):
#     new_sound = pygame.mixer.Sound(song_name)
#     queue_channels.append(new_channel)
#     queue_sounds.append(new_sound)
#     channel_num += 1


# def pip_song():
#     channel = queue_channels[0]
#     sound = queue_sounds[0]
#     del queue_channels[0]
#     del queue_sounds[0]
#     return channel, sound


# playing = 0  # 0 for channel 1 and 1 for channel 2

# add_song_to_queue("VirgosGroove-m.mp3")
# add_song_to_queue("Despacito-m.mp3")
# add_song_to_queue("Runaway-m.mp3")

# while True:
#     if playing == 0:
#         seconds = time.time()
#         pygame.mixer.find_channel().play(sound1)

#         while channel1.get_busy():
#             if(seconds >= 20):
#                 transition_between_songs(channel1, channel2, 1000)
#         channel1, sound1 = pip_song()
#         playing = 1
#     if playing == 1:
#         seconds = time.time()
#         channel2.play(sound2)

#         while channel2.get_busy():
#             if seconds >= 20:
#                 transition_between_songs(channel2, channel1, 1000)
#         channel2, sound2 = pip_song()
#         playing = 0


# while channel1.get_busy() or channel2.get_busy():
#     pygame.time.wait(2000)

#     print(volume)
#     print(volume2)
#     if(volume < 0):
#         channel1.set_volume(0.0)
#         # channel1 = pygame.mixer.Sound("Runaway.mp3")
#         chanel1 = queue_sounds[0]

#     if(volume > 0):
#         channel1.set_volume(volume)
#         volume -= 0.1
#         pygame.time.wait(1000)
#     if(volume < .15 and volume2 < 1):
#         channel2.set_volume(volume2)
#         volume2 += 0.15
#         pygame.time.wait(1000)
#     if(volume2 >= 1):
#         channel2.set_volume(volume2)
#         volume2 -= 15
#         pygame.time.wait(1000)
#     if(volume2 > .85 and volume < .15):
#         channel1.set_volume(volume)
#         volume += .15
#         pygame.time.wait(1000)
#     pygame.time.Clock().tick()
