#FinalProject.py
#Nicholas Culmone

from pygame import *
from math import *
from random import *

def loadimages():
    
    if player1[CHAR] == "ryu" or player2[CHAR] == "ryu":
        #RYU
        #====================
        #IDLE
        #==========
        ridle0,ridle1,ridle2,ridle3 = [image.load("ryu/idle/idle0.png"),image.load("ryu/idle/idle1.png"),
                                       image.load("ryu/idle/idle2.png"),image.load("ryu/idle/idle3.png")]
        ridle = [ridle0,ridle1,ridle2,ridle3]
        #WALK
        #==========
        rwalk0,rwalk1,rwalk2,rwalk3,rwalk4 =[image.load("ryu/walk/walk0.png"),image.load("ryu/walk/walk1.png"),
                                             image.load("ryu/walk/walk2.png"),image.load("ryu/walk/walk3.png"),
                                             image.load("ryu/walk/walk4.png")]
        rwalk = [rwalk0,rwalk1,rwalk2,rwalk3,rwalk4]
        #JUMP
        #==========
        rjump0,rjump1,rjump2,rjump3,rjump4,rjump5,rjump6 = [image.load("ryu/jump/jump0.png"),image.load("ryu/jump/jump1.png"),
                                                            image.load("ryu/jump/jump2.png"),image.load("ryu/jump/jump3.png"),
                                                            image.load("ryu/jump/jump4.png"),image.load("ryu/jump/jump5.png"),
                                                            image.load("ryu/jump/jump6.png")]
        rjump = [rjump0,rjump1,rjump2,rjump3,rjump4,rjump5,rjump6]
        #PUNCH
        #==========
        rpunch0,rpunch1,rpunch2,rpunch3,rpunch4 = [image.load("ryu/punch/punch0.png"),image.load("ryu/punch/punch1.png"),
                                                   image.load("ryu/punch/punch2.png"),image.load("ryu/punch/punch3.png"),
                                                   image.load("ryu/punch/punch4.png")]
        rpunch = [rpunch0,rpunch1,rpunch2,rpunch3,rpunch4]
        #KICK
        #==========
        rkick0,rkick1,rkick2,rkick3,rkick4 = [image.load("ryu/kick/kick0.png"),image.load("ryu/kick/kick1.png"),
                                              image.load("ryu/kick/kick2.png"),image.load("ryu/kick/kick3.png"),
                                              image.load("ryu/kick/kick4.png")]
        rkick = [rkick0,rkick1,rkick2,rkick3,rkick4]
        #AIR PUNCH
        #==========
        rairpunch0,rairpunch1,rairpunch2 = [image.load("ryu/airpunch/airpunch0.png"),image.load("ryu/airpunch/airpunch1.png"),
                                            image.load("ryu/airpunch/airpunch2.png")]
        rairpunch = [rairpunch0,rairpunch1,rairpunch2]
        #AIRKICK
        #==========
        rairkick0,rairkick1,rairkick2 = [image.load("ryu/airkick/airkick0.png"),image.load("ryu/airkick/airkick1.png"),
                                         image.load("ryu/airkick/airkick2.png")]
        rairkick = [rairkick0,rairkick1,rairkick2]
        #SPECIAL/HADOUKEN
        #==========
        hadouken0,hadouken1,hadouken2,hadouken3,hadouken4 = [image.load("ryu/hadouken/hadouken0.png"),image.load("ryu/hadouken/hadouken1.png"),
                                                             image.load("ryu/hadouken/hadouken2.png"),image.load("ryu/hadouken/hadouken3.png"),
                                                             image.load("ryu/hadouken/hadouken4.png")]
        hadouken = [hadouken0,hadouken1,hadouken2,hadouken3,hadouken4]
        #GETS HIT
        #==========
        rhit0,rhit1,rhit2,rhit3 = [image.load("ryu/hit/hit0.png"),image.load("ryu/hit/hit1.png"),
                                   image.load("ryu/hit/hit2.png"),image.load("ryu/hit/hit3.png")]
        rhit = [rhit0,rhit1,rhit2,rhit3]
        #GETS KO'D
        #==========
        rko0,rko1,rko2,rko3,rko4 = [image.load("ryu/ko/ko0.png"),image.load("ryu/ko/ko1.png"),image.load("ryu/ko/ko2.png"),
                                    image.load("ryu/ko/ko3.png"),image.load("ryu/ko/ko4.png")]
        rko = [rko0,rko1,rko2,rko3,rko4]
        #VICTORY CELEBRATION
        #==========
        rwin0,rwin1,rwin2,rwin3,rwin4,rwin5,rwin6 = [image.load("ryu/victory/victory0.png"),image.load("ryu/victory/victory1.png"),
                                                     image.load("ryu/victory/victory2.png"),image.load("ryu/victory/victory3.png"),
                                                     image.load("ryu/victory/victory4.png"),image.load("ryu/victory/victory5.png"),
                                                     image.load("ryu/victory/victory6.png")]
        rwin = [rwin0,rwin1,rwin2,rwin3,rwin4,rwin5,rwin6]
        #HADOUKEN FIREBALL
        #==========
        rball0,rball1 = [image.load("ryu/ball/ball0.png"),image.load("ryu/ball/ball1.png")]
        rball = [rball0,rball1]
        #==========
        global ryumoves
        ryumoves = [ridle,rwalk,rjump,rpunch,rkick,rairpunch,rairkick,hadouken,rhit,rko,rwin,rball]



    if player1[CHAR] == "ken" or player2[CHAR] == "ken":
        #KEN
        #====================
        #IDLE
        #==========
        kidle0,kidle1,kidle2,kidle3 = [image.load("ken/idle/idle0.png"),image.load("ken/idle/idle1.png"),
                                       image.load("ken/idle/idle2.png"),image.load("ken/idle/idle3.png")]
        kidle = [kidle0,kidle1,kidle2,kidle3]
        #WALK
        #==========
        kwalk0,kwalk1,kwalk2,kwalk3,kwalk4 =[image.load("ken/walk/walk0.png"),image.load("ken/walk/walk1.png"),
                                             image.load("ken/walk/walk2.png"),image.load("ken/walk/walk3.png"),
                                             image.load("ken/walk/walk4.png")]
        kwalk = [kwalk0,kwalk1,kwalk2,kwalk3,kwalk4]
        #JUMP
        #==========
        kjump0,kjump1,kjump2,kjump3,kjump4,kjump5,kjump6 = [image.load("ken/jump/jump0.png"),image.load("ken/jump/jump1.png"),
                                                            image.load("ken/jump/jump2.png"),image.load("ken/jump/jump3.png"),
                                                            image.load("ken/jump/jump4.png"),image.load("ken/jump/jump5.png"),
                                                            image.load("ken/jump/jump6.png")]
        kjump = [kjump0,kjump1,kjump2,kjump3,kjump4,kjump5,kjump6]
        #PUNCH
        #==========
        kpunch0,kpunch1,kpunch2,kpunch3,kpunch4,kpunch5,kpunch6 = [image.load("ken/punch/punch0.png"),image.load("ken/punch/punch1.png"),
                                                   image.load("ken/punch/punch2.png"),image.load("ken/punch/punch3.png"),
                                                   image.load("ken/punch/punch4.png"),image.load("ken/punch/punch5.png"),
                                                   image.load("ken/punch/punch6.png")]
        kpunch = [kpunch0,kpunch1,kpunch2,kpunch3,kpunch4,kpunch5,kpunch6]
        #KICK
        #==========
        kkick0,kkick1,kkick2,kkick3,kkick4 = [image.load("ken/kick/kick0.png"),image.load("ken/kick/kick1.png"),
                                              image.load("ken/kick/kick2.png"),image.load("ken/kick/kick3.png"),
                                              image.load("ken/kick/kick4.png")]
        kkick = [kkick0,kkick1,kkick2,kkick3,kkick4]
        #AIR PUNCH
        #==========
        kairpunch0,kairpunch1= [image.load("ken/airpunch/airpunch0.png"),image.load("ken/airpunch/airpunch1.png")]
        kairpunch = [kairpunch0,kairpunch1]
        #AIRKICK
        #==========
        kairkick0,kairkick1,kairkick2 = [image.load("ken/airkick/airkick0.png"),image.load("ken/airkick/airkick1.png"),
                                         image.load("ken/airkick/airkick2.png")]
        kairkick = [kairkick0,kairkick1,kairkick2]
        #SPECIAL/FIREPUNCH
        #==========
        firepunch0,firepunch1,firepunch2,firepunch3,firepunch4,firepunch5 = [image.load("ken/firepunch/firepunch0.png"),image.load("ken/firepunch/firepunch1.png"),
                                                                             image.load("ken/firepunch/firepunch2.png"),image.load("ken/firepunch/firepunch3.png"),
                                                                             image.load("ken/firepunch/firepunch4.png"),image.load("ken/firepunch/firepunch5.png")]
        firepunch = [firepunch0,firepunch1,firepunch2,firepunch3,firepunch4,firepunch5]
        #GETS HIT
        #==========
        khit0,khit1,khit2,khit3 = [image.load("ken/hit/hit0.png"),image.load("ken/hit/hit1.png"),
                                   image.load("ken/hit/hit2.png"),image.load("ken/hit/hit3.png")]
        khit = [khit0,khit1,khit2,khit3]
        #GETS KO'D
        #==========
        kko0,kko1,kko2,kko3,kko4 = [image.load("ken/ko/ko0.png"),image.load("ken/ko/ko1.png"),image.load("ken/ko/ko2.png"),
                                    image.load("ken/ko/ko3.png"),image.load("ken/ko/ko4.png")]
        kko = [kko0,kko1,kko2,kko3,kko4]
        #VICTORY CELEBRATION
        #==========
        kwin0,kwin1,kwin2 = [image.load("ken/victory/victory0.png"),image.load("ken/victory/victory1.png"),image.load("ken/victory/victory2.png")]
        kwin = [kwin0,kwin1,kwin2]
        #==========
        global kenmoves
        kenmoves = [kidle,kwalk,kjump,kpunch,kkick,kairpunch,kairkick,firepunch,khit,kko,kwin]



    if player1[CHAR] == "bison" or player2[CHAR] == "bison":
        #MIKE BISON
        #====================
        #IDLE
        #==========
        bidle0,bidle1,bidle2 = [image.load("bison/idle/idle0.png"),image.load("bison/idle/idle1.png"),
                                       image.load("bison/idle/idle2.png")]
        bidle = [bidle0,bidle1,bidle2]
        #WALK
        #==========
        bwalk0,bwalk1,bwalk2,bwalk3 =[image.load("bison/walk/walk0.png"),image.load("bison/walk/walk1.png"),
                                             image.load("bison/walk/walk2.png"),image.load("bison/walk/walk3.png")]
        bwalk = [bwalk0,bwalk1,bwalk2,bwalk3]
        #JUMP
        #==========
        bjump0,bjump1,bjump2,bjump3,bjump4 = [image.load("bison/jump/jump0.png"),image.load("bison/jump/jump1.png"),
                                                            image.load("bison/jump/jump2.png"),image.load("bison/jump/jump3.png"),
                                                            image.load("bison/jump/jump4.png")]
        bjump = [bjump0,bjump1,bjump2,bjump3,bjump4]
        #PUNCH
        #==========
        bpunch0,bpunch1,bpunch2,bpunch3= [image.load("bison/punch/punch0.png"),image.load("bison/punch/punch1.png"),
                                                   image.load("bison/punch/punch2.png"),image.load("bison/punch/punch3.png")]
        bpunch = [bpunch0,bpunch1,bpunch2,bpunch3]
        #KICK
        #==========
        bkick0,bkick1,bkick2,bkick3 = [image.load("bison/kick/kick0.png"),image.load("bison/kick/kick1.png"),
                                              image.load("bison/kick/kick2.png"),image.load("bison/kick/kick3.png")]
        bkick = [bkick0,bkick1,bkick2,bkick3]
        #AIR PUNCH
        #==========
        bairpunch0,bairpunch1,bairpunch2,bairpunch3,bairpunch4,bairpunch5 = [image.load("bison/airpunch/airpunch0.png"),image.load("bison/airpunch/airpunch1.png"),
                                                                             image.load("bison/airpunch/airpunch2.png"),image.load("bison/airpunch/airpunch3.png"),
                                                                             image.load("bison/airpunch/airpunch4.png"),image.load("bison/airpunch/airpunch5.png")]
        bairpunch = [bairpunch0,bairpunch1,bairpunch2,bairpunch3,bairpunch4,bairpunch5]
        #AIRKICK
        #==========
        bairkick0,bairkick1 = [image.load("bison/airkick/airkick0.png"),image.load("bison/airkick/airkick1.png")]
        bairkick = [bairkick0,bairkick1]
        #SPECIAL
        #==========
        special0,special1,special2,special3,special4,special5,special6,special7 = [image.load("bison/special/special0.png"),image.load("bison/special/special1.png"),
                                                                                   image.load("bison/special/special2.png"),image.load("bison/special/special3.png"),
                                                                                   image.load("bison/special/special4.png"),image.load("bison/special/special5.png"),
                                                                                   image.load("bison/special/special6.png"),image.load("bison/special/special7.png")]
        special = [special0,special1,special2,special3,special4,special5,special6,special7]
        #GETS HIT
        #==========
        bhit = [image.load("bison/hit/hit0.png")]
        #GETS KO'D
        #==========
        bko0,bko1,bko2,bko3 = [image.load("bison/ko/ko0.png"),image.load("bison/ko/ko1.png"),image.load("bison/ko/ko2.png"),
                                    image.load("bison/ko/ko3.png")]
        bko = [bko0,bko1,bko2,bko3]
        #VICTORY CELEBRATION
        #==========
        bwin0,bwin1,bwin2,bwin3 = [image.load("bison/victory/victory0.png"),image.load("bison/victory/victory1.png"),
                                   image.load("bison/victory/victory2.png"),image.load("bison/victory/victory3.png")]
        bwin = [bwin0,bwin1,bwin2,bwin3]
        #==========
        global bisonmoves
        bisonmoves = [bidle,bwalk,bjump,bpunch,bkick,bairpunch,bairkick,special,bhit,bko,bwin]


        
    #BACKGROUNDS
    #====================
    #stage0,stage1,stage2 = [image.load("stages/stage0.jpg"),image.load("stages/stage1.png"),image.load("stages/stage2.jpg")]
    #stages = [stage0,stage1,stage2]
    #FOR NOW ONLYYYYYY
    #====================
    global IDLE,WALK,JUMP,PUNCH,KICK,AIRPUNCH,AIRKICK,SPECIAL,HIT,KO,WIN,PROJ
    IDLE = 0
    WALK = 1
    JUMP = 2
    PUNCH = 3
    KICK = 4
    AIRPUNCH = 5
    AIRKICK = 6
    SPECIAL = 7
    HIT = 8
    KO = 9
    WIN = 10
    PROJ = 11
    #========================================

