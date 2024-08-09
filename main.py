from modules import *

pygame.init()
pygame.display.set_caption("Game")
hero = Hero(50, 50, 100, 250, 'player/idle/0.png', 4, 3, 5)
enemy = Enemy(40, 40, 540, 360, 'enemy/idle/0.png', 1, 1.5, 'r', 2)
not_food = Sprite(40, 40, 760, 10, 'food/0.png')
font = pygame.font.Font(None, 43)
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
        if i.collision_food(hero):
            counter += 1
            text_food = font.render(f"{0 + counter}", True, (0, 0, 0))
        if counter > 0:
            not_food.show_sprite()
            screen.blit(text_food, (737, 19))
    if enemy.HEARTS > 0:
        enemy.show_sprite()
        enemy.check_move(hero)
        enemy.hero_colision(hero)
    else:
        enemy.enemy_death()
    if hero.HEARTS > 0:
        hero.show_sprite()
        hero.move(list_block, list_food, enemy, start_x)
        hero.jump()
    hero.hero_fell()
    pygame.display.flip()