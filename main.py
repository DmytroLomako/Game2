import pygame
from modules.settings import screen, background
from modules.create_map import list_block, list_apple
from modules.hero import Hero

pygame.init()
pygame.display.set_caption("Game")
hero = Hero(50, 50, 100, 250, 'player/idle/0.png', 4, 3, 5)
font = pygame.font.Font(None, 36)
counter = 0
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
    for i in list_apple:
        i.show_sprite()
        if i.collision_apple(hero):
            counter += 1
            text_apple = font.render(f"{0 + counter}", True, (0, 0, 0))
        if counter > 0:
            screen.blit(text_apple, (740, 19))
    hero.show_sprite()
    hero.move()
    hero.hero_fell()
    hero.jump()
    pygame.display.flip()