import pygame 
from pygame.sprite import Sprite

# A class to manage all things bullets
class Bullet(Sprite):

    def __init__(self, ai_game): #Create bullet at ship's position

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) # attribute created
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet position as a decimal value
        self.y = float(self.rect.y)

    def update(self): # move bullet up screen
        self.y -= self.settings.bullet_speed # update dec position of bullet
        self.rect.y = self.y # update rect position

    def draw_bullet(self): 
        pygame.draw.rect(self.screen, self.color, self.rect)

