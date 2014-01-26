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
titlebottom = (pygame.image.load('titletext.png'))

end1 = (pygame.image.load('end1.png'))
end2 = (pygame.image.load('end2.png'))

ruletop = (pygame.image.load('rules.png'))
rulebottom = (pygame.image.load('rulestext.png'))

life = (pygame.image.load('life.png'))
back = (pygame.image.load('back.png'))

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
    if level == 8:
        Globals.timer = 0
        Globals.play.playerlevel = 2
        Globals.cycleperiod = 60
        Globals.play.x = 30
        Globals.play.y = 550
        Globals.play.lastdir = 1
        Globals.play.imgdir = 1
        Globals.goal.x = 150
        Globals.goal.y = -600
        Globals.enemies.append(enemy(700,-230,0,-2,0,0))
        Globals.enemies.append(enemy(450,-230,0,-2,0,2))
        Globals.enemies.append(enemy(200,-230,0,-2,0,1)) 
        Globals.floors.append(floor(400,625,10))
        Globals.floors.append(floor(30,570,8))
        Globals.floors.append(floor(200,570,6))
        Globals.floors.append(floor(430,570,8))
        Globals.floors.append(floor(510,430,9))
        Globals.floors.append(floor(590,290,9))
        Globals.floors.append(floor(670,190,9))
        Globals.floors.append(floor(770,110,8))
        Globals.floors.append(floor(0,30,7))
        Globals.floors.append(floor(400,30,7))
        Globals.floors.append(floor(30,-110,9))
        Globals.floors.append(floor(300,-200,7))
        Globals.floors.append(floor(700,-200,7))
        Globals.floors.append(floor(700,-330,9))
        Globals.floors.append(floor(400,-440,6))
        Globals.floors.append(floor(150,-550,8))
    if level == 9:
        Globals.timer = 0
        Globals.play.playerlevel = 2
        Globals.cycleperiod = 60
        Globals.play.x = 30
        Globals.play.y = 550
        Globals.play.lastdir = 1
        Globals.play.imgdir = 1
        Globals.goal.x = 50
        Globals.goal.y = -880
        Globals.floors.append(floor(400,625,10))
        Globals.floors.append(floor(30,570,8))
        Globals.floors.append(floor(215,570,8))
        Globals.floors.append(floor(400,570,8))
        Globals.floors.append(floor(500,430,9))
        Globals.floors.append(floor(500,290,9))
        Globals.floors.append(floor(500,150,9))
        Globals.floors.append(floor(500,10,9))    
        Globals.floors.append(floor(500,-140,9))
        Globals.floors.append(floor(500,-280,9))
        Globals.floors.append(floor(500,-420,9))
        Globals.floors.append(floor(500,-540,9))
        Globals.floors.append(floor(350,-540,8))
        Globals.floors.append(floor(200,-540,9))
        Globals.floors.append(floor(50,-540,8))
    if level == 10:        
        Globals.timer = 0
        Globals.play.playerlevel = 3
        Globals.cycleperiod = 60
        Globals.play.x = 30
        Globals.play.y = 550
        Globals.goal.x = 620
        Globals.goal.y = -250
        Globals.play.lastdir = 1
        Globals.play.imgdir = 1
        Globals.enemies.append(enemy(350,540,0,3,0,0))
        Globals.enemies.append(enemy(500,540,0,-4,0,1))
        Globals.enemies.append(enemy(600,540,0,-2,0,2))
        Globals.enemies.append(enemy(550,270,0,5,0,3))
        Globals.enemies.append(enemy(350,270,0,-3,0,4))
        Globals.enemies.append(enemy(200,270,0,4,0,5))
        Globals.enemies.append(enemy(330,10,0,-3,0,6))
        Globals.enemies.append(enemy(180,10,0,4,0,7))
        Globals.enemies.append(enemy(510,10,0,-5,0,8))
        Globals.floors.append(floor(400,625,10))
        Globals.floors.append(floor(30,570,8))
        Globals.floors.append(floor(770,570,8))
        Globals.floors.append(floor(400,570,13))
        Globals.floors.append(floor(100,515,14))
        Globals.floors.append(floor(700,515,14))
        Globals.floors.append(floor(770,440,9))
        Globals.floors.append(floor(770,310,9))
        Globals.floors.append(floor(400,310,13))
        Globals.floors.append(floor(100,255,14))
        Globals.floors.append(floor(700,255,14))
        Globals.floors.append(floor(30,310,9))
        Globals.floors.append(floor(30,180,9))
        Globals.floors.append(floor(30,50,9))
        Globals.floors.append(floor(400,50,13))
        Globals.floors.append(floor(100,-5,14))
        Globals.floors.append(floor(700,-5,14))
        Globals.floors.append(floor(770,50,9))
        Globals.floors.append(floor(770,-80,9))
        Globals.floors.append(floor(770,-210,9))
        Globals.floors.append(floor(620,-210,8))
    if level == 11:
        Globals.timer = 0
        Globals.play.playerlevel = 3
        Globals.cycleperiod = 60
        Globals.play.x = 30
        Globals.play.y = 550
        Globals.goal.x = 30
        Globals.goal.y = 20
        Globals.play.lastdir = 1
        Globals.play.imgdir = 1
        Globals.enemies.append(enemy(490,90,0,7,0,0))
        Globals.floors.append(floor(400,625,10))
        Globals.floors.append(floor(30,570,8))
        Globals.floors.append(floor(150,170,11))
        Globals.floors.append(floor(230,555,14))
        Globals.floors.append(floor(320,170,11))        
        Globals.floors.append(floor(410,555,14))
        Globals.floors.append(floor(530,470,9))
        Globals.floors.append(floor(620,380,9))
        Globals.floors.append(floor(730,280,9))
        Globals.floors.append(floor(690,170,9))
        Globals.floors.append(floor(620,105,14))
        Globals.floors.append(floor(580,150,8))
        Globals.floors.append(floor(520,150,8))
        Globals.floors.append(floor(460,150,8))
        Globals.floors.append(floor(400,150,8))
        Globals.floors.append(floor(360,105,14))
        Globals.floors.append(floor(230,300,9))
        Globals.floors.append(floor(100,220,9))
        Globals.floors.append(floor(100,100,9))
        Globals.floors.append(floor(30,80,8))
        
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
        
