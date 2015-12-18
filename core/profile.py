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
        
        lsts = [
                [0, 0, "1-C3-16-60", 0],
                ["2-D5-4-77", "3-D2-8-60", 0, 0],
                [0, 0, 0, "3-F2-16-80"],
                [0, "1-C1-2-65", 0, 0]
                ]
              
              
        return random.choice(lsts)
        