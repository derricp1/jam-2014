import pygame, sys
from pygame.locals import *

enemies = []

import Globals #global variables

enemies.append(pygame.image.load('spikeball.png'))

class enemy:
    def __init__(self, nx, ny, nty, ndx, ndy, i):    
        self.x = nx
        self.y = ny
        self.dx = ndx
        self.dy = ndy
        self.i = i

        self.image = enemies[nty]
        self.etype = nty

        self.mask = pygame.mask.from_surface(self.image)
        sizes = self.mask.get_size()
        self.sizex = sizes[0]/2.0
        self.sizey = sizes[1]/2.0

        self.rotation = 0

        self.lit = True

        if self.etype == 0:
            self.lit = True
        else:
            self.lit = False

    def update(self):
        if self.etype == 0:
            self.rotation += -5*(self.dx/abs(self.dx))
            self.x += self.dx
            #gravity
            self.dy = min(Globals.tv, self.dy + Globals.gravity)
            self.y += self.dy

            self.image = pygame.transform.rotate(enemies[self.etype],self.rotation)
            self.mask = pygame.mask.from_surface(self.image)
            sizes = self.mask.get_size()
            self.sizex = sizes[0]/2.0
            self.sizey = sizes[1]/2.0

            if self.x <= 0 or self.x >= Globals.SCREEN_WIDTH:
                self.dx = -self.dx
                self.x += self.dx

    def draw(self):
        if self.y-self.sizey+Globals.OFFSET >= 0 and self.y-self.sizey+Globals.OFFSET <= Globals.SCREEN_HEIGHT:
            Globals.DISPLAYSURF.blit(self.image, ((self.x-self.sizex), (self.y-self.sizey+Globals.OFFSET))) 

    def collisions(self):
        #platforms
        for f in Globals.floors:
            if f.lit == True or Globals.worldstatus < 3:
                if self.mask.overlap(f.mask, (int((f.x-f.sizex)-(self.x-self.sizex)), int((f.y-f.sizey)-(self.y-self.sizey)))) != None:
                    if self.y <= f.y and self.dy > 0:
                        self.y = f.y - f.sizey - self.sizey
                        self.dy = 0
                    elif self.y >= f.y and self.dy < 0:
                        self.y = f.y + f.sizey + self.sizey
                        self.dy = -0.5 * self.dy
                        
                if self.mask.overlap(f.mask, (int((f.x-f.sizex)-(self.x-self.sizex)), int((f.y-f.sizey)-(self.y-self.sizey)))) != None:
                    if self.x <= f.x and self.dx > 0:
                        self.x = f.x - f.sizex - self.sizex
                        self.dx = -self.dx
                    elif self.x >= f.x and self.dx < 0:
                        self.x = f.x + f.sizex + self.sizex
                        self.dx = -self.dx

        for e in Globals.enemies:
            if (self.i < e.i) and self.mask.overlap(e.mask, (int((e.x-e.sizex)-(self.x-self.sizex)), int((e.y-e.sizey)-(self.y-self.sizey)))) != None:
                if abs(self.x-e.x) > (self.sizex + e.sizex)/4:
                    if abs(self.dx) == abs(e.dx) or self.dx * e.dx < 0:
                        self.dx = -self.dx
                        e.dx = -e.dx
                    else:
                        if self.dx * e.dx > 0:
                            if self.dx > e.dx:
                                self.dx = -self.dx
                            else:
                                e.dx = -e.dx
                    while self.mask.overlap(e.mask, (int((e.x-e.sizex)-(self.x-self.sizex)), int((e.y-e.sizey)-(self.y-self.sizey)))) != None:
                        self.x += self.dx
                        e.x += e.dx
        
        #player
        if (f.lit == True or Globals.worldstatus < 3) and self.mask.overlap(Globals.play.eyemask, (int((Globals.play.x-Globals.play.sizex)-(self.x-self.sizex)), int((Globals.play.y-Globals.play.sizey)-(self.y-self.sizey)))) != None:
            Globals.died = True
