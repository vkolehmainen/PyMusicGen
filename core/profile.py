from core.rhythm_generator import RhythmGenerator
from core.melody_generator import MelodyGenerator
import random

class Profile():
    
    def __init__(self, name, channel, profile_manager):
        """Represents a single instrument profile."""
        
        self.name = name
        self.profile_manager = profile_manager
        self.rhythm_gen = RhythmGenerator()
        self.melody_gen = MelodyGenerator()
        self.channel = channel
        
        
    def get_playlist(self, chord):
        """Builds the playlist for this profile using the rhythm and melody generators."""
        
        steps = self.profile_manager.logic.bar_division
        pulses = random.randint(1,5)
        rhythm_list = self.rhythm_gen.bjorklund(pulses, steps)
        
        for index, item in enumerate(rhythm_list):
            if item == 0:
                rhythm_list[index] = "0"
            else:
                rhythm_list[index] = self.get_rand_note()
                   
        "SYNTAX: CHN-NOTE-LEN-VEL eg. 1-50-16-65"
             
        return rhythm_list
        
                
        """" TEMPORARY TEST LISTS
        lsts = [
                [0, 0, "1-C3-16-60", 0],
                ["2-D5-4-77", "3-D2-8-60", 0, 0],
                [0, 0, 0, "3-F2-16-80"],
                [0, "1-C1-2-65", 0, 0]
                ]
        """
        
    def get_rand_note(self):

        chn = 1
        note = random.choice([39, 41, 43, 44, 46, 48, 50, 51, 53, 55, 56, 58, 60, 62])
        len = random.randint(1,4)
        vel = random.randint(30,90)
        
        note_str = str(chn) + "-" + str(note) + "-" + str(len) + "-" + str(vel)
        
        return note_str