from .settings import Person
from pygame import Rect

class Enemy(Person):
    def __init__(self, width, height, x, y, image_name, speed, gravity, direction):
        super().__init__(width, height, x, y, image_name, speed, gravity)
        self.DIRECTION = direction
        self.JUMP_COUNT = 0
        self.HEARTS = 1
    def move_enemy(self):
        self.hero_fell()
        self.check_move_right()
        self.check_move_left()
        if self.DIRECTION == 'r':
            self.X += self.SPEED
            self.load_image(True)
            if self.CAN_MOVE_R == False:
                self.DIRECTION = 'l'
        elif self.DIRECTION == 'l':
            self.X -= self.SPEED
            self.load_image()
            if self.CAN_MOVE_L == False:
                self.DIRECTION = 'r'
    def hero_colision(self, hero):
        rect_hero = Rect(hero.X, hero.Y, hero.WIDTH, hero.HEIGHT)
        rect_enemy = Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        if hero.Y + hero.HEIGHT > self.Y and hero.X < self.X + self.WIDTH and hero.X + hero.WIDTH > self.X and self.Y + self.HEIGHT > hero.Y + hero.HEIGHT:
            self.HEARTS -= 1
        else:
            if rect_hero.colliderect(rect_enemy):
                hero.HEARTS -= 1