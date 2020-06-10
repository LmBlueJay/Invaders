import sys 
import pygame

from settings import Settings # bring in settings class
from ship import Ship # bring in ship class

class AlienInvasion: 
    """ Overall Class for game assets & behavior """
    
    def __init__(self): #initialize the game and game resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # size of window
        pygame.display.set_caption("LmBlueJay's Alien Invasion") # Window name

        self.ship = Ship(self) # make ship instance after window created

        # Background color
        self.screen.fill(self.settings.bg_color) #light gray

    def run_game(self): # start main loop of game
        while True:
            # Watch keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() # when exit is hit, its hit and game ends
                    pass

            self.screen.fill(self.settings.bg_color) # Redraw screen during each loop
            self.ship.blitme() # ship on top of background

            pygame.display.flip() # Make most recently drawn screen visible

if __name__ == '__main__':
    # Make game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
