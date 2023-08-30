import sys
import pygame

from shooter import Shooter
from bullets import Bullet

class SidewaysShooter:
    """Class to represent a cowboy that shoots across the screen"""
    def __init__(self):
        """Initializes class attributes and behaviors"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.shooter = Shooter(self)    

        self.bullets = pygame.sprite.Group()   

    def run_game(self):
        while True:
            self.screen.fill((15,100,15))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        self.shooter.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.shooter.moving_down = True
                    if event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.shooter.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.shooter.moving_down = False


            self.bullets.update()
            for bullet in self.bullets:
                bullet.draw_bullet()
            self.shooter.update()
            self.shooter.draw_shooter()
            self._update_bullets()

            self.clock.tick(60)
            pygame.display.flip()

    def _fire_bullet(self):
        """Draw bullet at shooter."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Remove bullets that are out of screen bounds"""
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.shooter.screen_rect.right:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()