import pygame, sys
from pygame.locals import *

import Globals #global variables

image = pygame.image.load('clock.png')

class goal:
    def __init__(self, nx, ny):
        self.x = nx
        self.y = ny
        self.dy = 0

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        sizes = self.mask.get_size()
        self.sizex = sizes[0]/2.0
        self.sizey = sizes[1]/2.0

    def draw(self):
        Globals.DISPLAYSURF.blit(self.image, ((self.x-self.sizex), (self.y-self.sizey+Globals.OFFSET))) 

    def update(self):
        self.dy = min(Globals.tv, self.dy + Globals.gravity)
        self.y += self.dy


    def collisions(self):
        #platforms
        for f in Globals.floors:
            if f.lit == True or Globals.worldstatus < 3:
                if self.mask.overlap(f.mask, (int((f.x-f.sizex)-(self.x-self.sizex)), int((f.y-f.sizey)-(self.y-self.sizey)))) != None:
                    if self.y <= f.y: #ends a jump
                        self.y = f.y - f.sizey - self.sizey
                    else:
                        self.y = f.y + f.sizey + self.sizey
                if self.mask.overlap(f.mask, (int((f.x-f.sizex)-(self.x-self.sizex)), int((f.y-f.sizey)-(self.y-self.sizey)))) != None:
                    if self.x <= f.x:
                        self.x = f.x - f.sizex - self.sizex
                    else:
                        self.x = f.x + f.sizex + self.sizex
