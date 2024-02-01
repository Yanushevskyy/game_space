import pygame, sys, gun
from bullet import Bullet


def events(screen, gun, bullets):

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            # Right
            if event.key == pygame.K_d:
                gun.mright = True
            # # left
            elif event.key == pygame.K_a:
                gun.mleft = True

            elif event.key == pygame.K_SPACE:

                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                
        elif event.type == pygame.KEYUP:
            # Right
            if event.key == pygame.K_d:
                gun.mright = False
                
            elif event.key == pygame.K_a:
                gun.mleft = False

def display_upd(bg_color,screen, gun, bullets):
    screen.fill(bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()
