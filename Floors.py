import pygame, sys
from pygame.locals import *

import Globals #global variables

images = []

images.append(pygame.image.load('floor0.png'))
images.append(pygame.image.load('floor1.png'))
images.append(pygame.image.load('floor2.png'))
images.append(pygame.image.load('floor3.png'))
images.append(pygame.image.load('floor4.png'))
images.append(pygame.image.load('floor5.png'))
images.append(pygame.image.load('floor6.png'))
images.append(pygame.image.load('floor7.png'))
images.append(pygame.image.load('floor8.png'))
images.append(pygame.image.load('floor9.png'))
images.append(pygame.image.load('floor10.png'))
images.append(pygame.image.load('floor11.png'))
images.append(pygame.image.load('floor12.png'))

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

        self.deadly = False
        self.lit = False
        
        if self.ftype == 0 or self.ftype == 10 or self.ftype == 3 or self.ftype == 2 or self.ftype == 4 or self.ftype == 5 or self.ftype == 7 or self.ftype == 8:
            self.lit = True
        else:
            self.lit = False

        if self.ftype == 2 or self.ftype == 10:
            self.deadly = True
        else:
            self.deadly = False        
            

    def draw(self):
        Globals.DISPLAYSURF.blit(self.image, ((self.x-self.sizex), (self.y-self.sizey+Globals.OFFSET))) 
