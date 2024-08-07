from .settings import Person
from pygame import Rect

class Enemy(Person):
    def __init__(self, width, height, x, y, image_name, speed, gravity, direction, jump_height):
        super().__init__(width, height, x, y, image_name, speed, gravity)
        self.DIRECTION = direction
        self.JUMP_COUNT = 0
        self.HEARTS = 1
        self.JUMP_HEIGHT = jump_height
        self.DEATH_ANIMATION = 0
        self.COUNT_IDLE_ANIMATION = 0
    def move_enemy(self):
        self.hero_fell()
        self.check_move_right()
        self.check_move_left()
        if self.DIRECTION == 'r':
            self.X += self.SPEED
            self.jump()
            self.load_image(True)
            if self.CAN_MOVE_R == False:
                self.DIRECTION = 'l'
        elif self.DIRECTION == 'l':
            self.X -= self.SPEED
            self.jump()
            self.load_image()
            if self.CAN_MOVE_L == False:
                self.DIRECTION = 'r'
    def check_move(self, hero):
        if self.X - 200 < hero.X and self.Y + self.HEIGHT >= hero.Y + self.HEIGHT - 100 and self.Y + self.HEIGHT <= hero.Y + hero.HEIGHT + 100:
            self.move_enemy()
        else:
            if self.FALL == True or self.JUMP_COUNT > 0:
                self.JUMP_COUNT = 0
                self.IMAGE_NAME = f'enemy/gravity/0.png'
                self.hero_fell()
                if self.DIRECTION == 'r':
                    self.load_image(True)
                elif self.DIRECTION == 'l':
                    self.load_image()
            else:
                self.COUNT_IDLE_ANIMATION += 1
                self.enemy_idle_animation()
                if self.DIRECTION == 'r':
                    self.load_image(True)
                elif self.DIRECTION == 'l':
                    self.load_image()
    def hero_colision(self, hero):
        rect_hero = Rect(hero.X, hero.Y, hero.WIDTH, hero.HEIGHT)
        rect_enemy = Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        if hero.Y + hero.HEIGHT > self.Y and hero.X < self.X + self.WIDTH and hero.X + hero.WIDTH > self.X and self.Y + self.HEIGHT > hero.Y + hero.HEIGHT:
            self.HEARTS -= 1
        else:
            if rect_hero.colliderect(rect_enemy):
                hero.HEARTS -= 1
    def jump(self):
        self.check_jump()
        if self.FALL == False: 
            self.JUMP_COUNT = 20
        else:
            self.IMAGE_NAME = f'enemy/gravity/0.png'
        if self.JUMP_COUNT > 0: 
            self.IMAGE_NAME = f'enemy/jump/0.png'
            self.Y -= self.JUMP_HEIGHT
            self.JUMP_COUNT -= 1 
    def enemy_death(self):
        animation = self.DEATH_ANIMATION // 6
        if animation < 6:
            self.show_sprite()
            self.DEATH_ANIMATION += 1
            self.IMAGE_NAME = f'enemy-death/{animation}.png'
            if self.DIRECTION == 'r':
                self.load_image(True)
            elif self.DIRECTION == 'l':
                self.load_image()
    def enemy_idle_animation(self):
        animation = self.COUNT_IDLE_ANIMATION // 14
        if animation == 4:
            animation = 0
            self.COUNT_IDLE_ANIMATION = 0
        self.IMAGE_NAME = f'enemy/idle/{animation}.png'