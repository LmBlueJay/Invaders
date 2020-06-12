import pygame  
from pygame.sprite import Sprite

class Stars(Sprite): # Class representing a single star 
    def __init__(self, ai_game): #initialize star
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/back.bmp') # load alien and set rect attribute
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width # Start each new star at top left of scren 
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) # Store star's horizontal position
