import pygame, sys
from pygame.locals import *

from Player import player
from Floors import floor
from Goal import goal

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

FPS = 60
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fpsClock = pygame.time.Clock()

gravity = 1
tv = 10
jumpspeed = -12.5
runspeed = 4

timeclock = 0
worldstatus = 0

play = player(320,400)
goal = goal(100,500)
hitgoal = True
restart = False
died = False

leftflag = 0
rightflag = 0
upflag = 0

floors = []
        
