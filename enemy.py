import pygame
from pygame.sprite import Sprite

class Poster(Sprite):
    """A class to represent the enemy who must be taken down."""
    def __init__(self, game):
        """Set the starting formation of a single wanted poster."""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load image and set size
        self.image = pygame.image.load('wanted_poster.bmp')
        self.image = pygame.transform.scale(self.image, (372,546))
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.width
        self.rect.midleft = self.screen_rect.midright
    
    def update(self):
        """Update the positioning of the enemy."""
        self.rect.x -= 2


class Enemy(Sprite):
    """A class to represent the enemy who must be taken down."""
    def __init__(self, game):
        """Set the starting formation of a single wanted poster."""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.speed = 5

        # Load image and set size
        self.image = pygame.image.load('enemy.bmp')
        self.image = pygame.transform.scale(self.image, (50,90))
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.width
        self.rect.y = self.rect.height
    
    def update(self):
        """Update the positioning of the enemy."""
        self.rect.x -= self.speed