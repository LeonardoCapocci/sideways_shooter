import sys
import pygame

class SidewaysShooter:
    """Class to represent a cowboy that shoots across the screen"""
    def __init__(self):
        """Initializes class attributes and behaviors"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        self.shooter = pygame.image.load('shooter.bmp')
        self.shooter = pygame.transform.scale(self.shooter, (100,220))
        self.shooter_rect = self.shooter.get_rect()
        self.shooter_rect.midleft = self.screen_rect.midleft
        
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.screen.fill((15,125,40))
            self.screen.blit(self.shooter, self.shooter_rect)

            self.clock.tick(60)
            pygame.display.flip()

if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()