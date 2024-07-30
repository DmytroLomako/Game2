import pygame
from .settings import Sprite

class Apple(Sprite):
    def __init__(self, width, height, x, y, image_name):
        super().__init__(width, height, x, y, image_name)
        self.COUNT_APPLE = 0
    def collision_apple(self, hero):
        apple_rect = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        hero_rect = pygame.Rect(hero.X, hero.Y, hero.WIDTH, hero.HEIGHT)
        if apple_rect.colliderect(hero_rect):
            self.COUNT_APPLE += 1
            self.X = 760
            self.Y = 15
            return True
        