p1frames = [False,0]
p2frames = [False,0]

ANI = 0
NUM = 1

global player1,p1hitbox,p1attbox,attack1,attack2,p1sprite,waiting,waittime


player1 = [True,True,False,False,True,False,False,False]
player2 = [False,True,False,False,True,False,False,False]
#facing right, can att, is att, character, on ground, y-velocity, moving

global RIGHT,CANATT,ISATT,CHAR,ONGROUND,VEL,MOVING,SPRITE
RIGHT = 0
CANATT = 1
ISATT = 2
CHAR = 3
ONGROUND = 4
VEL = 5
MOVING = 6
SPRITE = 7

p1hitbox = [100,400,0,0] #x,y,width,height
p1hit = Rect(p1hitbox)

p2hitbox = [100,200,0,0] #x,y,width,height
p2hit = Rect(p2hitbox)

global X,Y,WID,HEI
X = 0
Y = 1
WID  = 2
HEI = 3

player1[CHAR] = "ryu"

def movep1():
    if player1[ISATT] == False and player1[ONGROUND] == True:
        
        if player1[CHAR] == "ryu":
            if keys[ord("a")] == 1 and keys[ord("d")] == 1:
                p1frames[ANI] = "idle"
            
            elif keys[ord("a")] == 1:
                if p1frames[ANI] != "movel":
                    p1frames[ANI] = "movel"
                    p1frames[NUM] = 0
                    
                player1[RIGHT] = False
                player1[MOVING] = True
                p1frames[NUM] += 0.2

                if round(p1frames[NUM],0) == 5:
                    p1frames[NUM] = 0

                player1[SPRITE] = transform.flip(ryumoves[WALK][int(round(p1frames[NUM],0))],1,0)

                p1hitbox[X] -= 2
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

                
            elif keys[ord("d")] == 1:
                if p1frames[ANI] != "mover":
                    p1frames[ANI] = "mover"
                    p1frames[NUM] = 0

                print(p1hitbox)
                player1[RIGHT] = True
                player1[MOVING] = True
                p1frames[NUM] += 0.2

                if round(p1frames[NUM],0) == 5:
                    p1frames[NUM] = 0

                player1[SPRITE] = ryumoves[WALK][int(round(p1frames[NUM],0))]

                p1hitbox[X] += 2
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

            if p1frames[ANI] == "movel" and keys[ord("a")] == 0:
                player1[MOVING] = False
                p1frames[ANI] = "idle"
                p1frames[NUM] = 0
                
            elif p1frames[ANI] == "mover" and keys[ord("d")] == 0:
                player1[MOVING] = False
                p1frames[ANI] = "idle"
                p1frames[NUM] = 0
                



    
