class Settings: #Stores all game settings

    def __init__(self): # initialize settings
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship Settings
        self.ship_speed_x = 1.5 # x speed
        self.ship_speed_y = 1.0 # y speed

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (243, 73, 74)
        self.bullets_allowed = 4

