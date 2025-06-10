import pygame

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/pixilart-drawing.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.right = False
        self.left  = False
        self.speed = 1.5

    def update_gun(self):
        if self.right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.left and self.rect.left > 0:
            self.center -= self.speed
        self.rect.centerx = int(self.center)

    def output(self):
        self.screen.blit(self.image, self.rect)

    def create_gun(self):
        self.center = self.screen_rect.centerx


