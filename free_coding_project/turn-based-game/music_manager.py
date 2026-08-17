import pygame



class MusicManager:

    def __init__(self, music_path):
        # 1. Initialize the mixer
        pygame.mixer.init()

        # 2. Load the MP3 file
        pygame.mixer.music.load(music_path)

        # 3. Set the volume (optional, value from 0.0 to 1.0)
        #pygame.mixer.music.set_volume(0.7)

        # 4. Start playing the song

    def start_music(self):
        pygame.mixer.music.play()

    def end_music(self):
        pygame.mixer.music.stop()

    def sound_effect(self):
        pygame.mixer.Sound("music/Hurt.wav").play()