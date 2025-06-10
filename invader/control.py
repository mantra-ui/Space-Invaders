import pygame , sys
from bullet import Bullet
from  enemy import Enemy
import time


def events (bg_color,screen, gun, bullets,enemies):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.right = True
            elif event.key == pygame.K_a:
                gun.left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.right= False
            elif event.key == pygame.K_a:
                gun.left = False
    collisions = pygame.sprite.groupcollide(bullets,enemies,True,True)
    if len(enemies) == 0:
        bullets.empty()
        create_army(screen,enemies)

    

def update (bg_color, screen, gun, enemies, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemies.draw(screen)
    pygame.display.flip()


def gun_kill(stats, screen ,gun,enemies,bullets ):
    stats.guns_left -= 1
    enemies.empty()
    bullets.empty()
    create_army(screen, enemies)
    gun.create_gun()
    time.sleep(2)
def update_enemies(stats, screen,gun,enemies, bullets):
    enemies.update()
    if pygame.sprite.spritecollideany(gun, enemies,):
        gun_kill(stats, screen, gun, enemies,bullets)
    en_check(stats, screen, gun, enemies, bullets)


def create_army(screen, enomyies):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((700 -2 * enemy_width)/ enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 100 - 2 * enemy_height)/ enemy_height)


    for row_number in range(number_enemy_y -1):

       for enemy_nomber in range(number_enemy_x):
        enemy = Enemy(screen)
        enemy.x = enemy_width + enemy_width * enemy_nomber
        enemy.y = enemy_height + enemy_height * row_number
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.rect.height + 1 * enemy.rect.height * row_number
        enomyies.add(enemy)


def en_check(stats, screen, gun, enemies, bullets):
    screen_rect =  screen.get_rect()
    for single_enemies in enemies.sprites():
        if single_enemies.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen ,gun, enemies,bullets)
            break