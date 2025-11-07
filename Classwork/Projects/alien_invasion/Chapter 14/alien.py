import pygame
from pygame.sprite import Sprite
from pathlib import Path

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its start position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Build a robust path to the alien image
        BASE_DIR = Path(__file__).parent
        IMAGES_DIR = BASE_DIR / "images"
        alien_image_path = IMAGES_DIR / "alien.png"
        
        # Load the Alien image and set its rect attribute
        self.image = pygame.image.load(str(alien_image_path))
        self.image = pygame.transform.scale(self.image,(55, 60))
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        
    def update(self):
        """Move alien to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
    
    def check_edges(self):
        """Return True is Alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)