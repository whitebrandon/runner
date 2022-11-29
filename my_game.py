import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
fps = pygame.time.Clock()
test_font = pygame.font.Font('ultimatepygameintro/font/Pixeltype.ttf', 50)
# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')
sky_surface = pygame.image.load('ultimatepygameintro/graphics/Sky.png').convert()
ground_surface = pygame.image.load('ultimatepygameintro/graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')
snail_surface = pygame.image.load('ultimatepygameintro/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    screen.blit(sky_surface, (0,0)) # blit stands for [bl]ock [i]mage [t]ransfer
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 100))
    snail_x_pos -= 4
    if snail_x_pos < -4:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    # update everything
    pygame.display.update()
    fps.tick(45)