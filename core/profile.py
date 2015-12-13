from core.rhythm_generator import RhythmGenerator
from core.melody_generator import MelodyGenerator

class Profile():
    
    def __init__(self, name, channel):
        """Represents a single instrument profile."""
        
        self.name = name
        self.rhythm_gen = RhythmGenerator
        self.melody_gen = MelodyGenerator
        self.channel = channel
        
    def get_playlist(self, chord):
        """Builds the playlist for this profile using the rhythm and melody generators."""
              
        return "playlist"
        