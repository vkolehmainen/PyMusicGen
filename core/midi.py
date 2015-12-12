import pygame.midi
import time
import random

pygame.midi.init()

print( "There are " + str(pygame.midi.get_count()) + " MIDI devices")

print("The default input device number is "  +
str(pygame.midi.get_default_input_id()))

print("The default output device number is "  +
str(pygame.midi.get_default_output_id()))

print( "The default input device info is " +
str(pygame.midi.get_device_info(pygame.midi.get_default_input_id())))

print("The default output device info is " +
str(pygame.midi.get_device_info(pygame.midi.get_default_output_id())))

print( "The current time on the PortMidi timer is " +
str(pygame.midi.time()) + " ms")

class Midi():
    """
    INSTRUCTIONS
    
    You need to install PyGame for Python 3.4 to get this module working.
    To send MIDI-messages to a MIDI-player you need loopMIDI. It acts as a virtual MIDI cable.
    
    1. dl/install PyGame: https://bitbucket.org/pygame/pygame/downloads       (pygame-1.9.2a0-hg_ea3b3bb8714a.win32-py3.4.msi confirmed working)
    2. dl/install loopMIDI: http://www.tobias-erichsen.de/software/loopmidi.html
    3. create a port in loopMIDI
    4. check which DEVICE it represents in pygame.midi by calling "" print(pygame.midi.get_device_info(X)) "" with different values
    5. set that as the output device of pygame.midi (in __init__)
    6. map the same port to be the input port of the device (or software synth) of your choice
    
    Python/pygame.midi:  output--->    loopMIDI    --->input: some MIDI player    
    """
     
    def __init__(self):
        """Sends MIDI note commands to the output device."""
        
        # This will vary depending on your other MIDI devices
        self.output = pygame.midi.Output(5)
        
        # Some queue structure that the note_off commands will be sent to
        self.queue = ""
        
    def play_chord(self, chord):
        """A METHOD FOR TESTING PURPOSES ONLY, NOT INTENDED TO BE IN LATER VERSIONS."""
        #Settings are optimized for chords with a long release time
        self.output.note_on(note, 50)
        self.output.note_on(note + chord[0], 50)
        self.output.note_on(note + chord[1], 50)
        if len(chord) > 2:
            self.output.note_on(note + chord[2], 50)
        
        time.sleep(random.randint(2,3))
        
        self.output.note_off(note)
        self.output.note_off(note + chord[0])
        self.output.note_off(note + chord[1])
        
        if len(chord) > 2:
            self.output.note_off(note + chord[2])
            
    def play_note(self, profile, note, length, velocity):
        """Sends a note_on command and pushes the note_off command to the queue.
        
        @param profile: the instrument profile that plays the note
        @type profile: core.Profile
        
        @param note: MIDI note number
        @type note: int
        
        @param length: length of the note in 1/16th notes
                        eg. a note that lasts for one bar is 1/16 * 16 -> length = 16
        @type length: int 
        
        @param velocity: the velocity of the note
        @type velocity: int
        """
        channel = profile.channel
        
        self.output.note_on(note, velocity, channel)
        
        self.queue.push(note, velocity, channel, length)
        #SEE self.queue AT __init__
    
    def choose_chord(self):       
        """Each sublist contains the half-step increments relative to the base note for 2nd, 3rd and sometimes 4th notes of the chord
        eg. [3, 7] is a minor chord (0-3-7)   
        
        FOR TESTING PURPOSES    
        """
        chords = [[3, 7], [4, 7], [3, 6], [5, 7], [5, 12], [4, 9, 12], [3, 7, 10]]
    
        return random.choice(chords)
        
midi = Midi()
note = 60

#Loop that starts from MIDI note 60 and randomly increases/decreases the base note and plays chords relative to it
while True:
            
    next = midi.choose_chord()             
    midi.play_chord(next)

    time.sleep(random.randint(1,3))
    
    note += random.randint(-5, 5)
    
