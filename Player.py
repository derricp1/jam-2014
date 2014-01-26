import pygame, sys
from pygame.locals import *

import Globals #global variables

legs = []
body = []

legs.append(pygame.image.load('legball.png'))
legs.append(pygame.image.load('centerball.png'))

body.append(pygame.image.load('eyeopen.png'))
body.append(pygame.image.load('eyedroopy.png'))
body.append(pygame.image.load('eyetired.png'))
body.append(pygame.image.load('eyeclosed.png'))

class player:
    def __init__(self, nx, ny):
        self.x = nx
        self.y = ny
        self.dx = 0
        self.dy = 0

        self.lastdir = 1
        self.imgdir = 1
        
        self.jumping = False

        self.eyestate = 0 #important for visual stuff
        self.legstate = 0 #animation only

        self.eyeimage = body[self.eyestate]
        self.legimage = legs[self.legstate]

        self.eyemask = pygame.mask.from_surface(self.eyeimage)
        self.legmask = pygame.mask.from_surface(self.legimage)
        sizes = self.eyemask.get_size()
        self.sizex = sizes[0]/2.0
        self.sizey = sizes[1]/2.0

        self.playerlevel = 1
        self.legcount = 0

    def update(self):
        if self.dx > 0:
            self.lastdir = 1
        elif self.dx < 0:
            self.lastdir = -1

        if Globals.upflag == 1 and self.jumping == False:
            self.jumping = True
            self.dy = Globals.jumpspeed
        if self.dy > 0:
            self.jumping = True

        #gravity
        self.dy = min(Globals.tv, self.dy + Globals.gravity)          

        if Globals.leftflag == 1 and Globals.rightflag == 0:
            self.dx = -Globals.runspeed
        elif Globals.leftflag == 0 and Globals.rightflag == 1:
            self.dx = Globals.runspeed
        else:
            self.dx = 0

        self.x += self.dx
        self.y += self.dy
        self.y += self.dy

        if self.x < self.sizex:
            self.x = self.sizex
        if self.x > Globals.SCREEN_WIDTH - self.sizex:
            self.x = Globals.SCREEN_WIDTH - self.sizex  
        
        #blinking
        if self.playerlevel == 1:
            cycleperiod = 60
            if Globals.timeclock % cycleperiod <= 42:
                self.eyestate = 0
            if Globals.timeclock % cycleperiod > 42 and Globals.timeclock % cycleperiod <= 45:
                self.eyestate = 1
            if Globals.timeclock % cycleperiod > 45 and Globals.timeclock % cycleperiod <= 48:
                self.eyestate = 2
            if Globals.timeclock % cycleperiod > 48:
                self.eyestate = 3


        Globals.worldstatus = self.eyestate

        if abs(self.dx) > 0:
            self.legcount += 1
            if self.legcount == 6:
                self.legcount = 0
                self.legstate += 1
                self.legstate = self.legstate % 2
        else:
            self.legstate = 0
            

        #update eye/leg image
        self.eyeimage = body[self.eyestate]
        self.legimage = legs[self.legstate]

        if self.dx * self.lastdir < 0:
            self.imgdir = -1 * self.imgdir

        if self.imgdir == -1:
            self.eyeimage = pygame.transform.flip(body[self.eyestate], 1, 0)
            self.legimage = pygame.transform.flip(legs[self.legstate], 1, 0)            
        
        self.eyemask = pygame.mask.from_surface(self.eyeimage)
        self.legmask = pygame.mask.from_surface(self.legimage)
        sizes = self.eyemask.get_size()
        self.sizex = sizes[0]/2.0
        self.sizey = sizes[1]/2.0

        if self.y > Globals.SCREEN_HEIGHT: #safety
            Globals.restart = True
                

    def draw(self):
        Globals.DISPLAYSURF.blit(self.eyeimage, ((self.x-self.sizex), (self.y-self.sizey+Globals.OFFSET))) 
        Globals.DISPLAYSURF.blit(self.legimage, ((self.x-self.sizex), (self.y-self.sizey+Globals.OFFSET)))
        
    def collisions(self):
        #platforms
        for f in Globals.floors:
            if f.lit == True or Globals.worldstatus < 3:
                if self.eyemask.overlap(f.mask, (int((f.x-f.sizex)-(self.x-self.sizex)), int((f.y-f.sizey)-(self.y-self.sizey)))) != None:
                    if self.y <= f.y-f.sizey and ((self.x+self.sizex >= f.x-f.sizex and f.dx >= 0) or (f.x-self.sizex <= f.x+f.sizex and self.dx <= 0)): #trying to land on top
                        self.y = f.y - f.sizey - self.sizey
                        self.dy = 0
                        if f.deadly == True:
                           Globals.died = True
                        self.jumping = False
                    elif self.y >= f.y+f.sizey and ((self.x+self.sizex >= f.x-f.sizex and self.dx >= 0) or (self.x-self.sizex <= f.x+f.sizex and self.dx <= 0)): #trying to bounce off bottom
                        self.y = f.y + f.sizey + self.sizey
                        self.dy = 0
                    elif (self.y > f.y-f.sizey or self.y < f.y+f.sizey) and (self.x + self.sizex > f.x - f.sizex and self.x <= f.x) and self.dx >= 0:
                        self.x = f.x - f.sizex - self.sizex
                    elif (self.y > f.y-f.sizey or self.y < f.y+f.sizey) and (self.x - self.sizex < f.x + f.sizex and self.x >= f.x) and self.dx <= 0:
                        self.x = f.x + f.sizex + self.sizex       

        if self.eyemask.overlap(Globals.goal.mask, (int((Globals.goal.x-Globals.goal.sizex)-(self.x-self.sizex)), int((Globals.goal.y-Globals.goal.sizey)-(self.y-self.sizey)))) != None:
            Globals.hitgoal = True
