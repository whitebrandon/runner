import pygame
from sys import exit 
from random import randint

TEXT_COLOR = (64,64,64)
BOX_COLOR = '#c0e8ec'
INTRO_COLOR = (94, 129, 162)

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) /1000)
    score_surf = test_font.render(f'Score: {current_time}', False, TEXT_COLOR)
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time 

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5 # every obstacle moved to left by tiny bit

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

            # screen.blit(snail_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: 
        return []

# def collisions(player,obstacles):
# 	if obstacles:
# 		for obstacle_rect in obstacles:
# 			if player.colliderect(obstacle_rect): return False
# 	return True

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump # jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)] # walk
    # play walking animation if the player is on floor
    # display the jump surface when player is not on floor

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
fps = pygame.time.Clock()
test_font = pygame.font.Font('ultimatepygameintro/font/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0

sky_surf = pygame.image.load('ultimatepygameintro/graphics/Sky.png').convert()
ground_surf = pygame.image.load('ultimatepygameintro/graphics/ground.png').convert()

# score_surf = test_font.render('My game', False, TEXT_COLOR)
# score_rect = score_surf.get_rect(center = (400, 50))

# Obstacles

# Snail
snail_frame_1 = pygame.image.load('ultimatepygameintro/graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('ultimatepygameintro/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]
# snail_rect = snail_surf.get_rect(bottomright = (600, 300)) # Don't need anymore

# Fly
fly_frame_1 = pygame.image.load('ultimatepygameintro/graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('ultimatepygameintro/graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]


obstacle_rect_list = []


player_walk_1 = pygame.image.load('ultimatepygameintro/graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('ultimatepygameintro/graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0 # use it to pick surface b/w player_walk_1 and player_walk_2
player_jump = pygame.image.load('ultimatepygameintro/graphics/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_walk_1.get_rect(midbottom = (80, 300))
player_gravity = 0
# player_walk = 0

# Intro screen
player_stand = pygame.image.load('ultimatepygameintro/graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1 # add plus one because some events are already reserved, so we add plus one to avoid
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


# def playerFall(rect, gravity):
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_SPACE]:
#         return
#     if rect.y < 217:
#         gravity += 1
#         rect.y += gravity

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                # if event.key == pygame.K_RIGHT:
                #     player_walk += 2
                # if event.key == pygame.K_LEFT:
                #     player_walk -= 2
            # if event.type == pygame.KEYUP:
                # if event.key == pygame.K_RIGHT:
                #     player_walk -= 2
                # if event.key == pygame.K_LEFT:
                #     player_walk += 2

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = pygame.time.get_ticks()
        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2): # 0 = true 1 = false
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                   snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surf, (0,0)) 
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, BOX_COLOR, score_rect, 10) # first we say we want to draw, then we specify what shape we want to draw
        # pygame.draw.rect(screen, BOX_COLOR, score_rect)

        # screen.blit(score_surf, score_rect)

        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800

        # screen.blit(snail_surf, snail_rect)
        
        # Player
        # if player_rect.y < 217:
        #   playerFall(player_rect, player_gravity)

        player_gravity += 1
        player_rect.y += player_gravity
        # player_rect.x += player_walk
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        # if snail_rect.colliderect(player_rect):
        #     game_active = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     pass

        # if player_rect.colliderect(snail_rect):
        #     pass

        game_active = collisions(player_rect, obstacle_rect_list)
    else:
        screen.fill(INTRO_COLOR)
        snail_rect = snail_surf.get_rect(bottomright = (600, 300))
        player_rect = player_surf.get_rect(midbottom = (80, 300))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else: 
            screen.blit(score_message, score_message_rect)


    pygame.display.update()
    fps.tick(60)
    