import pygame,control
from  gun import  Gun
from  pygame.sprite import Group
from static import Stats





def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("invader")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    Bullets = Group()
    enemies = Group()
    control.create_army(screen, enemies)
    stats = Stats()

    while True:
        control.events(bg_color,screen,gun, Bullets,enemies)
        gun.update_gun()
        Bullets.update()
        control.update(bg_color, screen, gun,enemies ,Bullets)
        control.update_enemies(stats, screen, gun, enemies, Bullets)



run()