def main():

    pygame.mixer.music.load('jump.ogg')

    #main vars
    Globals.leftflag = 0
    Globals.rightflag = 0
    Globals.upflag = 0
    alive = True
    level = 0
    lives = 3 #don't run out!
    abort = False

    while alive == True: #main loop
        if Globals.hitgoal == True or Globals.restart == True or Globals.died == True:

            if Globals.hitgoal == True:
                level = level + 1 #should iterate
            else:
                lives -= 1
            
            Globals.hitgoal = False
            Globals.restart = False
            Globals.died = False
            Globals.timeclock = 0
            Globals.OFFSET = 0
            Globals.leftflag = 0
            Globals.rightflag = 0
            Globals.upflag = 0
            if Globals.timer > -1:
                Globals.timer = 0
            Globals.cycleperiod = 60
            
            
            if lives == 0 or level > 11:
                alive = False
            else:
                levelup(level)

        if alive == True:
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
                        abort = True
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

            if Globals.timer >= 0:
                Globals.timer += 1

            #draw life
            Globals.DISPLAYSURF.blit(life, (0,0))                
            if lives > 1:
                Globals.DISPLAYSURF.blit(life, (80,0))
            if lives > 2:
                Globals.DISPLAYSURF.blit(life, (160,0))
            
            #end of loop
            pygame.display.update()
            #print "FPS:", Globals.fpsClock.get_fps()
            Globals.fpsClock.tick(Globals.FPS)

    #display the fail or win screen
    d = 0
    while d == 0 and abort == False:
        if lives == 0:
            Globals.DISPLAYSURF.blit(end1, (0,0))
        else:
            Globals.DISPLAYSURF.blit(end2, (0,0))
        
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

def rules():
    d = 0

    while d == 0:
        Globals.DISPLAYSURF.fill(BLACK)
        Globals.DISPLAYSURF.blit(ruletop, (0,0))    
        Globals.DISPLAYSURF.blit(rulebottom, (0,320)) 
        
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
frame = 0

while d == 0:
    Globals.DISPLAYSURF.fill(BLACK)
    if frame % 120 < 30:
        Globals.DISPLAYSURF.blit(titleimages[0], (0,0))
    elif frame % 120 < 60:
        Globals.DISPLAYSURF.blit(titleimages[1], (0,0))
    elif frame % 120 < 90:
        Globals.DISPLAYSURF.blit(titleimages[2], (0,0))
    else:
        Globals.DISPLAYSURF.blit(titleimages[3], (0,0)) 
    
    Globals.DISPLAYSURF.blit(titlebottom, (0,320))    
    
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

    frame += 1
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
    
