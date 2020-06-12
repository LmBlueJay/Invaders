import sys 
import pygame


from settings import Settings # bring in settings class
from ship import Ship # bring in ship class
from bullet import Bullet # bring in bullet class
from alien import Alien # bring in Alien class
##from stars import Stars # bring in Stars Class
## from random import randint

class AlienInvasion: 
    """ Overall Class for game assets & behavior """
    
    def __init__(self): #initialize the game and game resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # size of window
        pygame.display.set_caption("LmBlueJay's Alien Invasion") # Window name

        self.stars = pygame.sprite.Group()
        self.ship = Ship(self) # make ship instance after window created
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

##        self._create_field()
        self._create_fleet()

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
    
    ##def _create_field(self): # Creating the field of stars
    ##    star = Stars(self)
    ##    self.stars.add(star)

    ##    stars = Stars(self) # Create an star
    ##    stars_width, stars_height = stars.rect.size #  
        
    ##    available_space_x = self.settings.screen_width   # x space calculation
    ##    number_stars_x = available_space_x // (2 * stars_width)
        
    ##    # y space calculation
    ##    available_space_y = (self.settings.screen_height)
    ##    number_stars_y = available_space_y // (stars_height)
        
    ##    for row_number in range(number_stars_y) : # Create full fleet/array of aliens
    ##        for stars_number in range(number_stars_x) : # Create full fleet of aliens
    ##            self._create_stars(stars_number, row_number)

    def _create_fleet(self): # Creating the fleet of aliens
        alien = Alien(self) # Create an alien
        alien_width, alien_height = alien.rect.size # spacing between each alien is equal to the alien width and height... tuple 
        
        available_space_x = self.settings.screen_width - (1 * alien_width)   # x space calculation
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height = self.ship.rect.height  # y space calculation
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        for row_number in range(number_rows) : # Create full fleet/array of aliens
            for alien_number in range(number_aliens_x) : # Create full fleet of aliens
                self._create_alien(alien_number, row_number)

    ##def _create_stars(self, stars_number, row_number): # Create aliens in a row
    ##        stars = Stars(self)
    ##        stars_width, stars_height = stars.rect.size
    ##        stars.x = stars_width + 2 * stars_width * stars_number
    ##        stars.rect.x = stars.x
    ##        stars.rect.y = stars.rect.height + 2 * stars.rect.height * row_number
    ##        self.stars.add(stars) # Create first row of aliens

    def _create_alien(self, alien_number, row_number): # Create aliens in a row
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien) # Create first row of aliens


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
            self.stars.draw(self.screen) #stars to appear
            self.ship.blitme() # ship on top of background
            for bullet in self.bullets.sprites(): # bullets to appear
                bullet.draw_bullet()
            
            self.aliens.draw(self.screen) # alien to appear
            

            
            pygame.display.flip() # Make most recently drawn screen visible

# Game initializer 
if __name__ == '__main__':
    # Make game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
