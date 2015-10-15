from core.profilemanager import ProfileManager
from core.midi import Midi
from core.databasemanager import DatabaseManager

class Logic():
    
    def __init__(self):
        
        self.profile_manager = ProfileManager()
        self.midi = Midi()
        self.database_manager = DatabaseManager()