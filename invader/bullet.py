import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()

        self.screen = screen
        self.color = (139, 195,  74)
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.rect.centerx = gun.rect.centerx
        self.rect.top     = gun.rect.top

        self.speed = 5

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = int(self.y)
        if self.rect.bottom < 0:
            self.kill()




    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)





