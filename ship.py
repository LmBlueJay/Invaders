import pygame

class Ship: 
    

    def __init__(self, ai_game): 
        # Setup ship at starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and get its rect 
        ##og_ship = Image.open("images/ship.bmp")
        ##size = (512, 512)
        ##ship = ImageOps.fit(og_ship, size, Image.ANTIALIAS)

        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the window
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw ship at its durrent location
        self.screen.blit(self.image, self.rect)


        


