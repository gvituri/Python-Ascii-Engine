import pygame
import math
from PIL import Image
from settings import *


#Initializes PyGame
pygame.init()

#Initializes the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ASCII RENDERER')

#Gets the RGB value for background and foreground
sprite_sheet = Image.open('resources/ascii_table_16x.png')
sprite_sheet_pixel = sprite_sheet.load()
void_tile_coordinate_y = math.trunc((32/16)) * 16
void_tile_coordinate_x = (32 - void_tile_coordinate_y) * 16
full_tile_coordinate_y = math.trunc((219/16)) * 16
full_tile_coordinate_x = (219 - full_tile_coordinate_y) * 16
background_color = sprite_sheet_pixel[void_tile_coordinate_x,void_tile_coordinate_y]
foreground_color = sprite_sheet_pixel[full_tile_coordinate_x,full_tile_coordinate_y]
print(background_color)
print(foreground_color)

def get_tile_from_sheet(sheet_path, tile_index, resolution, scale):
#Gets the RGB value for background and foreground
    sprite_sheet = Image.open(sheet_path)
    sprite_sheet_pixel = sprite_sheet.load()
    void_tile_coordinate_y = math.trunc(32/16) * resolution
    void_tile_coordinate_x = (32 - (math.trunc(32/16) * 16)) * resolution
    full_tile_coordinate_y = math.trunc(219/16) * resolution
    full_tile_coordinate_x = (219 - (math.trunc(219/16) * 16)) * resolution
    background_color = sprite_sheet_pixel[void_tile_coordinate_x,void_tile_coordinate_y]
    foreground_color = sprite_sheet_pixel[full_tile_coordinate_x,full_tile_coordinate_y]
    print(background_color)
    print(foreground_color)

    sprite_sheet_game = pygame.image.load(sheet_path).convert_alpha()

    tile = pygame.Surface((resolution, resolution)).convert_alpha()

    tile_coordinate_y = math.trunc(tile_index/16) * resolution
    tile_coordinate_x = (tile_index - (math.trunc(tile_index/16) * 16)) * resolution

    tile.blit(sprite_sheet_game, (0, 0), (tile_coordinate_x ,tile_coordinate_y, resolution, resolution))
    tile = pygame.transform.scale(tile, (resolution * scale, resolution * scale))
    tile.set_colorkey(background_color)
    return tile

test_tile = get_tile_from_sheet('resources/ascii_table_16x.png', 178, 16, 1)

run = True
while run:

    #update background
    screen.fill(BACKGROUND_COLOR)

    #display image
    screen.blit(test_tile, (0 + 1, 1))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()