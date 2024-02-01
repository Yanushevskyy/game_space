import pygame, controls
from gun import Gun
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Space Defender")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()

    while True:

        controls.events(screen, gun, bullets)
        gun.update_gun_pos()
        bullets.update()
        controls.display_upd(bg_color,screen, gun, bullets)

run()