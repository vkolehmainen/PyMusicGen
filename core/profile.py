from core.rhythm_generator import RhythmGenerator
from core.melody_generator import MelodyGenerator
import random

class Profile():
    
    def __init__(self, name, channel):
        """Represents a single instrument profile."""
        
        self.name = name
        self.rhythm_gen = RhythmGenerator
        self.melody_gen = MelodyGenerator
        self.channel = channel
        
    def get_playlist(self, chord):
        """Builds the playlist for this profile using the rhythm and melody generators."""
              
        # temporary notes for testing
        
        "SYNTAX: CHN-NOTE-LEN-VEL eg. 1-50-16-65"
    
        chn = 1
        note = random.randint(40,60)
        len = random.randint(1,4)
        vel = random.randint(40,80)
        
        note_str = str(chn) + "-" + str(note) + "-" + str(len) + "-" + str(vel)
        lst = [note_str, "0", "0", "0"]
             
        return lst
     
                
        """" TEMPORARY TEST LISTS
        lsts = [
                [0, 0, "1-C3-16-60", 0],
                ["2-D5-4-77", "3-D2-8-60", 0, 0],
                [0, 0, 0, "3-F2-16-80"],
                [0, "1-C1-2-65", 0, 0]
                ]
        """