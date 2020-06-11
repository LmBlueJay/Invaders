class Settings: #Stores all game settings

    def __init__(self): # initialize settings
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed_x = 1.5 # x speed
        self.ship_speed_y = 1.0 # y speed

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

