import pygame, sys
from pygame.locals import *

import Globals
from Player import player
from Floors import floor
from Enemies import enemy

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

coverimage = (pygame.image.load('cover.png'))

titleimages = []
titleimages.append(pygame.image.load('title0.png'))
titleimages.append(pygame.image.load('title1.png'))
titleimages.append(pygame.image.load('title2.png'))
titleimages.append(pygame.image.load('title3.png'))

ruletop = (pygame.image.load('rules.png'))
rulebottom = (pygame.image.load('rulestext.png'))

def levelup(level):
    Globals.floors = []
    Globals.enemies = []
    if level == 1:
        Globals.play.x = 700
        Globals.play.y = 550
        Globals.goal.x = 100
        Globals.goal.y = 550
        Globals.play.lastdir = -1
        Globals.play.imgdir = -1
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(400,570,3))
    if level == 2:
        Globals.play.x = 700
        Globals.play.y = 550
        Globals.goal.x = 100
        Globals.goal.y = 550
        Globals.play.lastdir = -1
        Globals.play.imgdir = -1
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(400,595,2))
        Globals.floors.append(floor(300,595,2))
        Globals.floors.append(floor(500,595,2))
        Globals.floors.append(floor(330,530,4))
        Globals.floors.append(floor(470,530,4))
    if level == 3:
        Globals.play.x = 700
        Globals.play.y = 540
        Globals.goal.x = 700
        Globals.goal.y = 0
        Globals.play.lastdir = -1
        Globals.play.imgdir = -1
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(200,495,6))
        Globals.floors.append(floor(600,365,6))
        Globals.floors.append(floor(200,235,6))
        Globals.floors.append(floor(600,105,7))
    if level == 4:
        Globals.play.x = 700
        Globals.play.y = 540
        Globals.play.lastdir = -1
        Globals.play.imgdir = -1
        Globals.goal.x = 50
        Globals.goal.y = 0
        Globals.enemies.append(enemy(80,540,0,3.2,0,0))
        Globals.enemies.append(enemy(560,400,0,3.2,0,1))
        Globals.enemies.append(enemy(210,-330,0,2.0,0,2))
        Globals.enemies.append(enemy(50,-330,0,2.0,0,3))
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(80,570,3))
        Globals.floors.append(floor(600,420,7))
        Globals.floors.append(floor(270,445,9))
        Globals.floors.append(floor(600,280,8))
        Globals.floors.append(floor(500,150,8))
        Globals.floors.append(floor(400,30,8))
        Globals.floors.append(floor(300,-120,8))
        Globals.floors.append(floor(150,-300,5))
        Globals.floors.append(floor(50,100,8))
    if level == 5:
        Globals.play.x = 700
        Globals.play.y = 550
        Globals.play.lastdir = -1
        Globals.play.imgdir = -1
        Globals.goal.x = 100
        Globals.goal.y = -200         
        Globals.enemies.append(enemy(270,55,0,-3,0,0))
        Globals.enemies.append(enemy(270,185,0,3,0,1))
        Globals.enemies.append(enemy(270,315,0,-3,0,2))
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(250,495,5))
        Globals.floors.append(floor(650,495,5))
        Globals.floors.append(floor(450,495,1))
        Globals.floors.append(floor(550,365,5))
        Globals.floors.append(floor(150,365,5))
        Globals.floors.append(floor(350,365,1))
        Globals.floors.append(floor(250,235,5))
        Globals.floors.append(floor(650,235,5))
        Globals.floors.append(floor(450,235,1))
        Globals.floors.append(floor(550,105,5))
        Globals.floors.append(floor(150,105,5))
        Globals.floors.append(floor(350,105,1))
    if level == 6:
        Globals.play.x = 700
        Globals.play.y = 550
        Globals.play.lastdir = -1
        Globals.play.imgdir = -1
        Globals.goal.x = 260
        Globals.goal.y = 130        
        Globals.floors.append(floor(400,625,0))
        Globals.floors.append(floor(550,520,1))
        Globals.floors.append(floor(400,450,1))
        Globals.floors.append(floor(250,380,1))
        Globals.floors.append(floor(100,310,1))
        Globals.floors.append(floor(260,180,4))
        Globals.floors.append(floor(50,595,2))
        Globals.floors.append(floor(150,595,2))
        Globals.floors.append(floor(250,595,2))
        Globals.floors.append(floor(350,595,2))
        Globals.floors.append(floor(450,595,2))
    if level == 7:
        Globals.play.x = 80
        Globals.play.y = 450
        Globals.play.lastdir = 1
        Globals.play.imgdir = 1
        Globals.goal.x = 80
        Globals.goal.y = -100
        Globals.floors.append(floor(400,625,10))
        Globals.floors.append(floor(80,570,4))
        Globals.floors.append(floor(200,170,11))
        Globals.floors.append(floor(320,570,4))
        Globals.floors.append(floor(440,170,11))
        Globals.floors.append(floor(560,570,4))
        Globals.floors.append(floor(720,570,4))
        Globals.floors.append(floor(720,440,12))
        Globals.floors.append(floor(720,310,12))
        Globals.floors.append(floor(720,180,12))
        Globals.floors.append(floor(560,180,4))
        Globals.floors.append(floor(320,180,4))
        Globals.floors.append(floor(80,180,4))
        
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
        
