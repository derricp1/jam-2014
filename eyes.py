import pygame, sys
from pygame.locals import *

import Globals
from Player import player
from Floors import floor

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

coverimage = (pygame.image.load('cover.png'))

def levelup(level):
    Globals.floors = []
    if level == 1:
        Globals.play.x = 700
        Globals.play.y = 550
        Globals.goal.x = 100
        Globals.goal.y = 550
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(400,570,3))
    if level == 2:
        Globals.play.x = 700
        Globals.play.y = 550
        Globals.goal.x = 100
        Globals.goal.y = 550
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(400,595,2))
        Globals.floors.append(floor(300,595,2))
        Globals.floors.append(floor(500,595,2))
        Globals.floors.append(floor(330,530,4))
        Globals.floors.append(floor(470,530,4))
    if level == 3:
        Globals.play.x = 700
        Globals.play.y = 550
        Globals.goal.x = 260
        Globals.goal.y = 180        
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(550,520,1))
        Globals.floors.append(floor(400,450,1))
        Globals.floors.append(floor(250,380,1))
        Globals.floors.append(floor(100,310,1))
        Globals.floors.append(floor(260,230,4))
        Globals.floors.append(floor(50,595,2))
        Globals.floors.append(floor(150,595,2))
        Globals.floors.append(floor(250,595,2))
        Globals.floors.append(floor(350,595,2))
        Globals.floors.append(floor(450,595,2))
        

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
        
def main():

    #main vars
    Globals.leftflag = 0
    Globals.rightflag = 0
    Globals.upflag = 0
    alive = True
    level = 2

    while alive == True: #main loop
        if Globals.hitgoal == True or Globals.restart == True or Globals.died == True:

            if Globals.hitgoal == True:
                level = min(3, level + 1) #should iterate
            
            Globals.hitgoal = False
            Globals.restart = False
            Globals.died = False
            Globals.timeclock = 0
            
            levelup(level)
        
        Globals.DISPLAYSURF.fill(WHITE) #bg

        Globals.timeclock += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT):
                   Globals.leftflag = 1
                if (event.key == K_RIGHT):
                   Globals.rightflag = 1
                if (event.key == K_UP):
                   Globals.upflag = 1
                if (event.key == K_ESCAPE):
                    alive = False           
            elif event.type == KEYUP:
                if (event.key == K_LEFT):
                   Globals.leftflag = 0
                if (event.key == K_RIGHT):
                   Globals.rightflag = 0
                if (event.key == K_UP):
                   Globals.upflag = 0
                   
        Globals.goal.update()
        Globals.goal.draw()
        Globals.goal.collisions()
        
        for f in Globals.floors:
            if f.lit == False:
                f.draw()
                
        if Globals.worldstatus == 1 or Globals.worldstatus == 2:
            #cover
            cover = pygame.transform.scale(coverimage,(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
            cover = cover.convert()
            cover.set_alpha((25*Globals.timeclock % 120 - 109))
            Globals.DISPLAYSURF.blit(cover, (0,0))
        if Globals.worldstatus == 3:
            #cover
            cover = pygame.transform.scale(coverimage,(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
            cover = cover.convert()
            cover.set_alpha(255)
            Globals.DISPLAYSURF.blit(cover, (0,0))

        Globals.play.update()
        Globals.play.collisions()
        Globals.play.draw()

        for f in Globals.floors:
            if f.lit == True:
                f.draw()
        
        #end of loop
        pygame.display.update()
        #print "FPS:", Globals.fpsClock.get_fps()
        Globals.fpsClock.tick(Globals.FPS)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------

#main menu
d = 0
menutext = "SPACE to begin, ESC to quit"
font = pygame.font.Font(None, 48)

while d == 0:
    Globals.DISPLAYSURF.fill(BLACK)
    text = font.render(menutext, 1, WHITE)
    textpos = text.get_rect()
    textpos.centerx = (Globals.DISPLAYSURF.get_rect().centerx)
    textpos.centery = (Globals.DISPLAYSURF.get_rect().centery)*1.5
    Globals.DISPLAYSURF.blit(text, textpos)    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_SPACE):
                d = 1
            if (event.key == K_ESCAPE):
                d = -1

    pygame.display.update()
    #print "FPS:", Globals.fpsClock.get_fps()
    Globals.fpsClock.tick(Globals.FPS)

if d == -1:
    pygame.quit()
    sys.exit()
if d == 1:
    main()
    pygame.quit()
    sys.exit()
    
