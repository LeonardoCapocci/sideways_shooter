import sys
import pygame

from shooter import Shooter
from bullets import Bullet
from enemy import Poster
from enemy import Enemy

class SidewaysShooter:
    """Class to represent a cowboy that shoots across the screen"""
    def __init__(self):
        """Initializes class attributes and behaviors"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        self.shooter = Shooter(self)    

        self.bullets = pygame.sprite.Group()
        self.posters = pygame.sprite.Group()   
        self.enemies = pygame.sprite.Group()

        self._create_poster()

    def run_game(self):
        while True:
            self.screen.fill((190,240,125))
            self._check_events()

            self.bullets.update()
            
            self.shooter.update()
            
            self.posters.update()

            self._create_enemies()
            self.enemies.update()

            self._check_collisions()
            self._update_screen()
            self.clock.tick(60)
            pygame.display.flip()

    def _check_events(self):
        """Check and respond to keyboard events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.shooter.moving_up = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.shooter.moving_down = True
                    if event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.shooter.moving_up = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.shooter.moving_down = False

    def _fire_bullet(self):
        """Draw bullet at shooter."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Remove bullets that are out of screen bounds"""
        for bullet in self.bullets:
                bullet.draw_bullet()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.shooter.screen_rect.right:
                self.bullets.remove(bullet)

    def _create_poster(self):
        """Creates a single poster on the right side of the screen."""
        poster = Poster(self)
        self.posters.add(poster)
    
    def _update_poster(self):
        """Updates the poster's position."""
        self.posters.update()

    def _create_enemies(self):
        """Creates a column of enemies"""
        if len(self.posters) == 0:
            if len(self.enemies) == 0:   
                enemy = Enemy(self)
                current_y = enemy.rect.y
                while current_y <= self.screen_rect.height-enemy.rect.height*2:
                    new_enemy = Enemy(self)
                    new_enemy.rect.y = current_y
                    current_y += enemy.rect.height * 1.5
                    self.enemies.add(new_enemy)

    def _check_collisions(self):
        """Checks collisions between bullets and poster/enemies."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.posters, 
                                                True, True)
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, 
                                                True, True)
        
    def _update_screen(self):
        """Updates the screen every tick."""
        self._update_bullets()
        self.shooter.draw_shooter()
        self.posters.draw(self.screen)
        self.enemies.draw(self.screen)


if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()