import pygame
from pygame.sprite import Sprite

class Enemies(Sprite):
    """A class to represent the enemy who must be taken down."""
    def __init__(self, game):
        """Set the starting formation of a single wanted poster."""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load image and set size
        self.image = pygame.image.load('wanted_poster.bmp')
        self.image = pygame.transform.scale(self.image, (186,273))
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.width
        self.rect.y = 300#self.screen_rect.height
    
    def update(self):
        """Update the positioning of the enemy."""
        self.rect.x -= 2