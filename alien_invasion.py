import sys 
import pygame

from settings import Settings # bring in settings class
from ship import Ship # bring in ship class
from bullet import Bullet # bring in bullet class

class AlienInvasion: 
    """ Overall Class for game assets & behavior """
    
    def __init__(self): #initialize the game and game resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # size of window
        pygame.display.set_caption("LmBlueJay's Alien Invasion") # Window name

        self.ship = Ship(self) # make ship instance after window created
        self.bullets = pygame.sprite.Group()

        # Background color
        self.screen.fill(self.settings.bg_color) #light gray

    def run_game(self): # start main loop of game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        elif event.key == pygame.K_SPACE:
            self.rapidfire_bullet = True
            self._fire_bullet()

    def _check_keyup_events(self, event): # Refactor for keyups
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False 
        elif event.key == pygame.K_SPACE:
            self.rapidfire_bullet = False
            self._fire_bullet()
     

    def _fire_bullet(self): # create new bullet and add it to the group of fired bullets
        if self.rapidfire_bullet and len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self): # Update bullet positions
        self.bullets.update()
        #Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets)) Tracker for live bullets

    def _update_screen(self):                    
            # Update images up to screen 
            self.screen.fill(self.settings.bg_color) # Redraw screen during each loop
            self.ship.blitme() # ship on top of background
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            
            pygame.display.flip() # Make most recently drawn screen visible

# Game initializer 
if __name__ == '__main__':
    # Make game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
