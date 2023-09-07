import pygame

class Shooter:
    """Class to represent the fabled shooter."""
    def __init__(self, game):
        """Initialize shooter attributes."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.shooter = pygame.image.load('shooter.bmp')
        self.shooter = pygame.transform.scale(self.shooter, (100,220))
        self.rect = self.shooter.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
    
        # Shooter position starts non moving
        self.moving_up = False
        self.moving_down = False
        self.speed = 7

    def update(self):
        """Updates positioning of shooter."""
        if self.moving_up and self.y > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        self.rect.y = self.y
    
    def draw_shooter(self):
        """Draws the shooter."""
        self.screen.blit(self.shooter, self.rect)