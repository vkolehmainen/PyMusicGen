from core.profile import Profile

class ProfileManager():
    
    def __init__(self, logic):
        """Manages instrument profiles."""
        
        self.logic = logic
        self.profiles = []
        
    def add_profile(self, name, channel):
        """Adds a new profile.
        
        @param name: the name of the new profile
        @type name: string
        """
        
        new_profile = Profile(name, channel, self)
        self.profiles.append(new_profile)
        
    def delete_profile(self, profile):
        """Deletes a profile.
        
        @param profile: the profile to delete
        @type profile: Profile 
        """
        
        self.profiles.remove(profile)