import pygame
from pygame import *

pygame.init()

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400

WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')

background_img = image.load('restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, (WINDOW_RES))

pizza_img = image.load('vampire.png')
pizza_surf =  Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))

GAME_WINDOW.blit(VAMPIRE_PIZZA, (0, 0))
GAME_WINDOW.blit(BACKGROUND, (0, 0))

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False

    display.update()

pygame.quit()


#import pygame
#from pygame import*

#pygame.init()

#WINDOW_WIDTH = 900
#WINDOW_HEIGHT = 400
#WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#GAME_WINDOW = display.set_mode(WINDOW_RES)
#display.set_caption('Attack of the Vampire Pizzas!')

#background_img = image.load('restaurant.jpg')
#background_surf = Surface.convert_alpha(background_img)
#BACKGROUND = transform.scale(background__surf,(WINDOW_RES))
#pizza_img = image.load('vampire.png')
#pizza_surf = Surface.convert_alpha(pizza_img)
#VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))

#GAME_WINDOW.blit(CAT_SPRITE, (900, 400))
#GAME_WINDOW.blit(BACKGROUND, (0,0))
#GAME_WINDOW.blit(VAMPIRE_PIZZA, (700, 300))

#game_running = True
#while game_running:

    #for event in pygame.event.get():

        #if event.type == QUIT:
            #game_running = False

    #.update()


#pygame.quit()

