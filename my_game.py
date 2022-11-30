import pygame
from sys import exit 

TEXT_COLOR = (64,64,64)
BOX_COLOR = '#c0e8ec'

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
fps = pygame.time.Clock()
test_font = pygame.font.Font('ultimatepygameintro/font/Pixeltype.ttf', 50)


sky_surf = pygame.image.load('ultimatepygameintro/graphics/Sky.png').convert()
ground_surf = pygame.image.load('ultimatepygameintro/graphics/ground.png').convert()

score_surf = test_font.render('My game', False, TEXT_COLOR)
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('ultimatepygameintro/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('ultimatepygameintro/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

def playerFall(rect, gravity):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        return
    if rect.y < 217:
        gravity += 1
        rect.y += gravity

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    screen.blit(sky_surf, (0,0)) 
    screen.blit(ground_surf, (0, 300))
    pygame.draw.rect(screen, BOX_COLOR, score_rect, 10) # first we say we want to draw, then we specify what shape we want to draw
    pygame.draw.rect(screen, BOX_COLOR, score_rect)

    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surf, snail_rect)
    
    # Player
    if player_rect.y < 217:
        playerFall(player_rect, player_gravity)

    screen.blit(player_surf, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     pass

    if player_rect.colliderect(snail_rect):
        pass

    pygame.display.update()
    fps.tick(60)