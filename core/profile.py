from core.rhythm_generator import RhythmGenerator
from core.melody_generator import MelodyGenerator

class Profile():
    
    def __init__(self, name):
        """Represents a single instrument profile."""
        
        self.name = name
        self.rhythm_gen = RhythmGenerator
        self.melody_gen = MelodyGenerator
        