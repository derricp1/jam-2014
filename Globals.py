import pygame, sys
from pygame.locals import *

from Player import player
from Floors import floor
from Goal import goal
from Enemies import enemy

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

OFFSET = 0

FPS = 40
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fpsClock = pygame.time.Clock()

gravity = 1
tv = 10
jumpspeed = -12
runspeed = 7

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
enemies = []

timer = -1
cycleperiod = 60
        
