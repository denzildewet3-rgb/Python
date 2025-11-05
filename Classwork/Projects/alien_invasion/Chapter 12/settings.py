# Creating a settings class
import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background = pygame.image.load('images/background.jpg')
        self.background = pygame.transform.scale(self.background, (1200, 800))
        
        # Bullet Settings
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 20
        
        # Ship Settings
        self.ship_speed = 3.5