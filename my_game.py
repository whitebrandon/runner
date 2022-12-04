import pygame
from sys import exit 

TEXT_COLOR = (64,64,64)
BOX_COLOR = '#c0e8ec'
INTRO_COLOR = (94, 129, 162)

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) /1000)
    score_surf = test_font.render(f'Score: {current_time}', False, TEXT_COLOR)
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
fps = pygame.time.Clock()
test_font = pygame.font.Font('ultimatepygameintro/font/Pixeltype.ttf', 50)
game_active = True
start_time = 0


sky_surf = pygame.image.load('ultimatepygameintro/graphics/Sky.png').convert()
ground_surf = pygame.image.load('ultimatepygameintro/graphics/ground.png').convert()

# score_surf = test_font.render('My game', False, TEXT_COLOR)
# score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('ultimatepygameintro/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('ultimatepygameintro/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0
player_walk = 0

# Intro screen
player_stand = pygame.image.load('ultimatepygameintro/graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
                if event.key == pygame.K_RIGHT:
                    player_walk += 2
                if event.key == pygame.K_LEFT:
                    player_walk -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player_walk -= 2
                if event.key == pygame.K_LEFT:
                    player_walk += 2

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surf, (0,0)) 
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, BOX_COLOR, score_rect, 10) # first we say we want to draw, then we specify what shape we want to draw
        # pygame.draw.rect(screen, BOX_COLOR, score_rect)

        # screen.blit(score_surf, score_rect)

        display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800

        screen.blit(snail_surf, snail_rect)
        
        # Player
        # if player_rect.y < 217:
        #   playerFall(player_rect, player_gravity)

        player_gravity += 1
        player_rect.y += player_gravity
        player_rect.x += player_walk
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surf, player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     pass

        # if player_rect.colliderect(snail_rect):
        #     pass
    else:
        screen.fill(INTRO_COLOR)
        snail_rect = snail_surf.get_rect(bottomright = (600, 300))
        player_rect = player_surf.get_rect(midbottom = (80, 300))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)


    pygame.display.update()
    fps.tick(60)
    