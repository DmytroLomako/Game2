from pygame import *
from .settings import Person

class Hero(Person):
    def __init__(self, width, height, x, y, image_name, gravity, speed, jump_height):
        super().__init__(width, height, x, y, image_name, speed, gravity)
        self.COUNT_ANIMATION = 0
        self.DIRECTION = 'r'
        self.JUMP_HEIGHT = jump_height
        self.JUMP_COUNT = 0
    def move(self):
        keys = key.get_pressed()
        self.check_move_left()
        self.check_move_right()
        if keys[K_LEFT] and self.CAN_MOVE_L:
            self.X -= self.SPEED
            self.DIRECTION = 'l'
            if self.JUMP_COUNT > 0:
                self.IMAGE_NAME = 'player/jump/player-jump-1.png'
            elif self.FALL:
                self.IMAGE_NAME = 'player/jump/player-jump-2.png'
            else:
                self.COUNT_ANIMATION += 1
                self.animation()
            self.load_image(True)
        elif keys[K_RIGHT] and self.CAN_MOVE_R:
            self.X += self.SPEED
            self.DIRECTION = 'r'
            if self.JUMP_COUNT > 0:
                self.IMAGE_NAME = 'player/jump/player-jump-1.png'
            elif self.FALL:
                self.IMAGE_NAME = 'player/jump/player-jump-2.png'
            else:
                self.COUNT_ANIMATION += 1
                self.animation()
            self.load_image()
        else:
            if self.DIRECTION == 'r':
                if self.JUMP_COUNT > 0:
                    self.IMAGE_NAME = 'player/jump/player-jump-1.png'
                elif self.FALL:
                    self.IMAGE_NAME = 'player/jump/player-jump-2.png'
                else:
                    self.IMAGE_NAME = 'player/idle/0.png'
                self.load_image()
            elif self.DIRECTION == 'l':
                if self.JUMP_COUNT > 0:
                    self.IMAGE_NAME = 'player/jump/player-jump-1.png'
                elif self.FALL:
                    self.IMAGE_NAME = 'player/jump/player-jump-2.png'
                else:
                    self.IMAGE_NAME = 'player/idle/0.png'
                self.load_image(True)
    def animation(self):
        animation = self.COUNT_ANIMATION // 3
        if animation == 6:
            animation = 0
            self.COUNT_ANIMATION = 0
        self.IMAGE_NAME = f'player/run/{animation}.png'
    def jump(self):
        keys = key.get_pressed() 
        self.check_jump() 
        if keys[K_SPACE]:
            if self.FALL == False: 
                self.JUMP_COUNT = 20
        if self.JUMP_COUNT > 0: 
            self.Y -= self.JUMP_HEIGHT
            self.JUMP_COUNT -= 1 