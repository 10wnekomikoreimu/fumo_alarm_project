from playsound import playsound
import random
import os


class IOCtl():
    def __init__(self):
        self.sound_path="./sound"
        self.random_path="./random"
        self.sound_list=os.listdir(self.random_path)
        
    def play_sound(self,audio_file):
        #print("playing: ", audio_file)
        audio_file=self.sound_path+"/"+audio_file
        playsound(audio_file)
        
    def play_random(self):
        random_number = random.randint(0, len(self.sound_list)-1)
        audio_file=self.sound_list[random_number]
        #print("playing: ", audio_file)
        audio_file=self.random_path+"/"+audio_file
        playsound(audio_file)
