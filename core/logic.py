from core.profilemanager import ProfileManager
from core.midi import Midi
from core.databasemanager import DatabaseManager
from core.chord_generator import ChordGenerator
from PyQt4 import QtCore

class Logic():
    
    def __init__(self):
        """Keeps the program running and delegates tasks to sub-classes."""
        
        self.profile_manager = ProfileManager()
        self.midi = Midi(0)
        self.database_manager = DatabaseManager()
        self.chord_generator = ChordGenerator()
        
        self.set_BPM(60)
        self.bar_division = 16  # tells how many frames one bar is broken into
        
        self.timer = QtCore.QTimer() 
        self.timer.timeout.connect(self.next_frame) 
        self.frame = self.bar_division * 4
        self.timer.start(self.frame_length * 1000)
        
    def set_BPM(self, BPM):
        """Sets the BPM and calculates the length of a bar and a frame."""
                       
        self.BPM = BPM
        self.bar_length = 60 / self.BPM
        self.frame_length = self.bar_length / self.bar_division       
        
    def next_frame(self):
        """Moves to the next frame in the main playlist."""
        
        # create new chords every four bars
        if self.frame == self.bar_division * 4:
            self.next_chords = self.chord_generator.generate_next_chords()
            self.frame = 0
            self.chord_idx = 0
        
        # get profiles' playlists after every bar
        if self.frame % self.bar_division == 0:         
            self.playlist = self.get_playlists(self.next_chords[self.chord_idx])
            self.chord_idx += 1
        
        self.send_midi_notes(self.frame)
        
        self.frame += 1
        
    def get_playlists(self, chord):
        """Gets the playlist for the next bar from each of the profiles."""
        
        for profile in self.profile_manager.profiles:
            pass
            
    def merge_playlists(self):
        """Merges playlists of different instruments and returns them in one list."""
        
        pass
    
    def send_midi_notes(self, frame):
        """Sends the individual MIDI notes of the current frame to Midi class."""
        
        for note in self.playlist[frame]:    
            channel, note, length, velocity = self.decode(note)
            self.midi.play_note(channel, note, length, velocity)
            
    def decode(self, note):
        """Decodes a note.
        
        @type note: str in format: CHN-NOTE-LEN-VEL eg. 1-50-16-65
        @rtype: int, int, int, int
        """
        
        return "channel, note, length, velocity"
         
    