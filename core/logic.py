from core.profilemanager import ProfileManager
from core.midi import Midi
from core.databasemanager import DatabaseManager
from core.chord_generator import ChordGenerator
from PyQt4 import QtCore

class Logic():
    
    def __init__(self, BPM, bar_division):
        """Keeps the program running and delegates tasks to sub-classes."""
        
        self.profile_manager = ProfileManager(self)
        self.midi = Midi(4)
        self.database_manager = DatabaseManager()
        self.chord_generator = ChordGenerator()
        
        self.profile_manager.add_profile("Profile1", 1)
        self.profile_manager.add_profile("Profile2", 2)
        
        self.bar_division = bar_division  # tells how many frames one bar is broken into
        self.set_BPM(BPM)
        self.playlist = self.get_empty_playlist()
     
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.next_frame) 
        self.frame = self.bar_division
        self.bar = 3
        self.timer.start(self.frame_length * 1000)
        
    def set_BPM(self, BPM):
        """Sets the BPM and calculates the length of a bar and a frame."""
                       
        self.BPM = BPM
        self.bar_length = 60 / self.BPM
        self.frame_length = self.bar_length / self.bar_division
        
    def set_timer_interval(self):
        
        self.timer.setInterval(self.frame_length * 1000)    
        
    def next_frame(self):
        """Moves to the next frame in the main playlist."""
        
        # create new chords every four bars
        if self.bar == 3 and self.frame == self.bar_division:
            self.next_chords = self.chord_generator.generate_next_chords()
            self.frame = 0
            self.bar = -1
            self.chord_idx = 0
        
        # get profiles' playlists after every bar
        if self.frame % self.bar_division == 0:
            self.playlist = self.get_empty_playlist()
            self.playlist = self.get_playlists(self.next_chords[self.chord_idx])
            self.chord_idx += 1
            self.bar += 1
            self.frame = 0
            print("The playlist for the next bar: " + str(self.playlist))
        
        self.send_midi_notes(self.frame)
        
        print("Frame: " + str(self.frame) + " Bar: " + str(self.bar))
        self.frame += 1
        
    def get_playlists(self, chord):
        """Gets the playlist for the next bar from each of the profiles."""
        
        for profile in self.profile_manager.profiles:
            
            tmp_playlist = profile.get_playlist(chord)
            self.playlist = self.merge_playlists(self.playlist, tmp_playlist)
            
        return self.playlist
            
    def merge_playlists(self, playlist1, playlist2):
        """Merges two playlists and returns them in one."""
        
        for index, item in enumerate(playlist2):
            playlist1[index].append(item)
        
        return playlist1
    
    def send_midi_notes(self, frame):
        """Sends the individual MIDI notes of the current frame to Midi class."""
        
        for note in self.playlist[frame]:
               
            if note is not "0":
                channel, note, length, velocity = self.decode(note)
                self.midi.play_note(channel, note, length, velocity)
            
    def decode(self, note):
        """Decodes a note.
        
        @type note: str in format: CHN-NOTE-LEN-VEL eg. 1-50-16-65
        @rtype: int, int, int, int
        """

        parts = note.split("-")
        return int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
      
    def get_empty_playlist(self):
        """Returns an empty list of lists corresponding to the bar_division value."""
        
        return [[] for i in range(self.bar_division)]
         
    