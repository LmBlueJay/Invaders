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
            self._check_events()
            self.ship.update()
            self._update_screen()
                    
    def _check_events(self):        
        # Watch keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # when exit is hit, its hit and game ends

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

## Refactors referenced in While loop
    def _check_keydown_events(self, event): # Refactor for keydowns
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True 
        elif event.key == pygame.K_q: # Exit at anytime by pressing 'q'
            sys.exit()

    def _check_keyup_events(self, event): # Refactor for keyups
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False 

    def _update_screen(self):                    
            # Update images up to screen 
            self.screen.fill(self.settings.bg_color) # Redraw screen during each loop
            self.ship.blitme() # ship on top of background

            pygame.display.flip() # Make most recently drawn screen visible

# Game initializer 
if __name__ == '__main__':
    # Make game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