def idlep1():
    if player1[ISATT] == False and player1[MOVING] == False and player1[ONGROUND] == True:
        if player1[CHAR] == "ryu":
            if p1frames[ANI]!= "idle":
                p1frames[ANI] = "idle"
                p1frames[NUM] = 0

            p1frames[NUM] += 0.1

            if round(p1frames[NUM],0) == 4:
                    p1frames[NUM] = 0

            if player1[RIGHT] == True:
                player1[SPRITE] = ryumoves[IDLE][int(round(p1frames[NUM],0))]
            else:
                player1[SPRITE] = transform.flip(ryumoves[IDLE][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]


def attp1():
    if player1[CANATT] == True and player1[ONGROUND] == True:
        
        if player1[CHAR] == "ryu":
            if keys[ord("t")] == 1:
                player1[CANATT] = False



def drawp1():
    screen.blit(player1[SPRITE],(p1hitbox[X],p1hitbox[Y]))




ground = Rect(0,600,2000,1000)

myClock = time.Clock()
screen = display.set_mode((1024,768))

player1[CHAR] = "ryu"
loadimages()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    keys = key.get_pressed()
    screen.fill((0,0,0))
    draw.rect(screen,(255,255,255),ground)

    movep1()
    idlep1()
    drawp1()
























    myClock.tick(60)
    display.flip()
quit()
