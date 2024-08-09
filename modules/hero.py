from pygame import *
from .settings import Person

class Hero(Person):
    def __init__(self, width, height, x, y, image_name, gravity, speed, jump_height, crouching_ability = 0):
        super().__init__(width, height, x, y, image_name, speed, gravity, crouching_ability)
        self.COUNT_ANIMATION = 0
        self.DIRECTION = 'r'
        self.JUMP_HEIGHT = jump_height
        self.JUMP_COUNT = 0
        self.COUNT_CROUCH = 0
        self.HEARTS = 1
        self.IDLE_ANIMATION = 0
        self.CROUCHING_ABILITY = 0
    def move(self, list_block, list_food, enemy, start_x):
        keys = key.get_pressed()
        self.check_move_left()
        self.check_move_right()
        if keys[K_LEFT] and self.CAN_MOVE_L:
            if self.X <= -5:
                self.X = -5
                self.IDLE_ANIMATION += 1
                self.animation_idle()
                self.load_image(True)
            else:
                if start_x.X >= 0:
                    self.X -= self.SPEED
                elif start_x.X < 0 and self.X == 100:
                    for block in list_block:
                        block.X += self.SPEED
                    for food in list_food:
                        food.X += self.SPEED
                    enemy.X += self.SPEED
                    start_x.X += self.SPEED
                else:
                    self.X -= self.SPEED
                self.DIRECTION = 'l'
                if self.CROUCHING_ABILITY == 25 and self.C:
                    self.COUNT_CROUCH += 1
                    self.crouch()
                else:
                    self.CROUCHING_ABILITY = 0
                    if self.JUMP_COUNT > 0:
                        self.IMAGE_NAME = 'player/jump/0.png'
                    elif self.FALL:
                        self.IMAGE_NAME = 'player/gravity/0.png'
                    elif keys[K_c]:
                        self.COUNT_CROUCH += 1
                        self.CROUCHING_ABILITY = 25
                        self.crouch()
                    else:
                        self.COUNT_ANIMATION += 1
                        self.animation()
                self.load_image(True)
        elif keys[K_RIGHT] and self.CAN_MOVE_R:
            if self.X >= 760:
                self.X = 760
                self.IDLE_ANIMATION += 1
                self.animation_idle()
                self.load_image()
            else:
                if start_x.X <= -1700:
                    self.X += self.SPEED
                elif start_x.X > -1700 and self.X == 100:
                    for block in list_block:
                        block.X -= self.SPEED
                    for food in list_food:
                        food.X -= self.SPEED
                    enemy.X -= self.SPEED
                    start_x.X -= self.SPEED
                else:
                    self.X += self.SPEED
                self.DIRECTION = 'r'
                if self.CROUCHING_ABILITY == 25 and self.C:
                    self.COUNT_CROUCH += 1
                    self.crouch()
                else:
                    self.CROUCHING_ABILITY = 0
                    if self.JUMP_COUNT > 0:
                        self.IMAGE_NAME = 'player/jump/0.png'
                    elif self.FALL:
                        self.IMAGE_NAME = 'player/gravity/0.png'
                    elif keys[K_c]:
                        self.COUNT_CROUCH += 1
                        self.CROUCHING_ABILITY = 25
                        self.crouch()
                    else:
                        self.COUNT_ANIMATION += 1
                        self.animation()
                self.load_image()
        else:
            if self.DIRECTION == 'r':
                if self.CROUCHING_ABILITY == 25 and self.C:
                    self.COUNT_CROUCH += 1
                    self.crouch()
                else:
                    self.CROUCHING_ABILITY = 0
                    if self.JUMP_COUNT > 0:
                        self.IMAGE_NAME = 'player/jump/0.png'
                    elif self.FALL:
                        self.IMAGE_NAME = 'player/gravity/0.png'
                    elif keys[K_c]:
                        self.COUNT_CROUCH += 1
                        self.CROUCHING_ABILITY = 25
                        self.crouch()
                    else:
                        self.IDLE_ANIMATION += 1
                        self.animation_idle()
                self.load_image()
            elif self.DIRECTION == 'l':
                if self.CROUCHING_ABILITY == 25 and self.C:
                    self.COUNT_CROUCH += 1
                    self.crouch()
                else:
                    self.CROUCHING_ABILITY = 0
                    if self.JUMP_COUNT > 0:
                        self.IMAGE_NAME = 'player/jump/0.png'
                    elif self.FALL:
                        self.IMAGE_NAME = 'player/gravity/0.png'
                    elif keys[K_c]:
                        self.COUNT_CROUCH += 1
                        self.CROUCHING_ABILITY = 25
                        self.crouch()
                    else:
                        self.IDLE_ANIMATION += 1
                        self.animation_idle()
                self.load_image(True)
    def animation(self):
        animation = self.COUNT_ANIMATION // 3
        if animation == 6:
            animation = 0
            self.COUNT_ANIMATION = 0
        self.IMAGE_NAME = f'player/run/{animation}.png'
    def crouch(self):
        animation = self.COUNT_CROUCH // 8
        if animation == 2:
            animation = 0
            self.COUNT_CROUCH = 0
        self.IMAGE_NAME = f'player/crouch/player-crouch-{animation}.png'
    def jump(self):
        keys = key.get_pressed() 
        self.check_jump() 
        if keys[K_SPACE]:
            if self.FALL == False: 
                self.JUMP_COUNT = 20
        if self.JUMP_COUNT > 0: 
            self.Y -= self.JUMP_HEIGHT
            self.JUMP_COUNT -= 1 
    def animation_idle(self):
        animation = self.IDLE_ANIMATION // 8
        if animation == 4:
            animation = 0
            self.IDLE_ANIMATION = 0
        self.IMAGE_NAME = f'player/idle/{animation}.png'