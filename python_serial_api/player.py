from defines import *
from pygame import mixer



class Player():
    def __init__(self):
        self.player = mixer
        self.active = False
        self.user = 0
        self.track = 0
        self.player.init()
        self.player.music.load(AUDIO_TRACKS[0][0]) #TODO default track
        self.player.music.play()
    
    def setState(self, state):
        self.active = state
    
    def update(self, user, track):
        if user != self.user or track != self.track:
            print(user)
            print(self.user)
            print(track)
            print(self.track)
            print("Change")
            # No matter what state, on change turn music off
            self.player.music.stop()

            self.player.music.load(AUDIO_TRACKS[user][track])
            self.user = user
            self.track = track
        
            # If state active then play the music
            if self.active == True:        
                self.player.music.play()
        
    
    
