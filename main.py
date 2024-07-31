import pygame
from modules.settings import screen, background
from modules.create_map import list_block, list_food
from modules.hero import Hero
from modules.enemy import Enemy

pygame.init()
pygame.display.set_caption("Game")
hero = Hero(50, 50, 100, 250, 'player/idle/0.png', 4, 3, 5)
enemy = Enemy(40, 40, 540, 360, 'enemy/idle/0.png', 4, 4, 'r')
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
    for i in list_food:
        i.show_sprite()
        if i.collision_food(hero):
            counter += 1
            text_food = font.render(f"{0 + counter}", True, (0, 0, 0))
        if counter > 0:
            screen.blit(text_food, (740, 19))
    enemy.show_sprite()
    enemy.move_enemy()
    hero.enemy_colision(enemy)
    if hero.HEARTS > 0:
        hero.show_sprite()
        hero.move()
        hero.hero_fell()
        hero.jump()
    pygame.display.flip()