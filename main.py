# Import All Packages
import pygame as pg
from pygame.locals import *
import time
import random

# Call Package
pg.init()

# Declare Variables
screensize = (700,700)
fps = 0.04
bushlocations = [(random.randint(0,700), random.randint(0,700)), (random.randint(0,700), random.randint(0,700)), (random.randint(0,700), random.randint(0,700)), (random.randint(0,700), random.randint(0,700)), (random.randint(0,700), random.randint(0,700)), (random.randint(0,700), random.randint(0,700)), (random.randint(0,700), random.randint(0,700))]

# Declare Gameplay Variables
player_x, player_y = 325, 325
keydown = []

# Declare Colors
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
green_dark = (0,153,0)
green_light = (153,255,153)

# Setup Screen
screen = pg.display.set_mode(screensize)
pg.display.set_caption("Top-Down Python")

# Run Script Loop
run = True
while run:

    # Change Background
    screen.fill(green_dark)
    pg.draw.rect(screen, white, rect=(player_x, player_y, 50, 50))

    # Draw Bushes
    for i in range(len(bushlocations)):
        pg.draw.circle(screen, green_light, bushlocations[i], 50)

    # Update Frames
    pg.display.update()
    time.sleep(fps)

    # Check for Keypresses
    keydown = pg.key.get_pressed()

    # Update Player Location
    if keydown[pg.K_w]:
        player_y -= 15
    if keydown[pg.K_s]:
        player_y += 15
    if keydown[pg.K_a]:
        player_x -= 15
    if keydown[pg.K_d]:
        player_x += 15

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False