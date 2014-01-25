import pygame, sys
from pygame.locals import *

import Globals #global variables

images = []

images.append(pygame.image.load('floor0.png'))
images.append(pygame.image.load('floor1.png'))

class floor:
    def __init__(self, nx, ny, ft):
        self.x = nx
        self.y = ny
        self.dx = 0
        self.dy = 0

        self.ftype = ft

        self.image = images[self.ftype]

        self.mask = pygame.mask.from_surface(self.image)
        sizes = self.mask.get_size()
        self.sizex = sizes[0]/2.0
        self.sizey = sizes[1]/2.0

        self.lit = False
        
        if self.ftype == 0:
            self.lit = True
        else:
            self.lit = False 

    def draw(self):
        Globals.DISPLAYSURF.blit(self.image, ((self.x-self.sizex), (self.y-self.sizey))) 
