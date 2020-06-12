import pygame 
from pygame.sprite import Sprite

class Alien(Sprite): # Class representing a single alien 
    def __init__(self, ai_game): #initialize alien
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien4.bmp') # load alien and set rect attribute
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width # Start each new alien at top left of scren 
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) # Store alien's horizontal position
