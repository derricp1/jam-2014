import pygame, sys
from pygame.locals import *

from Player import player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

FPS = 60
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fpsClock = pygame.time.Clock()

gravity = 9.8
jumpspeed = 50
runspeed = 4

timeclock = 0

play = player(320,400)

leftflag = 0
rightflag = 0
upflag = 0
