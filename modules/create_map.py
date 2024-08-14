from .map import game_matrix, list_block, list_food, list_food_y, enemy_list, enemy_list_x, enemy_list_direction
from .settings import Sprite
from .food import FOOD
from .enemy import Enemy

x = 0
y = 0
for i in game_matrix:
    for j in i:
        if j == 1:
            block = Sprite(25, 25, x, y, 'map/level_1/1.png')
            list_block.append(block)
        elif j == 2:
            block = Sprite(25, 25, x, y, 'map/level_1/2.png')
            list_block.append(block)
        elif j == 3:
            block = Sprite(25, 25, x, y, 'map/level_1/3.png')
            list_block.append(block)
        elif j == 7:
            block = Sprite(25, 25, x, y, 'map/level_1/7.png')
            list_block.append(block)
        elif j == 8:
            block = Sprite(25, 25, x, y, 'map/level_1/8.png')
            list_block.append(block)
        elif j == 9:
            block = Sprite(25, 25, x, y, 'map/level_1/9.png')
            list_block.append(block)
        elif j == 'a':
            food = FOOD(30, 30, x + 2, y - 2, 'food/0.png')
            list_food.append(food)
            list_food_y.append(food.Y)
        elif j == 's':
            start_x = Sprite(25, 25, x, y, 'food/0.png')
        elif j == 'e':
            enemy =  Enemy(40, 40, x, y, 'enemy/idle/0.png', 1, 1.5, 'r', 2)
            enemy_list.append(enemy)
            enemy_list_x.append(enemy.X)
            enemy_list_direction.append(enemy.DIRECTION)
        x += 25
    y += 25
    x = 0