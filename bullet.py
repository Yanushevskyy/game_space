import pygame
from pygame.sprite import Group

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self,screen,gun):
        """Creation of bullet"""

        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,12)
        self.color = 255, 194, 14
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """movement of bullet"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """drawing of the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)