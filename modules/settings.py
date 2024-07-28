import pygame
import os
from .map import game_matrix, list_block

screen = pygame.display.set_mode((800, 450))
class Class:
    def __init__(self, width, height, x, y, image_name):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.IMAGE_NAME = image_name
        self.IMAGE = None
        self.load_image()
    def load_image(self, flip_x = False):
        path_folder = os.path.abspath(__file__ + '/../../images')
        path_image = os.path.join(path_folder, self.IMAGE_NAME)
        self.IMAGE = pygame.image.load(path_image)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
        self.IMAGE = pygame.transform.flip(self.IMAGE, flip_x, False)
    def show_sprite(self):
        screen.blit(self.IMAGE, (self.X, self.Y))
        
class Person(Class):
    def __init__(self, width, height, x, y, image_name, speed, gravity):
        super().__init__(width, height, x, y, image_name)
        self.SPEED = speed
        self.FALL = True
        self.GRAVITY = gravity
        self.CAN_MOVE_R = True 
        self.CAN_MOVE_L = True 
    def hero_fell(self):
        self.check_fall()
        if self.JUMP_COUNT == 0:
            if self.FALL:
                self.Y += self.GRAVITY
    def check_fall(self):
        for block in list_block:
            if self.Y + self.HEIGHT > block.Y - 4 and self.X < block.X + block.WIDTH and self.X + self.WIDTH > block.X and self.Y < block.Y + block.HEIGHT: 
                self.FALL = False
                self.Y = block.Y - self.HEIGHT
                break
            else:
                self.FALL = True
    def check_move_right(self): 
        for block in list_block: 
            
            if self.X + self.WIDTH > block.X - 3 and self.X < block.X + block.WIDTH and self.Y + self.HEIGHT > block.Y and self.Y < block.Y + block.HEIGHT: 
                self.CAN_MOVE_R = False 
                
                break 
            else:
                self.CAN_MOVE_R = True 
    def check_move_left(self):
        for block in list_block:
            if self.Y + self.HEIGHT > block.Y and self.Y < block.Y + block.HEIGHT and self.X < block.X + block.WIDTH + 3 and self.X + self.WIDTH > block.X:
                self.CAN_MOVE_L = False
                break
            else:
                self.CAN_MOVE_L = True
    def check_jump(self):
        for block in list_block:
            if self.X < block.X + block.WIDTH and self.X + self.WIDTH > block.X and self.Y < block.Y + block.HEIGHT + 3 and self.Y > block.Y:
                self.JUMP_COUNT = 0
                self.FALL = True
                break
        
background = Class(800, 400, 0, 0, 'screen/1.jpeg')
        
x = 0
y = 0
for i in game_matrix:
    for j in i:
        if j == 1:
            block = Class(25, 25, x, y, 'tilemap/level_1/1.png')
            list_block.append(block)
        elif j == 2:
            block = Class(25, 25, x, y, 'tilemap/level_1/2.png')
            list_block.append(block)
        elif j == 3:
            block = Class(25, 25, x, y, 'tilemap/level_1/3.png')
            list_block.append(block)
        elif j == 4:
            block = Class(25, 25, x, y, 'tilemap/level_1/4.png')
            list_block.append(block)
        elif j == 5:
            block = Class(25, 25, x, y, 'tilemap/level_1/5.png')
            list_block.append(block)
        elif j == 6:
            block = Class(25, 25, x, y, 'tilemap/level_1/6.png')
            list_block.append(block)
        elif j == 7:
            block = Class(25, 25, x, y, 'tilemap/level_1/7.png')
            list_block.append(block)
        x += 25
    y += 25
    x = 0