from .map import game_matrix, list_block, list_food
from .settings import Sprite
from .food import FOOD

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
        x += 25
    y += 25
    x = 0