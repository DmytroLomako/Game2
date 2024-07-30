from .map import game_matrix, list_block, list_apple
from .settings import Sprite
from .apple import Apple

x = 0
y = 0
for i in game_matrix:
    for j in i:
        if j == 1:
            block = Sprite(25, 25, x, y, 'tilemap/level_1/1.png')
            list_block.append(block)
        elif j == 2:
            block = Sprite(25, 25, x, y, 'tilemap/level_1/2.png')
            list_block.append(block)
        elif j == 3:
            block = Sprite(25, 25, x, y, 'tilemap/level_1/3.png')
            list_block.append(block)
        elif j == 4:
            block = Sprite(25, 25, x, y, 'tilemap/level_1/4.png')
            list_block.append(block)
        elif j == 5:
            block = Sprite(25, 25, x, y, 'tilemap/level_1/5.png')
            list_block.append(block)
        elif j == 6:
            block = Sprite(25, 25, x, y, 'tilemap/level_1/6.png')
            list_block.append(block)
        elif j == 7:
            block = Sprite(25, 25, x, y, 'tilemap/level_1/7.png')
            list_block.append(block)
        elif j == 'a':
            apple = Apple(25, 25, x, y, 'apple.png')
            list_apple.append(apple)
        x += 25
    y += 25
    x = 0