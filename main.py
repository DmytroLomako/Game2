import pygame
from modules.settings import screen, list_block, background
from modules.hero import Hero

pygame.display.set_caption("Game")
hero = Hero(50, 50, 100, 250, 'player/idle/0.png', 4, 3, 5)
clock = pygame.time.Clock()
start = True
while start:
    clock.tick(60)
    background.show_sprite()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    for i in list_block:
        i.show_sprite()
    hero.show_sprite()
    hero.move()
    hero.hero_fell()
    hero.jump()
    pygame.display.flip()