from modules import *
import sqlite3

connection = sqlite3.connect('Data.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
connection.commit()
pygame.init()
pygame.display.set_caption("Game")
hero = Hero(50, 50, 100, 250, 'player/idle/0.png', 4, 3, 5)
enemy = Enemy(40, 40, 540, 360, 'enemy/idle/0.png', 1, 1.5, 'r', 2)
not_food = Sprite(40, 40, 760, 10, 'food/0.png')
font = pygame.font.Font(None, 43)
font_small = pygame.font.Font(None, 25)
text_auth = font.render('Welcome back', True, (255, 255, 255))
text_login = font_small.render('Username', True, (255, 255, 255))
input_login = pygame.Rect(310, 140, 180, 30)
text_password = font_small.render('Password', True, (255, 255, 255))
input_password = pygame.Rect(310, 260, 180, 30)
button_login = pygame.Rect(350, 330, 100, 30)
text_login_button = font_small.render('Sign in', True, (255, 255, 255))
text_register0 = font_small.render("Don't have an account?", True, (255, 255, 255))
text_register = font_small.render("Sign up.", True, (179, 214, 252))
rect_register = pygame.Rect(462, 388, 68, 24)
rect_show_password = pygame.Rect(455, 235, 32, 18)
show_password_icon = Sprite(52, 37, 445, 225, 'login/show_password1.png')
counter = 0
clock = pygame.time.Clock()
start = True
scene = 'login'
active_field = None
blue_color = (127, 184, 245)
text_input_password = ''
text_input_login = ''
show_password = False
while start:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if scene == 'login' or scene =='register':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_login.collidepoint(event.pos):
                    active_field = 'input_login'
                elif input_password.collidepoint(event.pos):
                    active_field = 'input_password'
                else:
                    active_field = None
                if button_login.collidepoint(event.pos):
                    if scene == 'login':
                        cursor.execute('SELECT * FROM Users WHERE username = ? AND password = ?', (text_input_login, text_input_password))
                        user = cursor.fetchone()
                        if user == None:
                            text_input_login = ''
                            text_input_password = ''
                        else:
                            scene = 'game'
                    elif scene == 'register':
                        if text_input_login != '' and text_input_password != '':
                            cursor.execute('INSERT INTO Users (username, password) VALUES (?, ?)', (text_input_login, text_input_password))
                            connection.commit()
                            scene = 'game'
                if rect_register.collidepoint(event.pos):
                    if scene == 'login':
                        scene = 'register'
                        text_auth = font.render('Create an account', True, (255, 255, 255))
                        text_register0 = font_small.render("Already have an account?", True, (255, 255, 255))
                        text_register = font_small.render('Sign in.', True, (179, 214, 252))
                        text_login_button = font_small.render('Sign up', True, (255, 255, 255))
                    elif scene == 'register':
                        scene = 'login'
                        text_auth = font.render('Welcome back', True, (255, 255, 255))
                        text_register0 = font_small.render("Don't have an account?", True, (255, 255, 255))
                        text_login_button = font_small.render('Sign in', True, (255, 255, 255))
                        text_register = font_small.render("Sign up.", True, (179, 214, 252))
                    text_input_login = ''
                    text_input_password = ''
                    show_password = False
                if rect_show_password.collidepoint(event.pos):
                    show_password = not show_password
            if event.type == pygame.KEYDOWN:
                if active_field == 'input_login':
                    if event.key == pygame.K_BACKSPACE:
                        if len(text_input_login) > 0:
                            text_input_login = list(text_input_login)
                            text_input_login.pop()
                            text_input_login = ''.join(text_input_login)
                    else:
                        if len(text_input_login) < 13:
                            text_input_login += event.unicode
                elif active_field == 'input_password':
                    if event.key == pygame.K_BACKSPACE:
                        if len(text_input_password) > 0:
                            text_input_password = list(text_input_password)
                            text_input_password.pop()
                            text_input_password = ''.join(text_input_password)
                    else:
                        if len(text_input_password) < 13:
                            text_input_password += event.unicode
    if scene == 'game':
        background.show_sprite()
        for i in list_block:
            i.show_sprite()
        for i in list_food:
            if i.collision_food(hero):
                counter += 1
                text_food = font.render(f"{0 + counter}", True, (0, 0, 0))
            if counter > 0:
                not_food.show_sprite()
                screen.blit(text_food, (737, 19))
        if enemy.HEARTS > 0:
            enemy.show_sprite()
            enemy.check_move(hero)
            enemy.hero_colision(hero)
        else:
            enemy.enemy_death()
        if hero.HEARTS > 0:
            hero.show_sprite()
            hero.move(list_block, list_food, enemy, start_x)
            hero.jump()
        else:
            scene = 'menu'
        hero.hero_fell()
    elif scene == 'login' or scene == 'register':
        screen.fill((0, 0, 0))
        background_login.show_sprite()
        background_login2.show_sprite()
        screen.blit(text_login, (310, 100))
        if active_field == 'input_login':
            pygame.draw.rect(screen, blue_color, input_login, 2)
            text_input_login_object = font_small.render(text_input_login, True, blue_color)
        else:
            pygame.draw.rect(screen, (255, 255, 255), input_login, 2)
            text_input_login_object = font_small.render(text_input_login, True, (255, 255, 255))
        screen.blit(text_input_login_object, (315, 145))
        screen.blit(text_password, (310, 220))
        if active_field == 'input_password':
            pygame.draw.rect(screen, blue_color, input_password, 2)
            if show_password:
                text_input_password_object = font_small.render(text_input_password, True, blue_color)
            elif not show_password:
                text_input_password_object = font.render('*' * len(text_input_password), True, blue_color)
        else:
            pygame.draw.rect(screen, (255, 255, 255), input_password, 2)
            if show_password:
                text_input_password_object = font_small.render(text_input_password, True, (255, 255, 255))
                show_password_icon = Sprite(52, 37, 445, 225, 'login/show_password2.png')
            elif not show_password:
                text_input_password_object = font.render('*' * len(text_input_password), True, (255, 255, 255))
                show_password_icon = Sprite(52, 37, 445, 225, 'login/show_password1.png')
        screen.blit(text_input_password_object, (315, 265))
        pygame.draw.rect(screen, (0, 120, 0), button_login)
        if scene == 'login':
            screen.blit(text_auth, (299, 38))
            screen.blit(text_register0, (270, 390))
            screen.blit(text_register, (464, 390))
            rect_register = pygame.Rect(462, 388, 68, 24)
            screen.blit(text_login_button, (373, 336))
        elif scene =='register':
            screen.blit(text_auth, (273, 38))
            screen.blit(text_register0, (263, 390))
            screen.blit(text_register, (478, 390))
            rect_register = pygame.Rect(475, 388, 68, 24)
            screen.blit(text_login_button, (370, 336))
        # pygame.draw.rect(screen, (255, 255, 255), rect_show_password, 2)
        show_password_icon.show_sprite()
    pygame.display.flip()
connection.commit()
connection.close()