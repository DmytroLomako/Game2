import pygame
import os
from .map import list_block

screen = pygame.display.set_mode((800, 450))
class Sprite:
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
        
class Person(Sprite):
    def __init__(self, width, height, x, y, image_name, speed, gravity, crouching_ability = 0):
        super().__init__(width, height, x, y, image_name)
        self.SPEED = speed
        self.FALL = True
        self.GRAVITY = gravity
        self.CAN_MOVE_R = True 
        self.CAN_MOVE_L = True 
        self.CROUCHING_ABILITY = crouching_ability
    def hero_fell(self):
        self.check_fall()
        if self.JUMP_COUNT == 0:
            if self.FALL:
                self.Y += self.GRAVITY
    def check_fall(self):
        for block in list_block:
            if self.Y + self.HEIGHT > block.Y - 2 and self.X < block.X + block.WIDTH and self.X + self.WIDTH > block.X and self.Y < block.Y + block.HEIGHT - self.CROUCHING_ABILITY: 
                self.FALL = False
                self.Y = block.Y - self.HEIGHT
                break
            else:
                self.FALL = True
    def check_move_right(self): 
        for block in list_block: 
            
            if self.X + self.WIDTH > block.X - self.SPEED - 1 and self.X < block.X + block.WIDTH and self.Y + self.HEIGHT > block.Y and self.Y < block.Y + block.HEIGHT - self.CROUCHING_ABILITY: 
                self.CAN_MOVE_R = False 
                
                break 
            else:
                self.CAN_MOVE_R = True 
    def check_move_left(self):
        for block in list_block:
            if self.Y + self.HEIGHT > block.Y and self.Y < block.Y + block.HEIGHT - self.CROUCHING_ABILITY and self.X < block.X + block.WIDTH + self.SPEED + 2 and self.X + self.WIDTH > block.X:
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
        
background = Sprite(800, 400, 0, 0, 'screen/1.jpeg')
        