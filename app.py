# IMPORT MODULES

import pygame # imports pygame modules into the pygame package
import os # imports operating system module
from sys import exit # imports exit from sys module
from random import randint, choice # imports randint and choice from random module

# CONSTANTS

SCORE_COLOR = (64, 64, 64) # dark grey
BOX_COLOR = '#c0e8ec' # lightblue
INTRO_COLOR = (94, 129, 162) # grayish blue
INTRO_TEXT_COLOR = (111, 196, 169) # seafoam green
FPS = pygame.time.Clock()

#  CUSTOM EVENTS

EVENT_OBSTACLE_TIMER = pygame.event.custom_type()
EVENT_SNAIL_ANIMATE_TIMER = pygame.event.custom_type()
EVENT_FLY_ANIMATE_TIMER = pygame.event.custom_type()

# DEFINE FUNCTIONS

def display_score():
    '''Displays game's score'''
    current_time = int((pygame.time.get_ticks()/ 1000) - start_time)
    score_surf = game_font.render(f'Score: {current_time}', False, SCORE_COLOR) # arg 2 sets the anti-aliasing to false
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    '''Draws and animates obstacles moving rtl across screen'''
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5 # every obstacle moved to left by tiny bit

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
                continue
            screen.blit(fly_surf, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    return []

def collisions(player, obstacles):
    '''Checks if collisions between player and obstacles are occuring'''
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    '''Animates player walking and/or jumping'''
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
        return 0
    player_index += 0.1
    if player_index >= len(player_walk):
        player_index = 0
    player_surf = player_walk[int(player_index)]
    return 0

def append_obstacle(obstacle_list):
    '''Adds obstacle to end of obstacle_list'''
    if choice((True, False)):
        return obstacle_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
    return obstacle_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))

# GAME | Initialize default game settings

pygame.init() # attempts to initialize all available pygame modules (i.e. pygame.display, pygame.event, pygame.font, pygame.image, etc)
screen = pygame.display.set_mode((800, 400)) # (w, h) 800px wide, 400px high
pygame.display.set_caption('Runner') # sets title in window tab
game_font = pygame.font.Font(os.path.join('ultimatepygameintro', 'font', 'Pixeltype.ttf'), 50)
game_active = True
start_time, score = (0, 0)

# IMAGES

sky_surf = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'Sky.png')).convert() # loads sky background
ground_surf = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'ground.png')).convert() # loads ground background
snail_frame_1 = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'snail', 'snail1.png')).convert_alpha() # loads snail1 image
snail_frame_2 = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'snail', 'snail2.png')).convert_alpha() # loads snail2 image
fly_frame_1 = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'Fly', 'Fly1.png')).convert_alpha() # loads Fly1 image
fly_frame_2 = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'Fly', 'Fly2.png')).convert_alpha() # loads Fly2 image
player_walk_1 = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'Player', 'player_walk_1.png')).convert_alpha() # loads player_walk_1 image
player_walk_2 = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'Player', 'player_walk_2.png')).convert_alpha() # loads player_walk_2 image
player_jump = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'Player', 'jump.png')).convert_alpha() # loads jump image
player_stand = pygame.image.load(os.path.join('ultimatepygameintro', 'graphics', 'Player', 'player_stand.png')).convert_alpha() # loads player_stand image

# Snail
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

# Fly
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

# Player
player_walk = [player_walk_1, player_walk_2]
player_index, player_gravity = (0, 0)
player_surf = player_walk[player_index]
player_rect = player_walk_1.get_rect(midbottom = (80, 300))

# Intro Screen
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) # angle of zoom is 0deg, scale is x2
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_title = game_font.render('Pixel Runner', False, INTRO_TEXT_COLOR)
game_title_rect = game_title.get_rect(center = (400, 80))

game_message = game_font.render('Press space to run', False, INTRO_TEXT_COLOR)
game_message_rect = game_message.get_rect(center = (400, 330))

# Timers
pygame.time.set_timer(EVENT_OBSTACLE_TIMER, 1500) #
pygame.time.set_timer(EVENT_SNAIL_ANIMATE_TIMER, 500) # Snail image alternates ever 0.5s
pygame.time.set_timer(EVENT_FLY_ANIMATE_TIMER, 200) # Fly image alternates every 0.2s

# game loop begins:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN: # if mouse cursor moves/hovers over player, player jumps (as long as player is not already in air)
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: # if user hits/holds spacebar, player jumps (as long as player is not already in air)
                    player_gravity = -20
            if event.type == EVENT_OBSTACLE_TIMER:
                append_obstacle(obstacle_rect_list)
            if event.type == EVENT_SNAIL_ANIMATE_TIMER:
                snail_frame_index = 1 if snail_frame_index == 0 else 0
            if event.type == EVENT_FLY_ANIMATE_TIMER:
                fly_frame_index = 1 if fly_frame_index == 0 else 0
            screen.blit(sky_surf, (0, 0))
            screen.blit(ground_surf, (0, 300))
            score = display_score()
            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom >= 300:
                player_rect.bottom = 300
            player_animation()
            screen.blit(player_surf, player_rect)

            # Obstacle movement
            obstacle_rect_list = obstacle_movement(obstacle_rect_list)

            # Collisions
            game_active = collisions(player_rect, obstacle_rect_list)
            continue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/ 1000)
        screen.fill(INTRO_COLOR)
        snail_rect = snail_surf.get_rect(bottomright = (600, 300))
        player_rect = player_surf.get_rect(midbottom = (80, 300))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (800, 300)
        player_gravity = 0
        score_message = game_font.render(f'Your score: {score}', False, INTRO_TEXT_COLOR)
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_message, game_message_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
            continue
        screen.blit(score_message, score_message_rect)
