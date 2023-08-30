import pygame

class Shooter:
    """Class to represent the fabled shooter"""
    def __init__(self, game):
        """Initialize shooter attributes"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.shooter = pygame.image.load('shooter.bmp')
        self.shooter = pygame.transform.scale(self.shooter, (100,220))
        self.rect = self.shooter.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
    
        # Shooter position starts non moving
        moving_up = False
        moving_down = False

    def update(self, ss_game):
        """Updates positioning of shooter"""
        self.screen.blit(self.shooter, self.rect)