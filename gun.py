import pygame


class Gun():

    def __init__(self, screen):
        """ incialisation of the gun"""

        self.screen = screen
        self.image = pygame.image.load('pics/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):

        self.screen.blit(self.image, self.rect)

    def update_gun_pos(self):
        """Gun position update"""

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left >0:
            self.center -= 1.5
        
        self.rect.centerx = self.center