def main():

    #main vars
    Globals.leftflag = 0
    Globals.rightflag = 0
    Globals.upflag = 0
    alive = True
    level = 6

    while alive == True: #main loop
        if Globals.hitgoal == True or Globals.restart == True or Globals.died == True:

            if Globals.hitgoal == True:
                level = min(7, level + 1) #should iterate
            
            Globals.hitgoal = False
            Globals.restart = False
            Globals.died = False
            Globals.timeclock = 0
            Globals.OFFSET = 0
            Globals.leftflag = 0
            Globals.rightflag = 0
            Globals.upflag = 0
            
            levelup(level)
        
        Globals.DISPLAYSURF.fill(WHITE) #bg

        Globals.timeclock += 1
        Globals.upflag = 0
        
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

        if Globals.play.y < Globals.SCREEN_HEIGHT/2:
            Globals.OFFSET = Globals.SCREEN_HEIGHT/2 - Globals.play.y
                   
        Globals.goal.update()
        Globals.goal.collisions()
        Globals.goal.draw()
        
        for f in Globals.floors:
            if f.lit == False:
                f.draw()
        for e in Globals.enemies:
            e.update()
            e.collisions()
            if e.lit == False:
                e.draw()
                
        if Globals.worldstatus == 1 or Globals.worldstatus == 2:
            #cover
            cover = coverimage.convert()
            cover.set_alpha((25*Globals.timeclock % 120 - 109))
            Globals.DISPLAYSURF.blit(cover, (0,0))
        if Globals.worldstatus == 3:
            #cover
            cover = coverimage.convert()
            cover.set_alpha(255)
            Globals.DISPLAYSURF.blit(cover, (0,0))

        Globals.play.update()
        Globals.play.collisions()
        Globals.play.draw()

        for f in Globals.floors:
            if f.lit == True:
                f.draw()
        for e in Globals.enemies:
            if e.lit == True:
                e.draw()
        
        #end of loop
        pygame.display.update()
        #print "FPS:", Globals.fpsClock.get_fps()
        Globals.fpsClock.tick(Globals.FPS)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------

def rules():
    d = 0

    while d == 0:
        Globals.DISPLAYSURF.fill(BLACK)
        for x in range(len(r)):
            Globals.DISPLAYSURF.blit(ruletop, (0,0))    
            Globals.DISPLAYSURF.blit(ruletop, (0,400)) 
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_r):
                    d = 1
                if (event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
        #print "FPS:", Globals.fpsClock.get_fps()
        Globals.fpsClock.tick(Globals.FPS)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------

#main menu
d = 0
menutext = "SPACE to begin, ESC to quit, R for rules"
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
            if (event.key == K_r):
                rules()              

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
    
