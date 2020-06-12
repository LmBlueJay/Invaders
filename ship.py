import pygame

class Ship: 
    def __init__(self, ai_game): 
        # Setup ship at starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings  # for updating the ship speed in later levels
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and get its rect       
        self.image = pygame.image.load('images/ship4.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the window
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's x & y position. 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self): #Ship position is updated based on movement flag
        # Update ship's x & y values, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_x
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_x
        if self.moving_down and self.rect.bottom < self.screen_rect.top + 780:
            self.y += self.settings.ship_speed_y
        elif self.moving_up and self.rect.top > self.screen_rect.top + 680:
            self.y -= self.settings.ship_speed_y

        # Update rect object from self.x ... controlling ship position
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # Draw ship at its durrent location
        self.screen.blit(self.image, self.rect)


        


