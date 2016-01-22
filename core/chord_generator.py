import random

class ChordGenerator():
    
    def __init__(self):
        """Uses Markov's chain to create a probability table and choose chords from it."""
        
        self.order = 1  # markov chain order from 1 to 4
    
    def load_chords(self):
        """Load chords to generator."""
               
        self.table = {}
        
        # An example chord progression, these will be loaded from the progressions.db database in future versions
        chord_tuple = ("C", "G", "Am", "F", "C", "G", "F", "C", "C", "G", "Am", "F", "C", "G", "F", "C", "Am", "Am", "F", "C", "G", "F", "C", "C", "G", "Am", "F", "C", "G", "F", "C", "C", "G", "Am", "F", "C", "G", "F", "C", "Am", "Am", "F", "C", "G", "F", "C", "Am", "Am", "F", "C", "G", "F", "C", "F", "C", "G", "F", "C", "C", "G", "Am", "F", "C", "G", "F", "C", "Am", "Am", "F", "C", "G", "F", "C", "C", "G", "Am", "F", "C", "G", "F", "C", "C", "G", "Am", "F", "C", "G", "F", "C", "Am", "Am", "F", "C", "G", "F", "C", "Am", "Am", "F", "C", "G", "F", "C")
        for i in range(len(chord_tuple) - self.order):
            try:
                self.table[chord_tuple[i:i + self.order]]
            except KeyError:
                self.table[chord_tuple[i:i + self.order]] = []               
                
            new = tuple([chord_tuple[i + self.order]])
                         
            self.table[chord_tuple[i:i + self.order]] += new
        
    def get_next_chords(self, previous_chords = None, max_length = 20):
        """Returns the next four chords."""
        
        """
        if previous_chords == None:
            s = random.choice(list(self.table))
        else:
            s = previous_chords
        try:
            while len(s) < max_length:
                s += random.choice(self.table[s[-self.order:]])
        except KeyError:
            pass
        return s
        """
        
        #dummy return
        return ["C", "Am", "F", "D"]


