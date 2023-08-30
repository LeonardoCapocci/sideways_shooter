import sys
import pygame

from shooter import Shooter

class SidewaysShooter:
    """Class to represent a cowboy that shoots across the screen"""
    def __init__(self):
        """Initializes class attributes and behaviors"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.shooter = Shooter(self)       

    def run_game(self):
        while True:
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
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.shooter.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.shooter.moving_down = False

            self.screen.fill((15,125,40))
            self.shooter.update(self)

            self.clock.tick(60)
            pygame.display.flip()

if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()