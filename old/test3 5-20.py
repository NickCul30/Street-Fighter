#FinalProject.py
#Nicholas Culmone

from pygame import *
from math import *
from random import *

global player1,p1hitbox,p1attbox,attack1,attack2,p1sprite,waiting,waittime

player1 = [True,True,False,False,True,False,False]
player2 = [False,True,False,False,True,False,False]
#facing right, can att, is att, character, on ground, y-velocity, moving

RIGHT = 0
CANATT = 1
ISATT = 2
CHAR = 3
ONGROUND = 4
VEL = 5
MOVING = 6

p1hitbox = [100,400,100,200] #x,y,width,height
p1attbox = [False,False,False,False] #x,y,wid,hei
p1hit = Rect(p1hitbox)
p1att = Rect(p1attbox)

p2hitbox = [100,200,100,200] #x,y,width,height
p2attbox = [False,False,False,False] #x,y,wid,hei
p2hit = Rect(p2hitbox)
p2att = Rect(p2attbox)

X = 0
Y = 1
WID  = 2
HEI = 3

attack1 = [0,0,False] #times played, sprite #, doing attack
attack2 = [0,0,False] #times played, sprite #, doing attack

TIMES = 0
SPRITE = 1
DOING = 2

att1spr = [(255,255,6),(255,6,255),(6,255,6),(6,6,255),(255,6,6)] #sprites
att2spr = [(202,75,215),(170,6,88),(6,201,187)] #sprites

p1sprite = (0,0,0)
ground = Rect(0,600,2000,1000)

waiting = False
waittime = False

myClock = time.Clock()
screen = display.set_mode((1024,768))

player1[CHAR] = "dipper"


def move(keys,x,y,attacking):
    if keys[ord("w")] == 1 and attacking == False and player1[ONGROUND] == True: #CHANGE TO ELIF
        player1[ONGROUND] = False
        player1[VEL] = 15
        return (x,y)
    if keys[ord("a")] == 1 and keys[ord("d")] == 1 and attacking == False:
        return (x,y)
    elif keys[ord("a")] == 1 and attacking == False:
        player1[RIGHT] = False
        return (x-5,y)
    elif keys[ord("d")] == 1 and attacking == False:
        player1[RIGHT] = True
        return (x+5,y)
    else: return (x,y)


def p1StartAtt(key):
    if key == "t" and player1[CANATT] == True and player1[ISATT] == False and player1[CHAR] == "dipper":
        player1[CANATT] = False
        player1[ISATT] = True
        attack1[DOING] = True
        attack1[TIMES] = 0
        p1hitbox[X],p1hitbox[Y] = p1hitbox[X]-50,p1hitbox[Y]+100
        p1hitbox[WID],p1hitbox[HEI] = 200,100

    if key == "y" and player1[CANATT] == True and player1[ISATT] == False and player1[CHAR] == "dipper":
        player1[CANATT] = False
        player1[ISATT] = True
        attack2[DOING] = True
        attack2[TIMES] = 0
        p1hitbox[WID],p1hitbox[HEI] = 100,200


def drawPlayer1(screen,x,y,wid,hei,sprite,facing):
    draw.rect(screen,sprite,(x,y,wid,hei),2)





running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    keys = key.get_pressed()
    
    screen.fill((0,0,0))
    draw.rect(screen,(255,255,255),ground)

    #====================================================================================
    #RUN MOVEMENT FUNCTION
    
    if keys[ord("w")] == 1 or keys[ord("a")] == 1 or keys[ord("d")] == 1:
        p1hitbox[X],p1hitbox[Y] = move(keys,p1hitbox[X],p1hitbox[Y],
                                       player1[ISATT])
    #====================================================================================
    #WHILE ATTACKS ARE RUNNING
        
    if attack1[DOING] == True:
        attack1[SPRITE] = attack1[TIMES]//24
        p1sprite = att1spr[attack1[SPRITE]]
        attack1[TIMES] += 1
        waittime = 180
        for i in range(0,4): p1attbox[i] = p1hitbox[i]
        if attack1[TIMES] == 120:
            attack1[TIMES] = 0
            attack1[DOING] = False
            player1[ISATT] = False
            p1attbox = [False,False,False,False]
            
            p1hitbox[X],p1hitbox[Y] = p1hitbox[X]+50,p1hitbox[Y]-100
            p1hitbox[WID],p1hitbox[HEI] = 100,200


    if attack2[DOING] == True:
        attack2[SPRITE] = attack2[TIMES]//20
        p1sprite = att2spr[attack2[SPRITE]]
        attack2[TIMES] += 1
        waittime = 100
        
        if player1[RIGHT] == True:
            p1attbox[X],p1attbox[Y] = p1hitbox[X],p1hitbox[Y]
        else:
            p1attbox[X],p1attbox[Y] = p1hitbox[X]-100,p1hitbox[Y]
            
        p1attbox[WID],p1attbox[HEI] = 200,100
        if attack2[TIMES] == 60:
            attack2[TIMES] = 0
            attack2[DOING] = False
            player1[ISATT] = False
            p1attbox = [False,False,False,False]
            
    #====================================================================================
            
    p1hit = Rect(p1hitbox)
    p1att = Rect(p1attbox)
    p2hit = Rect(p2hitbox)
    p2att = Rect(p2attbox)

    if waiting == waittime:
        player1[CANATT] = True
        waittime = False
        waiting = False
    else:
        waiting += 1

    if player1[ONGROUND] == False:
        player1[VEL] -= 1
        p1hitbox[Y] -= player1[VEL]
        p1hit = Rect(p1hitbox)
        if p1hit.colliderect((ground)):
            player1[Y] += 10
            player1[ONGROUND] = True

    if keys[ord("t")] == 1:
        p1StartAtt("t")
    elif keys[ord("y")] == 1:
        p1StartAtt("y")


    if player1[ISATT] == True: #temp VVV
        draw.rect(screen,(255,0,0),(p1attbox[0],p1attbox[1],p1attbox[2],
                                    p1attbox[3]))
    else:
        p1sprite = (255,255,255)
    
    drawPlayer1(screen,p1hitbox[X],p1hitbox[Y],p1hitbox[WID],
                p1hitbox[HEI],p1sprite,player1[RIGHT])
    
    myClock.tick(60)
    display.flip()
quit()
