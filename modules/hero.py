from pygame import *
from .settings import Person

class Hero(Person):
    def __init__(self, width, height, x, y, image_name, gravity, speed, jump_height):
        super().__init__(width, height, x, y, image_name, speed, gravity)
        self.COUNT_ANIMATION = 0
        self.DIRECTION = 'r'
        self.JUMP_HEIGHT = jump_height
        self.JUMP_COUNT = 0
        self.COUNT_CROUCH = 0
        self.HEARTS = 1
    def move(self):
        keys = key.get_pressed()
        self.check_move_left()
        self.check_move_right()
        if keys[K_LEFT] and self.CAN_MOVE_L:
            self.X -= self.SPEED
            self.DIRECTION = 'l'
            if self.JUMP_COUNT > 0:
                self.IMAGE_NAME = 'player/jump/0.png'
            elif self.FALL:
                self.IMAGE_NAME = 'player/gravity/0.png'
            elif keys[K_c]:
                self.COUNT_CROUCH += 1
                self.crouch()
            else:
                self.COUNT_ANIMATION += 1
                self.animation()
            self.load_image(True)
        elif keys[K_RIGHT] and self.CAN_MOVE_R:
            self.X += self.SPEED
            self.DIRECTION = 'r'
            if self.JUMP_COUNT > 0:
                self.IMAGE_NAME = 'player/jump/0.png'
            elif self.FALL:
                self.IMAGE_NAME = 'player/gravity/0.png'
            elif keys[K_c]:
                self.COUNT_CROUCH += 1
                self.crouch()
            else:
                self.COUNT_ANIMATION += 1
                self.animation()
            self.load_image()
        else:
            if self.DIRECTION == 'r':
                if self.JUMP_COUNT > 0:
                    self.IMAGE_NAME = 'player/jump/0.png'
                elif self.FALL:
                    self.IMAGE_NAME = 'player/gravity/0.png'
                elif keys[K_c]:
                    self.IMAGE_NAME = 'player/crouch/player-crouch-1.png'
                else:
                    self.IMAGE_NAME = 'player/idle/0.png'
                self.load_image()
            elif self.DIRECTION == 'l':
                if self.JUMP_COUNT > 0:
                    self.IMAGE_NAME = 'player/jump/0.png'
                elif self.FALL:
                    self.IMAGE_NAME = 'player/gravity/0.png'
                elif keys[K_c]:
                    self.IMAGE_NAME = 'player/crouch/player-crouch-1.png'
                else:
                    self.IMAGE_NAME = 'player/idle/0.png'
                self.load_image(True)
    def animation(self):
        animation = self.COUNT_ANIMATION // 3
        if animation == 6:
            animation = 0
            self.COUNT_ANIMATION = 0
        self.IMAGE_NAME = f'player/run/{animation}.png'
    def crouch(self):
        animation = self.COUNT_CROUCH // 10
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
    def enemy_colision(self, enemy):
        rect_hero = Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        rect_enemy = Rect(enemy.X, enemy.Y, enemy.WIDTH, enemy.HEIGHT)
        if rect_hero.colliderect(rect_enemy):
            self.HEARTS -= 1