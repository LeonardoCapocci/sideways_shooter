import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to represent the bullets shot by shooter"""
    def __init__(self, game):
        """Initialize base bullet info"""
        super().__init__()
        self.screen = game.screen
        self.color = (50, 50, 50)
        self.speed = 7

        # Create bullet rect and set at shooter
        self.rect = pygame.Rect(0, 0, 10, 4)
        self.rect.midright = game.shooter.rect.midright

        self.rect.y -= 5.4

        self.x = float(self.rect.x)


    def update(self):
        # Update bullet position
        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)