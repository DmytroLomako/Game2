from modules import *
import sqlite3
import json

connection = sqlite3.connect('Data.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
connection.commit()
pygame.init()
pygame.display.set_caption("Game")

with open('data.json', 'r') as f:
    data = json.load(f)
hero = Hero(50, 50, data['hero_x'], data['hero_y'], 'player/idle/0.png', 4, 3, 5)

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
font2 = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 25)
play_button = pygame.Rect(300, 40, 200, 80)
play_text = font2.render('PLAY', True, 'black')
exit_button = pygame.Rect(300, 320, 200, 80)
exit_text = font2.render('EXIT', True, 'black')
continue_button = pygame.Rect(300, 180, 200, 80)
continue_text = font2.render('CONTINUE', True, 'black')
finish_text = font2.render('FINISH', True, 'black')
counter = data['counter']
clock = pygame.time.Clock()
start = True
scene = 'login'
active_field = None
blue_color = (127, 184, 245)
text_input_password = ''
text_input_login = ''
show_password = False
count_continue = 0
count_enemy_death_animation = 0
start_x.X = data['start_x']
level = data['level']
hero.HEARTS = data['hero_hearts']

def game_work():
    global count_continue, counter, text_food, scene
    if level == 1: 
        background.show_sprite()
    elif level == 2:
        background2.show_sprite()
    finish.show_sprite()
    for enemy in enemy_list:
        if enemy.HEARTS > 0:
            enemy.show_sprite()
            enemy.check_move(hero)
            enemy.hero_colision(hero)
        else:
            if count_enemy_death_animation == 0:
                enemy.enemy_death()
    for i in list_block:
        i.show_sprite()
    for i in list_food:
        if i.collision_food(hero):
            counter += 1
            text_food = font.render(f"{0 + counter}", True, (0, 0, 0))
        if count_continue > 0:
            count_continue = 0
            text_food = font.render(f"{0 + counter}", True, (0, 0, 0))
        if counter > 0:
            not_food.show_sprite()
            if counter < 10:
                screen.blit(text_food, (737, 19))
            else:
                screen.blit(text_food, (726, 19))
    if hero.HEARTS > 0:
        hero.show_sprite()
        hero.hero_fell()
        hero.move(list_block, list_food, enemy_list, start_x, finish)
        hero.jump()
    else:
        scene = 'menu'
try:
    for i in range(len(enemy_list)):
        enemy_list[i].X = data['enemies'][i]['enemy_x']
        enemy_list[i].HEARTS = data['enemies'][i]['enemy_hearts']
        enemy_list[i].DIRECTION = data['enemies'][i]['direction']
except IndexError:
    pass
try:
    for i in range(len(list_food)):
        list_food[i].Y = data['food'][i]['food_y']
except IndexError:
    pass
while start:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            new_data = {
                "start_x" : start_x.X,
                "hero_x" : hero.X,
                "hero_y" : hero.Y,
                "hero_hearts" : hero.HEARTS,
                "level" : level,
                "counter" : counter,
                'enemies' : [],
                "food": []
            }
            for enemy in enemy_list:
                enemy_dict = {
                    'enemy_x' : enemy.X,
                    "enemy_hearts" : enemy.HEARTS,
                    'direction' : enemy.DIRECTION
                }
                new_data['enemies'].append(enemy_dict)
            for food in list_food:
                food_dict = {
                    'food_y' : food.Y
                }
                new_data['food'].append(food_dict)
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent = 4)
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
                            scene = 'menu'
                    elif scene == 'register':
                        if text_input_login != '' and text_input_password != '':
                            cursor.execute('INSERT INTO Users (username, password) VALUES (?, ?)', (text_input_login, text_input_password))
                            connection.commit()
                            scene = 'menu'
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
        elif scene == 'menu':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(pygame.mouse.get_pos()):
                    if hero.HEARTS > 0:
                        count_continue += 1
                        count_enemy_death_animation += 1
                        for i in list_block:
                            i.X += data['start_x']
                        for i in list_food:
                            i.X += data['start_x']
                        for i in range(len(enemy_list)):     
                            enemy_list[i].X = data['enemies'][i]['enemy_x']
                        finish.X += data['start_x']
                        scene = f'game{level}'
                elif play_button.collidepoint(pygame.mouse.get_pos()):
                    level = 1
                    start_x.X = 0
                    counter = 0
                    count_continue = 0
                    for i in range(len(list_block)):
                        list_block[i].X = list_block_x[i]
                    for i in range(len(list_food)):
                        list_food[i].X = list_food_x[i]
                        list_food[i].Y = list_food_y[i]
                    for i in range(len(enemy_list)):
                        enemy_list[i].X = enemy_list_x[i]
                        enemy_list[i].HEARTS = 1
                        enemy_list[i].DIRECTION = enemy_list_direction[i]
                    finish.X = 1840
                    hero.X = 100
                    hero.Y = 250
                    hero.HEARTS = 1
                    scene = 'game1'
                elif exit_button.collidepoint(pygame.mouse.get_pos()):
                    start = False
    if scene == 'game1':
        game_work()
        if hero.finish_colision(finish):
            hero.X = 100
            hero.Y = 400
            map_creation(game_matrix2)
            start_x.X = 0
            finish.X = 1840
            level = 2
            scene = 'game2'
    elif scene == 'game2':
        game_work()
        if hero.finish_colision(finish):
            hero.X = 100
            hero.Y = 400
            start_x.X = 0
            finish.X = 1840
            text_all_food = font2.render(f'You collected {counter} units of food', True, (100, 80, 10))
            scene = 'finish'
    elif scene == 'finish':
        background2.HEIGHT = 450
        background2.load_image()
        background2.show_sprite()
        screen.blit(text_all_food, (170, 30))
        screen.blit(finish_text, (350, 185))
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
        show_password_icon.show_sprite()
    elif scene == 'menu':
        screen.fill((0, 0, 0))
        background_menu.show_sprite()
        pygame.draw.rect(screen, (100, 200, 100), play_button)
        screen.blit(play_text, (356, 63))
        pygame.draw.rect(screen, (200, 100, 100), exit_button)
        screen.blit(exit_text, (356, 343))
        pygame.draw.rect(screen, (100, 200, 100), continue_button)
        screen.blit(continue_text, (305, 203))
    pygame.display.flip()
connection.commit()
connection.close()