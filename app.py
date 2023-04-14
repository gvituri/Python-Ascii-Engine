import pygame
import math
from settings import *

#Initializes PyGame
pygame.init()

#Initializes the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ASCII RENDERER')

#Initializes the sprite sheet
sprite_sheet_8x = pygame.image.load('resources/ascii_table_8x.png').convert_alpha()
sprite_sheet_16x = pygame.image.load('resources/ascii_table_16x.png').convert_alpha()

def get_tile_from_sheet(sheet, tile_index, resolution, scale, background_color):
    tile = pygame.Surface((resolution, resolution)).convert_alpha()

    tile_coordinate_y = math.trunc((tile_index/16)) * 16
    tile_coordinate_x = (tile_index - tile_coordinate_y) *16

    tile.blit(sheet, (0, 0), (tile_coordinate_x ,tile_coordinate_y, resolution, resolution))
    tile = pygame.transform.scale(tile, (resolution * scale, resolution * scale))
    tile.set_colorkey(background_color)
    return tile

test_tile = get_tile_from_sheet(sprite_sheet_16x, 172, 16, 5, (255, 0, 255))

run = True
while run:

    #update background
    screen.fill(BACKGROUND_COLOR)

    #display image
    screen.blit(test_tile, (0, 0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()