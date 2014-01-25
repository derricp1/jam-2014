import pygame, sys
from pygame.locals import *

import Globals
from Player import player

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

def main():

    #main vars
    Globals.leftflag = 0
    Globals.rightflag = 0
    Globals.upflag = 0
    alive = True

    while alive == True: #main loop
        Globals.DISPLAYSURF.fill(WHITE)

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
                    alive = false           
            elif event.type == KEYUP:
                if (event.key == K_LEFT):
                   Globals.leftflag = 0
                if (event.key == K_RIGHT):
                   Globals.rightflag = 0
                if (event.key == K_UP):
                   Globals.upflag = 0

        Globals.play.update()
        Globals.play.draw()
        
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
    
