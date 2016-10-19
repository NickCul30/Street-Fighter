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
        rairkick0,rairkick1,rairkick2,rairkick3 = [image.load("ryu/airkick/airkick0.png"),image.load("ryu/airkick/airkick1.png"),
                                         image.load("ryu/airkick/airkick2.png"),image.load("ryu/airkick/airkick3.png")]
        rairkick = [rairkick0,rairkick1,rairkick2,rairkick3]
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
        kairpunch0,kairpunch1,kairpunch2 = [image.load("ken/airpunch/airpunch0.png"),image.load("ken/airpunch/airpunch1.png"),image.load("ken/airpunch/airpunch2.png")]
        kairpunch = [kairpunch0,kairpunch1,kairpunch2]
        #AIRKICK
        #==========
        kairkick0,kairkick1,kairkick2,kairkick3 = [image.load("ken/airkick/airkick0.png"),image.load("ken/airkick/airkick1.png"),
                                         image.load("ken/airkick/airkick2.png"),image.load("ken/airkick/airkick3.png")]
        kairkick = [kairkick0,kairkick1,kairkick2,kairkick3]
        #HADOUKEN
        #==========
        khadouken0,khadouken1,khadouken2,khadouken3 = [image.load("ken/hadouken/hadouken0.png"),image.load("ken/hadouken/hadouken1.png"),
                                                                             image.load("ken/hadouken/hadouken2.png"),image.load("ken/hadouken/hadouken3.png")]
        khadouken = [khadouken0,khadouken1,khadouken2,khadouken3]
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
        kball = [image.load("ken/ball/ball0.png")]
        global kenmoves
        kenmoves = [kidle,kwalk,kjump,kpunch,kkick,kairpunch,kairkick,khadouken,khit,kko,kwin,kball]



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
        bairkick0,bairkick1,bairkick2 = [image.load("bison/airkick/airkick0.png"),image.load("bison/airkick/airkick1.png"),image.load("bison/airkick/airkick2.png")]
        bairkick = [bairkick0,bairkick1,bairkick2]
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
    global stages
    stage0,stage1,stage2 = [image.load("stages/stage0.jpg"),image.load("stages/stage1.jpg"),image.load("stages/stage2.jpg")]
    stages = [stage0,stage1,stage2]
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
    global mugshots,vs,texts
    mugshot0,mugshot1,mugshot2 = [image.load("mugshot/mugshot0.png"),image.load("mugshot/mugshot1.png"),image.load("mugshot/mugshot2.png")]
    mugshots = [mugshot0,mugshot1,mugshot2]
    vs = image.load("icons/vs.png")
    text0,text1,text2,text3,text4,text5,text6 = [image.load("icons/text0.png"),image.load("icons/text1.png"),image.load("icons/text2.png"),
                                                 image.load("icons/text3.png"),image.load("icons/text4.png"),image.load("icons/text5.png"),
                                                 image.load("icons/text6.png")]
    texts = [text0,text1,text2,text3,text4,text5,text6]
    

global p1delay,p2delay,WAITING,WAITTIME
p1delay = [False,False]
p2delay = [False,False]
#waited, amt need to wait

WAITING = 0
WAITTIME = 1

global hadouken1,hadouken2,hadoukenflag1,hadoukenflag2
hadouken1,hadouken2 = [[False,-100,False]],[[False,-100,False]]
hadoukenflag1,hadoukenflag2 = False,False
#Each entry in the hadouken list will represent a fireball:
#for each entry: [x,y,facing]


global NUM,ANI,p1frames,p2frames
p1frames = [False,0]
p2frames = [False,0]
#which attack, frame no.

ANI = 0
NUM = 1

global player1,p1hitbox,p1attbox,attack1,attack2,p1sprite,waiting,waittime

player1 = [True,True,False,False,True,False,False,False,False,5,True]
player2 = [False,True,False,False,True,False,False,False,False,5,True]
#facing right, can att, is att, character, on ground, y-velocity, moving,
#points of damage for attack, health

global RIGHT,CANATT,ISATT,CHAR,ONGROUND,VEL,MOVING,SPRITE,DAMAGE,HP,ALIVE
RIGHT = 0
CANATT = 1
ISATT = 2
CHAR = 3
ONGROUND = 4
VEL = 5
MOVING = 6
SPRITE = 7
DAMAGE = 8
HP = 9
ALIVE = 10


global X,Y,WID,HEI
X = 0
Y = 1
WID  = 2
HEI = 3


if player1[CHAR] == "bison": p1hitbox = [700,670-89,0,0] #x,y,width,height
else: p1hitbox = [300,670-89,0,0]
p1hit = Rect(p1hitbox)

if player2[CHAR] == "bison": p2hitbox = [700,670-89,0,0] #x,y,width,height
else: p2hitbox = [700,670-89,0,0]
p2hit = Rect(p2hitbox)

global outleft,outright
outleft = Rect(1024,0,100,1024)
outright = Rect(-100,0,100,1024)

global score,oldscore
score = [0,0]
oldscore = score




def movep1():
        
    if player1[CHAR] == "ryu":
        
        if player1[ISATT] == False and player1[ONGROUND] == True:
            
            if keys[ord("a")] == 1 and keys[ord("d")] == 1:
                p1frames[ANI] = "idle"
                player1[MOVING] = False
            
            elif keys[ord("a")] == 1:
                if p1frames[ANI] != "movel":
                    p1frames[ANI] = "movel"
                    p1frames[NUM] = 0
                    
                player1[RIGHT] = False
                player1[MOVING] = True
                p1frames[NUM] += 0.2

                if round(p1frames[NUM],0) >= 5:
                    p1frames[NUM] = 0

                player1[SPRITE] = transform.flip(ryumoves[WALK][int(round(p1frames[NUM],0))],1,0)

                p1hitbox[X] -= 3
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

                
            elif keys[ord("d")] == 1:
                if p1frames[ANI] != "mover":
                    p1frames[ANI] = "mover"
                    p1frames[NUM] = 0

                player1[RIGHT] = True
                player1[MOVING] = True
                p1frames[NUM] += 0.2

                if round(p1frames[NUM],0) >= 5:
                    p1frames[NUM] = 0

                player1[SPRITE] = ryumoves[WALK][int(round(p1frames[NUM],0))]

                p1hitbox[X] += 3
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

            
            if keys[ord("w")] == 1:
                if p1frames[ANI] != "jump":
                    p1frames[ANI] = "jump"
                    p1frames[NUM] = 0

                player1[ONGROUND] = False
                player1[MOVING] = True
                player1[VEL] = 15

        
#========================================



    elif player1[CHAR] == "ken":
        if player1[ISATT] == False and player1[ONGROUND] == True:
            
            if keys[ord("a")] == 1 and keys[ord("d")] == 1:
                p1frames[ANI] = "idle"
                player1[MOVING] = False
            
            elif keys[ord("a")] == 1:
                if p1frames[ANI] != "movel":
                    p1frames[ANI] = "movel"
                    p1frames[NUM] = 0
                    
                player1[RIGHT] = False
                player1[MOVING] = True
                p1frames[NUM] += 0.2

                if round(p1frames[NUM],0) >= 5:
                    p1frames[NUM] = 0

                player1[SPRITE] = transform.flip(kenmoves[WALK][int(round(p1frames[NUM],0))],1,0)

                p1hitbox[X] -= 3
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

                
            elif keys[ord("d")] == 1:
                if p1frames[ANI] != "mover":
                    p1frames[ANI] = "mover"
                    p1frames[NUM] = 0

                player1[RIGHT] = True
                player1[MOVING] = True
                p1frames[NUM] += 0.2

                if round(p1frames[NUM],0) >= 5:
                    p1frames[NUM] = 0

                player1[SPRITE] = kenmoves[WALK][int(round(p1frames[NUM],0))]

                p1hitbox[X] += 3
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

            if keys[ord("w")] == 1:
                if p1frames[ANI] != "jump":
                    p1frames[ANI] = "jump"
                    p1frames[NUM] = 0

                player1[ONGROUND] = False
                player1[MOVING] = True
                player1[VEL] = 15

#========================================


    elif player1[CHAR] == "bison":
        if player1[ISATT] == False and player1[ONGROUND] == True:
            
            if keys[ord("a")] == 1 and keys[ord("d")] == 1:
                p1frames[ANI] = "idle"
                player1[MOVING] = False
            
            elif keys[ord("a")] == 1:
                if p1frames[ANI] != "movel":
                    p1frames[ANI] = "movel"
                    p1frames[NUM] = 0
                    
                player1[RIGHT] = False
                player1[MOVING] = True
                p1frames[NUM] += 0.2

                if round(p1frames[NUM],0) >= 4:
                    p1frames[NUM] = 0

                player1[SPRITE] = transform.flip(bisonmoves[WALK][int(round(p1frames[NUM],0))],1,0)

                p1hitbox[X] -= 3
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

                
            elif keys[ord("d")] == 1:
                if p1frames[ANI] != "mover":
                    p1frames[ANI] = "mover"
                    p1frames[NUM] = 0

                player1[RIGHT] = True
                player1[MOVING] = True
                p1frames[NUM] += 0.2

                if round(p1frames[NUM],0) >= 4:
                    p1frames[NUM] = 0

                player1[SPRITE] = bisonmoves[WALK][int(round(p1frames[NUM],0))]

                p1hitbox[X] += 3
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

            if keys[ord("w")] == 1:
                if p1frames[ANI] != "jump":
                    p1frames[ANI] = "jump"
                    p1frames[NUM] = 0

                player1[ONGROUND] = False
                player1[MOVING] = True
                player1[VEL] = 15

#========================================


                
    if p1frames[ANI] == "movel" and keys[ord("a")] == 0:
        player1[MOVING] = False
        p1frames[ANI] = "idle"
        p1frames[NUM] = 0
                
    elif p1frames[ANI] == "mover" and keys[ord("d")] == 0:
        player1[MOVING] = False
        p1frames[ANI] = "idle"
        p1frames[NUM] = 0
#========================================







def movep2():
        
    if player2[CHAR] == "ryu":
        
        if player2[ISATT] == False and player2[ONGROUND] == True:
            
            if keys[K_LEFT] == 1 and keys[K_RIGHT] == 1:
                p2frames[ANI] = "idle"
                player2[MOVING] = False
            
            elif keys[K_LEFT] == 1:
                if p2frames[ANI] != "movel":
                    p2frames[ANI] = "movel"
                    p2frames[NUM] = 0
                    
                player2[RIGHT] = False
                player2[MOVING] = True
                p2frames[NUM] += 0.2

                if round(p2frames[NUM],0) >= 5:
                    p2frames[NUM] = 0

                player2[SPRITE] = transform.flip(ryumoves[WALK][int(round(p2frames[NUM],0))],1,0)

                p2hitbox[X] -= 3
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

                
            elif keys[K_RIGHT] == 1:
                if p2frames[ANI] != "mover":
                    p2frames[ANI] = "mover"
                    p2frames[NUM] = 0

                player2[RIGHT] = True
                player2[MOVING] = True
                p2frames[NUM] += 0.2

                if round(p2frames[NUM],0) >= 5:
                    p2frames[NUM] = 0

                player2[SPRITE] = ryumoves[WALK][int(round(p2frames[NUM],0))]

                p2hitbox[X] += 3
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

            
            if keys[K_UP] == 1:
                if p2frames[ANI] != "jump":
                    p2frames[ANI] = "jump"
                    p2frames[NUM] = 0

                player2[ONGROUND] = False
                player2[MOVING] = True
                player2[VEL] = 15
        
#========================================



    elif player2[CHAR] == "ken":
        if player2[ISATT] == False and player2[ONGROUND] == True:
            
            if keys[K_RIGHT] == 1 and keys[K_LEFT] == 1:
                p2frames[ANI] = "idle"
                player2[MOVING] = False
            
            elif keys[K_LEFT] == 1:
                if p2frames[ANI] != "movel":
                    p2frames[ANI] = "movel"
                    p2frames[NUM] = 0
                    
                player2[RIGHT] = False
                player2[MOVING] = True
                p2frames[NUM] += 0.2

                if round(p2frames[NUM],0) >= 5:
                    p2frames[NUM] = 0

                player2[SPRITE] = transform.flip(kenmoves[WALK][int(round(p2frames[NUM],0))],1,0)

                p2hitbox[X] -= 3
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

                
            elif keys[K_RIGHT] == 1:
                if p2frames[ANI] != "mover":
                    p2frames[ANI] = "mover"
                    p2frames[NUM] = 0

                player2[RIGHT] = True
                player2[MOVING] = True
                p2frames[NUM] += 0.2

                if round(p2frames[NUM],0) >= 5:
                    p2frames[NUM] = 0

                player2[SPRITE] = kenmoves[WALK][int(round(p2frames[NUM],0))]

                p2hitbox[X] += 3
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

            if keys[K_UP] == 1:
                if p2frames[ANI] != "jump":
                    p2frames[ANI] = "jump"
                    p2frames[NUM] = 0

                player2[ONGROUND] = False
                player2[MOVING] = True
                player2[VEL] = 15
               
#========================================


    elif player2[CHAR] == "bison":
        if player2[ISATT] == False and player2[ONGROUND] == True:
            
            if keys[K_LEFT] == 1 and keys[K_RIGHT] == 1:
                p2frames[ANI] = "idle"
                player2[MOVING] = False
            
            elif keys[K_LEFT] == 1:
                if p2frames[ANI] != "movel":
                    p2frames[ANI] = "movel"
                    p2frames[NUM] = 0
                    
                player2[RIGHT] = False
                player2[MOVING] = True
                p2frames[NUM] += 0.2

                if round(p2frames[NUM],0) >= 4:
                    p2frames[NUM] = 0

                player2[SPRITE] = transform.flip(bisonmoves[WALK][int(round(p2frames[NUM],0))],1,0)

                p2hitbox[X] -= 3
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

                
            elif keys[K_RIGHT] == 1:
                if p2frames[ANI] != "mover":
                    p2frames[ANI] = "mover"
                    p2frames[NUM] = 0

                player2[RIGHT] = True
                player2[MOVING] = True
                p2frames[NUM] += 0.2

                if round(p2frames[NUM],0) >= 4:
                    p2frames[NUM] = 0

                player2[SPRITE] = bisonmoves[WALK][int(round(p2frames[NUM],0))]

                p2hitbox[X] += 3
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

            if keys[K_UP] == 1:
                if p2frames[ANI] != "jump":
                    p2frames[ANI] = "jump"
                    p2frames[NUM] = 0

                player2[ONGROUND] = False
                player2[MOVING] = True
                player2[VEL] = 15

#========================================


                
    if p2frames[ANI] == "movel" and keys[K_LEFT] == 0:
        player2[MOVING] = False
        p2frames[ANI] = "idle"
        p2frames[NUM] = 0
                
    elif p2frames[ANI] == "mover" and keys[K_RIGHT] == 0:
        player2[MOVING] = False
        p2frames[ANI] = "idle"
        p2frames[NUM] = 0
#======================================== 




def jumpp1():
    if player1[CHAR] == "ryu":
        
        if player1[ONGROUND] == False and p1frames[ANI] == "jump":
            
            p1frames[NUM] += 0.2
            
            if round(p1frames[NUM],0) >= 7:
                p1frames[NUM] = 0

            if player1[RIGHT] == True:
                player1[SPRITE] = ryumoves[JUMP][int(round(p1frames[NUM],0))]
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
            else:
                player1[SPRITE] = transform.flip(ryumoves[JUMP][int(round(p1frames[NUM],0))],1,0)
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

                
    if player1[CHAR] == "ken":
        
        if player1[ONGROUND] == False and p1frames[ANI] == "jump":
            
            p1frames[NUM] += 0.2
            
            if round(p1frames[NUM],0) >= 7:
                p1frames[NUM] = 0

            if player1[RIGHT] == True:
                player1[SPRITE] = kenmoves[JUMP][int(round(p1frames[NUM],0))]
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
            else:
                player1[SPRITE] = transform.flip(kenmoves[JUMP][int(round(p1frames[NUM],0))],1,0)
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

                
    if player1[CHAR] == "bison":
        
        if player1[ONGROUND] == False and p1frames[ANI] == "jump":
            
            p1frames[NUM] += 0.125
            
            if round(p1frames[NUM],0) >= 5:
                p1frames[NUM] = 0

            if player1[RIGHT] == True:
                player1[SPRITE] = bisonmoves[JUMP][int(round(p1frames[NUM],0))]
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
            else:
                player1[SPRITE] = transform.flip(bisonmoves[JUMP][int(round(p1frames[NUM],0))],1,0)
                p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
                

    if keys[ord("a")] == 1 and player1[ONGROUND] == False and player1[ISATT] == False:
        p1hitbox[X] -= 2
        player1[RIGHT] = False
        
    elif keys[ord("d")] == 1 and player1[ONGROUND] == False and player1[ISATT] == False:
        p1hitbox[X] += 2
        player1[RIGHT] = True
        



#========================================




def jumpp2():
    if player2[CHAR] == "ryu":
        
        if player2[ONGROUND] == False and p2frames[ANI] == "jump":
            p2frames[NUM] += 0.2
            
            if round(p2frames[NUM],0) >= 7:
                p2frames[NUM] = 0

            if player2[RIGHT] == True:
                player2[SPRITE] = ryumoves[JUMP][int(round(p2frames[NUM],0))]
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
            else:
                player2[SPRITE] = transform.flip(ryumoves[JUMP][int(round(p2frames[NUM],0))],1,0)
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================

                
    if player2[CHAR] == "ken":
        
        if player2[ONGROUND] == False and p2frames[ANI] == "jump":
            
            p2frames[NUM] += 0.2
            
            if round(p2frames[NUM],0) >= 7:
                p2frames[NUM] = 0

            if player2[RIGHT] == True:
                player2[SPRITE] = kenmoves[JUMP][int(round(p2frames[NUM],0))]
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
            else:
                player2[SPRITE] = transform.flip(kenmoves[JUMP][int(round(p2frames[NUM],0))],1,0)
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================

                
    if player2[CHAR] == "bison":
        
        if player2[ONGROUND] == False and p2frames[ANI] == "jump":
            
            p2frames[NUM] += 0.125
            
            if round(p2frames[NUM],0) >= 5:
                p2frames[NUM] = 0

            if player2[RIGHT] == True:
                player2[SPRITE] = bisonmoves[JUMP][int(round(p2frames[NUM],0))]
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
            else:
                player2[SPRITE] = transform.flip(bisonmoves[JUMP][int(round(p2frames[NUM],0))],1,0)
                p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================


    if keys[K_LEFT] == 1 and player2[ONGROUND] == False and player2[ISATT] == False:
        p2hitbox[X] -= 2
        player2[RIGHT] = False
        
    elif keys[K_RIGHT] == 1 and player2[ONGROUND] == False and player2[ISATT] == False:
        p2hitbox[X] += 2
        player2[RIGHT] = True




#========================================


def chargeAttp1():
    global hadoukenflag1
    if player1[CANATT] == True and player1[ONGROUND] == True and keys[ord("u")] == 1:
        
        if player1[CHAR] == "ryu":
            if p1frames[ANI]!= "special":
                p1frames[ANI] = "special"
                p1frames[NUM] = 0
                
            player1[ISATT] = True
            player1[MOVING] = True
            p1frames[NUM] += 0.15

            if round(p1frames[NUM],0) >= 5:
                p1frames[NUM] = 0
                player1[CANATT] = False
                player1[ISATT] = False
                p1frames[ANI] = "idle"
                player1[MOVING] = False
                p1delay[WAITTIME] = 25
                p1hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]
                hadoukenflag1 = True

            if player1[RIGHT] == True and p1frames[ANI] == "special":
                player1[SPRITE] = ryumoves[SPECIAL][int(round(p1frames[NUM],0))]
            elif player1[RIGHT] == False and p1frames[ANI] == "special":
                player1[SPRITE] = transform.flip(ryumoves[SPECIAL][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

        if player1[CHAR] == "ken":
            if p1frames[ANI]!= "special":
                p1frames[ANI] = "special"
                p1frames[NUM] = 0
                
            player1[ISATT] = True
            player1[MOVING] = True
            p1frames[NUM] += 0.15

            if round(p1frames[NUM],0) >= 4:
                p1frames[NUM] = 0
                player1[ISATT] = False
                p1frames[ANI] = "idle"
                player1[CANATT] = False
                player1[MOVING] = False
                p1delay[WAITTIME] = 25
                p1hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]
                hadoukenflag1 = True

            if player1[RIGHT] == True and p1frames[ANI] == "special":
                player1[SPRITE] = kenmoves[SPECIAL][int(round(p1frames[NUM],0))]
            elif player1[RIGHT] == False and p1frames[ANI] == "special":
                player1[SPRITE] = transform.flip(kenmoves[SPECIAL][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

        if player1[CHAR] == "bison":
            if p1frames[ANI]!= "special":
                p1frames[ANI] = "special"
                p1frames[NUM] = 0
                
            player1[ISATT] = True
            player1[MOVING] = True
            p1frames[NUM] += 0.2

            if round(p1frames[NUM],0) >= 8:
                p1frames[NUM] = 0
                player1[ISATT] = False
                p1frames[ANI] = "idle"
                player1[CANATT] = False
                player1[MOVING] = False
                p1delay[WAITTIME] = 25
                p1hitbox[Y] = 670 - bisonmoves[IDLE][0].get_size()[1]
                player1[DAMAGE] = False

            if round(p1frames[NUM],0) >= 2 and round(p1frames[NUM],0) <= 6:
                player1[DAMAGE] = 0.2
                if player1[RIGHT] == True:
                    p1hitbox[X] += 5
                else:
                    p1hitbox[X] -= 5
            else: player1[DAMAGE] = 0
            
            if player1[RIGHT] == True and p1frames[ANI] == "special":
                player1[SPRITE] = bisonmoves[SPECIAL][int(round(p1frames[NUM],0))]
            elif player1[RIGHT] == False and p1frames[ANI] == "special":
                player1[SPRITE] = transform.flip(bisonmoves[SPECIAL][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]   
#========================================


        

    if keys[ord("u")] == 0 and p1frames[ANI] == "special":
        player1[MOVING] = False
        p1frames[ANI] = "idle"
        p1frames[NUM] = 0
        player1[DAMAGE] = False
        if player1[CHAR] == "ryu": p1hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]
        elif player1[CHAR] == "ken": p1hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]
        else: p1hitbox[Y] = 670 - bisonmoves[WALK][0].get_size()[1]
        player1[ISATT] = False
#========================================


def chargeAttp2():
    global hadoukenflag2
    if player2[CANATT] == True and player2[ONGROUND] == True and keys[ord("l")] == 1:
        
        if player2[CHAR] == "ryu":
            if p2frames[ANI]!= "special":
                p2frames[ANI] = "special"
                p2frames[NUM] = 0
                
            player2[ISATT] = True
            player2[MOVING] = True
            p2frames[NUM] += 0.15

            if round(p2frames[NUM],0) >= 5:
                p2frames[NUM] = 0
                player2[CANATT] = False
                player2[ISATT] = False
                p2frames[ANI] = "idle"
                player2[MOVING] = False
                p2delay[WAITTIME] = 25
                hadoukenflag2 = True
                p2hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]

            if player2[RIGHT] == True and p2frames[ANI] == "special":
                player2[SPRITE] = ryumoves[SPECIAL][int(round(p2frames[NUM],0))]
            elif player2[RIGHT] == False and p2frames[ANI] == "special":
                player2[SPRITE] = transform.flip(ryumoves[SPECIAL][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================

        if player2[CHAR] == "ken":
            if p2frames[ANI]!= "special":
                p2frames[ANI] = "special"
                p2frames[NUM] = 0
                
            player2[ISATT] = True
            player2[MOVING] = True
            p2frames[NUM] += 0.15

            if round(p2frames[NUM],0) >= 4:
                p2frames[NUM] = 0
                player2[ISATT] = False
                p2frames[ANI] = "idle"
                player2[CANATT] = False
                player2[MOVING] = False
                p2delay[WAITTIME] = 25
                hadoukenflag2 = True
                p2hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]

            if player2[RIGHT] == True and p2frames[ANI] == "special":
                player2[SPRITE] = kenmoves[SPECIAL][int(round(p2frames[NUM],0))]
            elif player2[RIGHT] == False and p2frames[ANI] == "special":
                player2[SPRITE] = transform.flip(kenmoves[SPECIAL][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================

        if player2[CHAR] == "bison":
            if p2frames[ANI]!= "special":
                p2frames[ANI] = "special"
                p2frames[NUM] = 0
                
            player2[ISATT] = True
            player2[MOVING] = True
            p2frames[NUM] += 0.2

            if round(p2frames[NUM],0) >= 8:
                p2frames[NUM] = 0
                player2[ISATT] = False
                p2frames[ANI] = "idle"
                player2[CANATT] = False
                player2[MOVING] = False
                p2delay[WAITTIME] = 25
                p2hitbox[Y] = 670 - bisonmoves[IDLE][0].get_size()[1]
                player2[DAMAGE] = False

            if round(p2frames[NUM],0) >= 2 and round(p2frames[NUM],0) <= 6:
                player2[DAMAGE] = 0.2
                if player2[RIGHT] == True:
                    p2hitbox[X] += 5
                else:
                    p2hitbox[X] -= 5
            else: player2[DAMAGE] = 0

            if player2[RIGHT] == True and p2frames[ANI] == "special":
                player2[SPRITE] = bisonmoves[SPECIAL][int(round(p2frames[NUM],0))]
            elif player2[RIGHT] == False and p2frames[ANI] == "special":
                player2[SPRITE] = transform.flip(bisonmoves[SPECIAL][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]   
#========================================


        

    if keys[ord("l")] == 0 and p2frames[ANI] == "special":
        player2[MOVING] = False
        p2frames[ANI] = "idle"
        p2frames[NUM] = 0
        player2[DAMAGE] = False
        if player2[CHAR] == "ryu": p2hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]
        elif player2[CHAR] == "ken": p2hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]
        else: p2hitbox[Y] = 670 - bisonmoves[WALK][0].get_size()[1]
        player2[ISATT] = False
#========================================


    
def idlep1():
    if player1[ISATT] == False and player1[MOVING] == False and player1[ONGROUND] == True:
        if player1[CHAR] == "ryu":
            if p1frames[ANI]!= "idle":
                p1frames[ANI] = "idle"
                p1frames[NUM] = 0

            p1frames[NUM] += 0.1

            if round(p1frames[NUM],0) >= 4:
                    p1frames[NUM] = 0

            if player1[RIGHT] == True:
                player1[SPRITE] = ryumoves[IDLE][int(round(p1frames[NUM],0))]
            else:
                player1[SPRITE] = transform.flip(ryumoves[IDLE][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

        elif player1[CHAR] == "ken":
            if p1frames[ANI]!= "idle":
                p1frames[ANI] = "idle"
                p1frames[NUM] = 0

            p1frames[NUM] += 0.1

            if round(p1frames[NUM],0) >= 4:
                    p1frames[NUM] = 0

            if player1[RIGHT] == True:
                player1[SPRITE] = kenmoves[IDLE][int(round(p1frames[NUM],0))]
            else:
                player1[SPRITE] = transform.flip(kenmoves[IDLE][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

        if player1[CHAR] == "bison":
            if p1frames[ANI]!= "idle":
                p1frames[ANI] = "idle"
                p1frames[NUM] = 0

            p1frames[NUM] += 0.1

            if round(p1frames[NUM],0) >= 3:
                    p1frames[NUM] = 0

            if player1[RIGHT] == True:
                player1[SPRITE] = bisonmoves[IDLE][int(round(p1frames[NUM],0))]
            else:
                player1[SPRITE] = transform.flip(bisonmoves[IDLE][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================




def idlep2():
    if player2[ISATT] == False and player2[MOVING] == False and player2[ONGROUND] == True:
        if player2[CHAR] == "ryu":
            if p2frames[ANI]!= "idle":
                p2frames[ANI] = "idle"
                p2frames[NUM] = 0

            p2frames[NUM] += 0.1

            if round(p2frames[NUM],0) >= 4:
                    p2frames[NUM] = 0

            if player2[RIGHT] == True:
                player2[SPRITE] = ryumoves[IDLE][int(round(p2frames[NUM],0))]
            else:
                player2[SPRITE] = transform.flip(ryumoves[IDLE][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================

        elif player2[CHAR] == "ken":
            if p2frames[ANI]!= "idle":
                p2frames[ANI] = "idle"
                p2frames[NUM] = 0

            p2frames[NUM] += 0.1

            if round(p2frames[NUM],0) >= 4:
                    p2frames[NUM] = 0

            if player2[RIGHT] == True:
                player2[SPRITE] = kenmoves[IDLE][int(round(p2frames[NUM],0))]
            else:
                player2[SPRITE] = transform.flip(kenmoves[IDLE][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================

        if player2[CHAR] == "bison":
            if p2frames[ANI]!= "idle":
                p2frames[ANI] = "idle"
                p2frames[NUM] = 0

            p2frames[NUM] += 0.1

            if round(p2frames[NUM],0) >= 3:
                    p2frames[NUM] = 0

            if player2[RIGHT] == True:
                player2[SPRITE] = bisonmoves[IDLE][int(round(p2frames[NUM],0))]
            else:
                player2[SPRITE] = transform.flip(bisonmoves[IDLE][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#ATTACKS
#========================================


def attp1():
    global p1frames

#========================================
#PUNCH
    
    if player1[CANATT] == True and player1[ONGROUND] == True and keys[ord("t")] == 1 and player1[CHAR] == "ryu":
            
        if p1frames[ANI]!= "punch":
            p1frames[ANI] = "punch"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 20

    
    if player1[ISATT] == True and p1frames[ANI] == "punch" and player1[CHAR] == "ryu":
                
        p1frames[NUM] += 0.3

        if round(p1frames[NUM],0) >= 5:
            p1frames[NUM] = 0
            player1[MOVING] = False
            player1[ISATT] = False
            p1hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]

        if round(p1frames[NUM],0) == 2:
            player1[DAMAGE] = 1.25
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "punch":
            player1[SPRITE] = ryumoves[PUNCH][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "punch":
            player1[SPRITE] = transform.flip(ryumoves[PUNCH][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#KICK


    if player1[CANATT] == True and player1[ONGROUND] == True and keys[ord("y")] == 1 and player1[CHAR] == "ryu":
            
        if p1frames[ANI]!= "kick":
            p1frames[ANI] = "kick"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 25

    
    if player1[ISATT] == True and p1frames[ANI] == "kick" and player1[CHAR] == "ryu":
                
        p1frames[NUM] += 0.3
        p1hitbox[Y] = 670 - ryumoves[KICK][2].get_size()[1]

        if round(p1frames[NUM],0) >= 5:
            p1frames[NUM] = 0
            player1[MOVING] = False
            player1[ISATT] = False
            p1hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]

        if round(p1frames[NUM],0) == 3:
            player1[DAMAGE] = 1.5
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "kick":
            player1[SPRITE] = ryumoves[KICK][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "kick":
            player1[SPRITE] = transform.flip(ryumoves[KICK][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#AIRPUNCH

    if player1[CANATT] == True and player1[ONGROUND] == False and keys[ord("t")] == 1 and player1[CHAR] == "ryu":

        if p1frames[ANI]!= "airpunch":
            p1frames[ANI] = "airpunch"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 35


    if player1[ISATT] == True and p1frames[ANI] == "airpunch" and player1[CHAR] == "ryu":
                
        p1frames[NUM] += 0.1

        if round(p1frames[NUM],0) >= 3:
            p1frames[NUM] = 2
            player1[MOVING] = False
            player1[ISATT] = False

        if round(p1frames[NUM],0) == 1:
            player1[DAMAGE] = 0.5
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "airpunch":
            player1[SPRITE] = ryumoves[AIRPUNCH][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "airpunch":
            player1[SPRITE] = transform.flip(ryumoves[AIRPUNCH][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#AIRKICK

    if player1[CANATT] == True and player1[ONGROUND] == False and keys[ord("y")] == 1 and player1[CHAR] == "ryu":

        if p1frames[ANI]!= "airkick":
            p1frames[ANI] = "airkick"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 35


    if player1[ISATT] == True and p1frames[ANI] == "airkick" and player1[CHAR] == "ryu":
                
        p1frames[NUM] += 0.1

        if round(p1frames[NUM],0) >= 3:
            p1frames[NUM] = 2
            player1[MOVING] = False
            player1[ISATT] = False

        if round(p1frames[NUM],0) == 1:
            player1[DAMAGE] = 0.5
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "airkick":
            player1[SPRITE] = ryumoves[AIRKICK][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "airkick":
            player1[SPRITE] = transform.flip(ryumoves[AIRKICK][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#PUNCH
        
    if player1[CANATT] == True and player1[ONGROUND] == True and keys[ord("t")] == 1 and player1[CHAR] == "ken":
            
        if p1frames[ANI]!= "punch":
            p1frames[ANI] = "punch"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 40

    
    if player1[ISATT] == True and p1frames[ANI] == "punch" and player1[CHAR] == "ken":
                
        p1frames[NUM] += 0.2

        if round(p1frames[NUM],0) >= 7:
            p1frames[NUM] = 0
            player1[MOVING] = False
            player1[ISATT] = False
            p1hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]

        if round(p1frames[NUM],0) >= 2 and round(p1frames[NUM],0) <= 4:
            player1[DAMAGE] = 0.4
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "punch":
            player1[SPRITE] = kenmoves[PUNCH][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "punch":
            player1[SPRITE] = transform.flip(kenmoves[PUNCH][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#KICK


    if player1[CANATT] == True and player1[ONGROUND] == True and keys[ord("y")] == 1 and player1[CHAR] == "ken":
            
        if p1frames[ANI]!= "kick":
            p1frames[ANI] = "kick"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 30

    
    if player1[ISATT] == True and p1frames[ANI] == "kick" and player1[CHAR] == "ken":
                
        p1frames[NUM] += 0.25

        if round(p1frames[NUM],0) >= 5:
            p1frames[NUM] = 0
            player1[MOVING] = False
            player1[ISATT] = False
            p1hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]

        if round(p1frames[NUM],0) == 2:
            player1[DAMAGE] = 1.5
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "kick":
            player1[SPRITE] = kenmoves[KICK][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "kick":
            player1[SPRITE] = transform.flip(kenmoves[KICK][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#AIRPUNCH

    if player1[CANATT] == True and player1[ONGROUND] == False and keys[ord("t")] == 1 and player1[CHAR] == "ken":

        if p1frames[ANI]!= "airpunch":
            p1frames[ANI] = "airpunch"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 25


    if player1[ISATT] == True and p1frames[ANI] == "airpunch" and player1[CHAR] == "ken":
                
        p1frames[NUM] += 0.1

        if round(p1frames[NUM],0) >= 3:
            p1frames[NUM] = 2
            player1[MOVING] = False
            player1[ISATT] = False

        if round(p1frames[NUM],0) == 1:
            player1[DAMAGE] = 0.5
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "airpunch":
            player1[SPRITE] = kenmoves[AIRPUNCH][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "airpunch":
            player1[SPRITE] = transform.flip(kenmoves[AIRPUNCH][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#AIRKICK

    if player1[CANATT] == True and player1[ONGROUND] == False and keys[ord("y")] == 1 and player1[CHAR] == "ken":

        if p1frames[ANI]!= "airkick":
            p1frames[ANI] = "airkick"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 25


    if player1[ISATT] == True and p1frames[ANI] == "airkick" and player1[CHAR] == "ken":
                
        p1frames[NUM] += 0.2

        if round(p1frames[NUM],0) >= 4:
            p1frames[NUM] = 3
            player1[MOVING] = False
            player1[ISATT] = False

        if round(p1frames[NUM],0) == 1:
            player1[DAMAGE] = 1
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "airkick":
            player1[SPRITE] = kenmoves[AIRKICK][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "airkick":
            player1[SPRITE] = transform.flip(kenmoves[AIRKICK][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

#========================================
#PUNCH
        
    if player1[CANATT] == True and player1[ONGROUND] == True and keys[ord("t")] == 1 and player1[CHAR] == "bison":
            
        if p1frames[ANI]!= "punch":
            p1frames[ANI] = "punch"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 30

    
    if player1[ISATT] == True and p1frames[ANI] == "punch" and player1[CHAR] == "bison":
                
        p1frames[NUM] += 0.2

        if round(p1frames[NUM],0) >= 4:
            p1frames[NUM] = 0
            player1[MOVING] = False
            player1[ISATT] = False
            p1hitbox[Y] = 670 - bisonmoves[IDLE][0].get_size()[1]

        if round(p1frames[NUM],0) >= 2:
            player1[DAMAGE] = 0.6
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "punch":
            player1[SPRITE] = bisonmoves[PUNCH][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "punch":
            player1[SPRITE] = transform.flip(bisonmoves[PUNCH][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#KICK


    if player1[CANATT] == True and player1[ONGROUND] == True and keys[ord("y")] == 1 and player1[CHAR] == "bison":
            
        if p1frames[ANI]!= "kick":
            p1frames[ANI] = "kick"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 20

    
    if player1[ISATT] == True and p1frames[ANI] == "kick" and player1[CHAR] == "bison":
                
        p1frames[NUM] += 0.3

        if round(p1frames[NUM],0) >= 4:
            p1frames[NUM] = 0
            player1[MOVING] = False
            player1[ISATT] = False
            p1hitbox[Y] = 670 - bisonmoves[IDLE][0].get_size()[1]

        if round(p1frames[NUM],0) == 2:
            player1[DAMAGE] = 1.25
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "kick":
            player1[SPRITE] = bisonmoves[KICK][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "kick":
            player1[SPRITE] = transform.flip(bisonmoves[KICK][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

#========================================
#AIRPUNCH
        
    if player1[CANATT] == True and player1[ONGROUND] == False and keys[ord("t")] == 1 and player1[CHAR] == "bison":

        if p1frames[ANI]!= "airpunch":
            p1frames[ANI] = "airpunch"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 25


    if player1[ISATT] == True and p1frames[ANI] == "airpunch" and player1[CHAR] == "bison":
                
        p1frames[NUM] += 0.35

        if round(p1frames[NUM],0) >= 6:
            p1frames[NUM] = 5
            player1[MOVING] = False
            player1[ISATT] = False

        if round(p1frames[NUM],0) >= 3 and round(p1frames[NUM],0) <= 4:
            player1[DAMAGE] = 0.8
        else: player1[DAMAGE] = False

        if player1[RIGHT] == True and p1frames[ANI] == "airpunch":
            player1[SPRITE] = bisonmoves[AIRPUNCH][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "airpunch":
            player1[SPRITE] = transform.flip(bisonmoves[AIRPUNCH][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================
#AIRKICK

    if player1[CANATT] == True and player1[ONGROUND] == False and keys[ord("y")] == 1 and player1[CHAR] == "bison":

        if p1frames[ANI]!= "airkick":
            p1frames[ANI] = "airkick"
            p1frames[NUM] = 0

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1delay[WAITTIME] = 20
        


    if player1[ISATT] == True and p1frames[ANI] == "airkick" and player1[CHAR] == "bison":
                
        p1frames[NUM] += 0.15

        if round(p1frames[NUM],0) >= 3:
            p1frames[NUM] = 2
            player1[MOVING] = False
            player1[ISATT] = False

        if round(p1frames[NUM],0) == 1:
            player1[DAMAGE] = 0.7
        else: player1[DAMAGE] = False


        if player1[RIGHT] == True and p1frames[ANI] == "airkick":
            player1[SPRITE] = bisonmoves[AIRKICK][int(round(p1frames[NUM],0))]
        elif player1[RIGHT] == False and p1frames[ANI] == "airkick":
            player1[SPRITE] = transform.flip(bisonmoves[AIRKICK][int(round(p1frames[NUM],0))],1,0)

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================




def attp2():
    global p2frames

#========================================
#PUNCH
    
    if player2[CANATT] == True and player2[ONGROUND] == True and keys[ord("j")] == 1 and player2[CHAR] == "ryu":
            
        if p2frames[ANI]!= "punch":
            p2frames[ANI] = "punch"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 20

    
    if player2[ISATT] == True and p2frames[ANI] == "punch" and player2[CHAR] == "ryu":
                
        p2frames[NUM] += 0.3

        if round(p2frames[NUM],0) >= 5:
            p2frames[NUM] = 0
            player2[MOVING] = False
            player2[ISATT] = False
            p2hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]

        if round(p2frames[NUM],0) == 2:
            player2[DAMAGE] = 1.25
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "punch":
            player2[SPRITE] = ryumoves[PUNCH][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "punch":
            player2[SPRITE] = transform.flip(ryumoves[PUNCH][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#KICK


    if player2[CANATT] == True and player2[ONGROUND] == True and keys[ord("k")] == 1 and player2[CHAR] == "ryu":
            
        if p2frames[ANI]!= "kick":
            p2frames[ANI] = "kick"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 25

    
    if player2[ISATT] == True and p2frames[ANI] == "kick" and player2[CHAR] == "ryu":
                
        p2frames[NUM] += 0.3
        p2hitbox[Y] = 670 - ryumoves[KICK][2].get_size()[1]

        if round(p2frames[NUM],0) >= 5:
            p2frames[NUM] = 0
            player2[MOVING] = False
            player2[ISATT] = False
            p2hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]

        if round(p2frames[NUM],0) == 3:
            player2[DAMAGE] = 1.5
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "kick":
            player2[SPRITE] = ryumoves[KICK][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "kick":
            player2[SPRITE] = transform.flip(ryumoves[KICK][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#AIRPUNCH

    if player2[CANATT] == True and player2[ONGROUND] == False and keys[ord("j")] == 1 and player2[CHAR] == "ryu":

        if p2frames[ANI]!= "airpunch":
            p2frames[ANI] = "airpunch"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 35


    if player2[ISATT] == True and p2frames[ANI] == "airpunch" and player2[CHAR] == "ryu":
                
        p2frames[NUM] += 0.1

        if round(p2frames[NUM],0) >= 3:
            p2frames[NUM] = 2
            player2[MOVING] = False
            player2[ISATT] = False

        if round(p2frames[NUM],0) == 1:
            player2[DAMAGE] = 0.5
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "airpunch":
            player2[SPRITE] = ryumoves[AIRPUNCH][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "airpunch":
            player2[SPRITE] = transform.flip(ryumoves[AIRPUNCH][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#AIRKICK

    if player2[CANATT] == True and player2[ONGROUND] == False and keys[ord("k")] == 1 and player2[CHAR] == "ryu":

        if p2frames[ANI]!= "airkick":
            p2frames[ANI] = "airkick"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 35


    if player2[ISATT] == True and p2frames[ANI] == "airkick" and player2[CHAR] == "ryu":
                
        p2frames[NUM] += 0.1

        if round(p2frames[NUM],0) >= 3:
            p2frames[NUM] = 2
            player2[MOVING] = False
            player2[ISATT] = False

        if round(p2frames[NUM],0) == 1:
            player2[DAMAGE] = 0.5
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "airkick":
            player2[SPRITE] = ryumoves[AIRKICK][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "airkick":
            player2[SPRITE] = transform.flip(ryumoves[AIRKICK][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#PUNCH
        
    if player2[CANATT] == True and player2[ONGROUND] == True and keys[ord("j")] == 1 and player2[CHAR] == "ken":
            
        if p2frames[ANI]!= "punch":
            p2frames[ANI] = "punch"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 40

    
    if player2[ISATT] == True and p2frames[ANI] == "punch" and player2[CHAR] == "ken":
                
        p2frames[NUM] += 0.2

        if round(p2frames[NUM],0) >= 7:
            p2frames[NUM] = 0
            player2[MOVING] = False
            player2[ISATT] = False
            p2hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]

        if round(p2frames[NUM],0) >= 2 and round(p2frames[NUM],0) <= 4:
            player2[DAMAGE] = 0.4
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "punch":
            player2[SPRITE] = kenmoves[PUNCH][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "punch":
            player2[SPRITE] = transform.flip(kenmoves[PUNCH][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#KICK


    if player2[CANATT] == True and player2[ONGROUND] == True and keys[ord("k")] == 1 and player2[CHAR] == "ken":
            
        if p2frames[ANI]!= "kick":
            p2frames[ANI] = "kick"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 30

    
    if player2[ISATT] == True and p2frames[ANI] == "kick" and player2[CHAR] == "ken":
                
        p2frames[NUM] += 0.25

        if round(p2frames[NUM],0) >= 5:
            p2frames[NUM] = 0
            player2[MOVING] = False
            player2[ISATT] = False
            p2hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]

        if round(p2frames[NUM],0) == 2:
            player2[DAMAGE] = 1.5
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "kick":
            player2[SPRITE] = kenmoves[KICK][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "kick":
            player2[SPRITE] = transform.flip(kenmoves[KICK][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#AIRPUNCH

    if player2[CANATT] == True and player2[ONGROUND] == False and keys[ord("j")] == 1 and player2[CHAR] == "ken":

        if p2frames[ANI]!= "airpunch":
            p2frames[ANI] = "airpunch"
            p2frames[NUM] = 0
            p2delay[WAITTIME] = 25

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True


    if player2[ISATT] == True and p2frames[ANI] == "airpunch" and player2[CHAR] == "ken":
                
        p2frames[NUM] += 0.1

        if round(p2frames[NUM],0) >= 3:
            p2frames[NUM] = 2
            player2[MOVING] = False
            player2[ISATT] = False

        if round(p2frames[NUM],0) == 1:
            player2[DAMAGE] = 0.5
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "airpunch":
            player2[SPRITE] = kenmoves[AIRPUNCH][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "airpunch":
            player2[SPRITE] = transform.flip(kenmoves[AIRPUNCH][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#AIRKICK

    if player2[CANATT] == True and player2[ONGROUND] == False and keys[ord("k")] == 1 and player2[CHAR] == "ken":

        if p2frames[ANI]!= "airkick":
            p2frames[ANI] = "airkick"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 25


    if player2[ISATT] == True and p2frames[ANI] == "airkick" and player2[CHAR] == "ken":
                
        p2frames[NUM] += 0.2

        if round(p2frames[NUM],0) >= 4:
            p2frames[NUM] = 3
            player2[MOVING] = False
            player2[ISATT] = False

        if round(p2frames[NUM],0) == 1:
            player2[DAMAGE] = 1
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "airkick":
            player2[SPRITE] = kenmoves[AIRKICK][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "airkick":
            player2[SPRITE] = transform.flip(kenmoves[AIRKICK][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================

#========================================
#PUNCH
        
    if player2[CANATT] == True and player2[ONGROUND] == True and keys[ord("j")] == 1 and player2[CHAR] == "bison":
            
        if p2frames[ANI]!= "punch":
            p2frames[ANI] = "punch"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 30

    
    if player2[ISATT] == True and p2frames[ANI] == "punch" and player2[CHAR] == "bison":
                
        p2frames[NUM] += 0.2

        if round(p2frames[NUM],0) >= 4:
            p2frames[NUM] = 0
            player2[MOVING] = False
            player2[ISATT] = False
            p2hitbox[Y] = 670 - bisonmoves[IDLE][0].get_size()[1]

        if round(p2frames[NUM],0) >= 2:
            player2[DAMAGE] = 0.6
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "punch":
            player2[SPRITE] = bisonmoves[PUNCH][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "punch":
            player2[SPRITE] = transform.flip(bisonmoves[PUNCH][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#KICK


    if player2[CANATT] == True and player2[ONGROUND] == True and keys[ord("k")] == 1 and player2[CHAR] == "bison":
            
        if p2frames[ANI]!= "kick":
            p2frames[ANI] = "kick"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 20

    
    if player2[ISATT] == True and p2frames[ANI] == "kick" and player2[CHAR] == "bison":
                
        p2frames[NUM] += 0.3

        if round(p2frames[NUM],0) >= 4:
            p2frames[NUM] = 0
            player2[MOVING] = False
            player2[ISATT] = False
            p2hitbox[Y] = 670 - bisonmoves[IDLE][0].get_size()[1]

        if round(p2frames[NUM],0) == 2:
            player2[DAMAGE] = 1.25
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "kick":
            player2[SPRITE] = bisonmoves[KICK][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "kick":
            player2[SPRITE] = transform.flip(bisonmoves[KICK][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]
#========================================

#========================================
#AIRPUNCH
        
    if player2[CANATT] == True and player2[ONGROUND] == False and keys[ord("j")] == 1 and player2[CHAR] == "bison":

        if p2frames[ANI]!= "airpunch":
            p2frames[ANI] = "airpunch"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 25


    if player2[ISATT] == True and p2frames[ANI] == "airpunch" and player2[CHAR] == "bison":
                
        p2frames[NUM] += 0.35

        if round(p2frames[NUM],0) >= 6:
            p2frames[NUM] = 5
            player2[MOVING] = False
            player2[ISATT] = False

        if round(p2frames[NUM],0) >= 3 and round(p2frames[NUM],0) <= 4:
            player2[DAMAGE] = 0.8
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "airpunch":
            player2[SPRITE] = bisonmoves[AIRPUNCH][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "airpunch":
            player2[SPRITE] = transform.flip(bisonmoves[AIRPUNCH][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================
#AIRKICK

    if player2[CANATT] == True and player2[ONGROUND] == False and keys[ord("k")] == 1 and player2[CHAR] == "bison":

        if p2frames[ANI]!= "airkick":
            p2frames[ANI] = "airkick"
            p2frames[NUM] = 0

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2delay[WAITTIME] = 20


    if player2[ISATT] == True and p2frames[ANI] == "airkick" and player2[CHAR] == "bison":
                
        p2frames[NUM] += 0.15

        if round(p2frames[NUM],0) >= 3:
            p2frames[NUM] = 2
            player2[MOVING] = False
            player2[ISATT] = False

        if round(p2frames[NUM],0) == 1:
            player2[DAMAGE] = 0.7
        else: player2[DAMAGE] = False

        if player2[RIGHT] == True and p2frames[ANI] == "airkick":
            player2[SPRITE] = bisonmoves[AIRKICK][int(round(p2frames[NUM],0))]
        elif player2[RIGHT] == False and p2frames[ANI] == "airkick":
            player2[SPRITE] = transform.flip(bisonmoves[AIRKICK][int(round(p2frames[NUM],0))],1,0)

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]
#========================================






def wait():
    global p1delay,p2delay
    if p1delay[WAITING] == p1delay[WAITTIME]:
        player1[CANATT] = True
        p1delay = [False,False]
    else:
        p1delay[WAITING] += 1
        player1[CANATT] = False

    if p2delay[WAITING] == p2delay[WAITTIME]:
        player2[CANATT] = True
        p2delay = [False,False]
    else:
        p2delay[WAITING] += 1
        player2[CANATT] = False







    
def gravity():
    if player1[ONGROUND] == False:
        p1hitbox[Y] -= player1[VEL]
        player1[VEL] -= 1

    if p1hit.colliderect(ground):
        player1[ONGROUND] = True
        player1[VEL] = False
        if player1[CHAR] == "ryu": p1hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]
        elif player1[CHAR] == "ken": p1hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]
        else: p1hitbox[Y] = 670 - bisonmoves[WALK][0].get_size()[1]
        player1[MOVING] = False

    if player2[ONGROUND] == False:
        p2hitbox[Y] -= player2[VEL]
        player2[VEL] -= 1

    if p2hit.colliderect(ground):
        player2[ONGROUND] = True
        player2[VEL] = False
        if player2[CHAR] == "ryu": p2hitbox[Y] = 670 - ryumoves[IDLE][0].get_size()[1]
        elif player2[CHAR] == "ken": p2hitbox[Y] = 670 - kenmoves[IDLE][0].get_size()[1]
        else: p2hitbox[Y] = 670 - bisonmoves[WALK][0].get_size()[1]
        player2[MOVING] = False



def drawScene():
    screen.blit(stages[2],(0,0))
    screen.blit(player1[SPRITE],(p1hitbox[X],p1hitbox[Y]))
    screen.blit(player2[SPRITE],(p2hitbox[X],p2hitbox[Y]))
    #draw.rect(screen,(255,255,255),p1hit,1)#<temp
    #draw.rect(screen,(255,255,255),p2hit,1)#<temp
    for i in range(0,len(hadouken1)):
        if hadouken1[i][2] == True:
            if player1[CHAR] == "ryu":
                screen.blit(ryumoves[PROJ][1],(hadouken1[i][X],hadouken1[i][Y]))
            elif player1[CHAR] == "ken":
                screen.blit(kenmoves[PROJ][0],(hadouken1[i][X],hadouken1[i][Y]))
        else:
            if player1[CHAR] == "ryu":
                screen.blit(transform.flip(ryumoves[PROJ][1],1,0),(hadouken1[i][X],hadouken1[i][Y]))
            elif player1[CHAR] == "ken":
                screen.blit(transform.flip(kenmoves[PROJ][0],1,0),(hadouken1[i][X],hadouken1[i][Y]))

    for i in range(0,len(hadouken2)):
        if hadouken2[i][2] == True:
            if player2[CHAR] == "ryu":
                screen.blit(ryumoves[PROJ][1],(hadouken2[i][X],hadouken2[i][Y]))
            elif player2[CHAR] == "ken":
                screen.blit(kenmoves[PROJ][0],(hadouken2[i][X],hadouken2[i][Y]))
        else:
            if player2[CHAR] == "ryu":
                screen.blit(transform.flip(ryumoves[PROJ][1],1,0),(hadouken2[i][X],hadouken2[i][Y]))
            elif player2[CHAR] == "ken":
                screen.blit(transform.flip(kenmoves[PROJ][0],1,0),(hadouken2[i][X],hadouken2[i][Y]))

    draw.rect(screen,(255,255,255),(50,50,300,50))
    draw.rect(screen,(255,255,255),(674,50,300,50))
    if player1[HP] > 0:
        draw.rect(screen,(255,0,0),(50,50,player1[HP]*3,50))
    if player2[HP] > 0:
        draw.rect(screen,(255,0,0),(974-player2[HP]*3,50,player2[HP]*3,50))
    draw.rect(screen,(0,0,0),(50,50,300,50),3)
    draw.rect(screen,(0,0,0),(674,50,300,50),3)

    if player1[CHAR] == "ryu":
        draw.rect(screen,(255,255,255),(370,20,mugshots[0].get_size()[0],mugshots[0].get_size()[1]))
        screen.blit(mugshots[0],(370,20))
        draw.rect(screen,(0,0,0),(370,20,mugshots[0].get_size()[0],mugshots[0].get_size()[1]),3)
    if player1[CHAR] == "ken":
        draw.rect(screen,(255,255,255),(370,20,mugshots[1].get_size()[0],mugshots[1].get_size()[1]))
        screen.blit(mugshots[1],(370,20))
        draw.rect(screen,(0,0,0),(370,20,mugshots[1].get_size()[0],mugshots[1].get_size()[1]),3)
    if player1[CHAR] == "bison":
        draw.rect(screen,(255,255,255),(370,20,mugshots[2].get_size()[0],mugshots[2].get_size()[1]))
        screen.blit(mugshots[2],(370,20))
        draw.rect(screen,(0,0,0),(370,20,mugshots[2].get_size()[0],mugshots[2].get_size()[1]),3)    

    if player2[CHAR] == "ryu":
        draw.rect(screen,(255,255,255),(581,20,mugshots[0].get_size()[0],mugshots[0].get_size()[1]))
        screen.blit(transform.flip(mugshots[0],1,0),(581,20))
        draw.rect(screen,(0,0,0),(581,20,mugshots[0].get_size()[0],mugshots[0].get_size()[1]),3)
    if player2[CHAR] == "ken":
        draw.rect(screen,(255,255,255),(581,20,mugshots[1].get_size()[0],mugshots[1].get_size()[1]))
        screen.blit(transform.flip(mugshots[1],1,0),(581,20))
        draw.rect(screen,(0,0,0),(581,20,mugshots[1].get_size()[0],mugshots[1].get_size()[1]),3)
    if player2[CHAR] == "bison":
        draw.rect(screen,(255,255,255),(581,20,mugshots[2].get_size()[0],mugshots[2].get_size()[1]))
        screen.blit(transform.flip(mugshots[2],1,0),(581,20))
        draw.rect(screen,(0,0,0),(581,20,mugshots[2].get_size()[0],mugshots[2].get_size()[1]),3)


    if player2[ALIVE] == False and player1[CHAR] == "ryu": screen.blit(texts[4],(325,350))
    if player2[ALIVE] == False and player1[CHAR] == "ken": screen.blit(texts[5],(325,350))
    if player2[ALIVE] == False and player1[CHAR] == "bison": screen.blit(texts[6],(200,350))

    if player1[ALIVE] == False and player2[CHAR] == "ryu": screen.blit(texts[4],(325,350))
    if player1[ALIVE] == False and player2[CHAR] == "ken": screen.blit(texts[5],(325,350))
    if player1[ALIVE] == False and player2[CHAR] == "bison": screen.blit(texts[6],(200,350))

    screen.blit(vs,(463,40))


def hadoukenp1():
    global hadoukenflag1,hadoukenflag2,hadouken1,hadouken2
    if hadoukenflag1 == True:
        if player1[CHAR] == "ryu":
            
            if player1[RIGHT] == True:
                hadouken1.append([p1hitbox[X]+ryumoves[SPECIAL][4].get_size()[0], 585, True])
            else:
                hadouken1.append([p1hitbox[X]-ryumoves[PROJ][1].get_size()[0], 585, False])
            hadoukenflag1 = False
            
        elif player1[CHAR] == "ken":
            
            if player1[RIGHT] == True:
                hadouken1.append([p1hitbox[X]+kenmoves[SPECIAL][3].get_size()[0], 595, True])
            else:
                hadouken1.append([p1hitbox[X]-kenmoves[PROJ][0].get_size()[0], 595, False])
            hadoukenflag1 = False

    for i in range(len(hadouken1)-1,0,-1):
        if hadouken1[i][2] == True:
            hadouken1[i][X] += 5
        else:
            hadouken1[i][X] -= 5

        if hadouken1[i][X] >= 1100 or hadouken1[i][X] <= -50:
            hadouken1.remove(hadouken1[i])

def hadoukenp2():
    global hadoukenflag1,hadoukenflag2,hadouken1,hadouken2
    if hadoukenflag2 == True:
        if player2[CHAR] == "ryu":
            
            if player2[RIGHT] == True:
                hadouken2.append([p2hitbox[X]+ryumoves[SPECIAL][4].get_size()[0], 585, True])
            else:
                hadouken2.append([p2hitbox[X]-ryumoves[PROJ][1].get_size()[0], 585, False])
            hadoukenflag2 = False
            
        elif player2[CHAR] == "ken":
            
            if player2[RIGHT] == True:
                hadouken2.append([p2hitbox[X]+kenmoves[SPECIAL][3].get_size()[0], 595, True])
            else:
                hadouken2.append([p2hitbox[X]-kenmoves[PROJ][0].get_size()[0], 595, False])
            hadoukenflag2 = False

    for i in range(len(hadouken2)-1,0,-1):
        if hadouken2[i][2] == True:
            hadouken2[i][X] += 5
        else:
            hadouken2[i][X] -= 5

        if hadouken2[i][X] >= 1100 or hadouken2[i][X] <= -50:
            hadouken2.remove(hadouken2[i])







def p1hitp2():
    if player1[DAMAGE] != False and p1hit.colliderect(p2hit):
        player2[HP] -= player1[DAMAGE]
        player2[DAMAGE] = False

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        
        if player2[HP] > 0:
            p2frames[ANI] = "hit"
            p2delay[WAITTIME] = 20
        else:
            p2frames[ANI] = "ko"
            player2[HP] = 0

    if player1[CHAR] == "ryu":
        for i in range(len(hadouken1)-1,0,-1):
            if Rect(hadouken1[i][X],hadouken1[i][Y],ryumoves[PROJ][1].get_size()[0],ryumoves[PROJ][1].get_size()[1]).colliderect(p2hitbox):
                hadouken1.remove(hadouken1[i])
                player2[HP] -= 2
                if player2[HP] > 0: p2frames[ANI] = "hit"
                else: p2frames[ANI] = "ko"

    if player1[CHAR] == "ken":
        for i in range(len(hadouken1)-1,0,-1):
            if Rect(hadouken1[i][X],hadouken1[i][Y],kenmoves[PROJ][0].get_size()[0],kenmoves[PROJ][0].get_size()[1]).colliderect(p2hitbox):
                hadouken1.remove(hadouken1[i])
                player2[HP] -= 2
                if player2[HP] > 0: p2frames[ANI] = "hit"
                else: p2frames[ANI] = "ko"

    if player2[CHAR] == "ryu":
        
        if p2frames[ANI] == "hit" and player2[HP] > 0:
            
            p2frames[NUM] += 0.2

            player2[MOVING] = True
            player2[ISATT] = True
            
            if round(p2frames[NUM],0) >= 4:
                p2frames[NUM] = 0
                player2[MOVING] = False
                player2[ISATT] = False

            if player1[RIGHT] == False and p2frames[ANI] == "hit":
                player2[RIGHT] = True
                p2hitbox[X] -= 2
                player2[SPRITE] = ryumoves[HIT][int(round(p2frames[NUM],0))]
            elif player1[RIGHT] == True and p2frames[ANI] == "hit":
                player2[RIGHT] = False
                p2hitbox[X] += 2
                player2[SPRITE] = transform.flip(ryumoves[HIT][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]


    if player2[CHAR] == "ken":
        
        if p2frames[ANI] == "hit" and player2[HP] > 0:
            
            p2frames[NUM] += 0.2

            player2[MOVING] = True
            player2[ISATT] = True

            if round(p2frames[NUM],0) >= 4:
                p2frames[NUM] = 0
                player2[MOVING] = False
                player2[ISATT] = False

            if player1[RIGHT] == False and p2frames[ANI] == "hit":
                player2[RIGHT] = True
                p2hitbox[X] -= 2
                player2[SPRITE] = kenmoves[HIT][int(round(p2frames[NUM],0))]
            elif player1[RIGHT] == True and p2frames[ANI] == "hit":
                player2[RIGHT] = False
                p2hitbox[X] += 2
                player2[SPRITE] = transform.flip(kenmoves[HIT][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]


    if player2[CHAR] == "bison":
        if p2frames[ANI] == "hit" and player2[HP] > 0:
            
            p2frames[NUM] += 0.04

            player2[MOVING] = True
            player2[ISATT] = True

            if round(p2frames[NUM],0) >= 1:
                p2frames[NUM] = 0
                player2[MOVING] = False
                player2[ISATT] = False

            if player1[RIGHT] == False and p2frames[ANI] == "hit":
                player2[RIGHT] = True
                p2hitbox[X] -= 2
                player2[SPRITE] = bisonmoves[HIT][int(round(p2frames[NUM],0))]
            elif player1[RIGHT] == True and p2frames[ANI] == "hit":
                player2[RIGHT] = False
                p2hitbox[X] += 2
                player2[SPRITE] = transform.flip(bisonmoves[HIT][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]


#============================


def p2hitp1():
    if player2[DAMAGE] != False and p2hit.colliderect(p1hit):
        player1[HP] -= player2[DAMAGE]
        player1[DAMAGE] = False

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        
        if player1[HP] > 0:
            p1frames[ANI] = "hit"
            p1delay[WAITTIME] = 20
        else:
            p1frames[ANI] = "ko"
            player1[HP] = 0

    if player2[CHAR] == "ryu":
        for i in range(len(hadouken2)-1,0,-1):
            if Rect(hadouken2[i][X],hadouken2[i][Y],ryumoves[PROJ][1].get_size()[0],ryumoves[PROJ][1].get_size()[1]).colliderect(p1hitbox):
                hadouken2.remove(hadouken2[i])
                player1[HP] -= 2
                if player1[HP] > 0: p1frames[ANI] = "hit"
                else: p1frames[ANI] = "ko"

    if player2[CHAR] == "ken":
        for i in range(len(hadouken2)-1,0,-1):
            if Rect(hadouken2[i][X],hadouken2[i][Y],kenmoves[PROJ][0].get_size()[0],kenmoves[PROJ][0].get_size()[1]).colliderect(p1hitbox):
                hadouken2.remove(hadouken2[i])
                player1[HP] -= 2
                if player1[HP] > 0: p1frames[ANI] = "hit"
                else: p1frames[ANI] = "ko"
    
    if player1[CHAR] == "ryu":
        if p1frames[ANI] == "hit" and player1[HP] > 0:
            
            p1frames[NUM] += 0.2

            player1[MOVING] = True
            player1[ISATT] = True

            if round(p1frames[NUM],0) >= 4:
                p1frames[NUM] = 0
                player1[MOVING] = False
                player1[ISATT] = False

            if player2[RIGHT] == False and p1frames[ANI] == "hit":
                player1[RIGHT] = True
                p1hitbox[X] -= 2
                player1[SPRITE] = ryumoves[HIT][int(round(p1frames[NUM],0))]
            elif player2[RIGHT] == True and p1frames[ANI] == "hit":
                player1[RIGHT] = False
                p1hitbox[X] += 2
                player1[SPRITE] = transform.flip(ryumoves[HIT][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]


    if player1[CHAR] == "ken":
        if p1frames[ANI] == "hit" and player1[HP] > 0:
            
            p1frames[NUM] += 0.2

            player1[MOVING] = True
            player1[ISATT] = True

            if round(p1frames[NUM],0) >= 4:
                p1frames[NUM] = 0
                player1[MOVING] = False
                player1[ISATT] = False
    
            if player2[RIGHT] == False and p1frames[ANI] == "hit":
                player1[RIGHT] = True
                p1hitbox[X] -= 2
                player1[SPRITE] = kenmoves[HIT][int(round(p1frames[NUM],0))]
            elif player2[RIGHT] == True and p1frames[ANI] == "hit":
                player1[RIGHT] = False
                p1hitbox[X] += 2
                player1[SPRITE] = transform.flip(kenmoves[HIT][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]


    if player1[CHAR] == "bison":
        if p1frames[ANI] == "hit" and player1[HP] > 0:
            
            p1frames[NUM] += 0.04

            player1[MOVING] = True
            player1[ISATT] = True

            if round(p1frames[NUM],0) >= 1:
                p1frames[NUM] = 0
                player1[MOVING] = False
                player1[ISATT] = False
                

            if player2[RIGHT] == False and p1frames[ANI] == "hit":
                player1[RIGHT] = True
                p1hitbox[X] -= 2
                player1[SPRITE] = bisonmoves[HIT][int(round(p1frames[NUM],0))]
            elif player2[RIGHT] == True and p1frames[ANI] == "hit":
                player1[RIGHT] = False
                p1hitbox[X] += 2
                player1[SPRITE] = transform.flip(bisonmoves[HIT][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

#============================

def kop1():

    if player1[CHAR] == "ryu" and player1[ALIVE] == True:
        if player1[HP] <= 0 or p1frames[ANI] == "ko":

            p1frames[ANI] = "ko"
            p1frames[NUM] += 0.1
            player1[ISATT] = True
            player1[CANATT] = False
            player1[MOVING] = True
            p1hitbox[Y] = 670 - ryumoves[KO][0].get_size()[1]

            if round(p1frames[NUM],0) >= 5:
                p1frames[NUM] = 4
                player1[MOVING] = False
                player1[ISATT] = False
                player1[ALIVE] = False

            if player1[RIGHT] == True and p1frames[ANI] == "ko":
                player1[RIGHT] = True
                player1[SPRITE] = ryumoves[KO][int(round(p1frames[NUM],0))]
            elif player1[RIGHT] == False and p1frames[ANI] == "ko":
                player1[RIGHT] = False
                player1[SPRITE] = transform.flip(ryumoves[KO][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

    if player1[CHAR] == "ryu" and player1[ALIVE] == False:
        
        if player1[RIGHT] == False:
            player1[SPRITE] = transform.flip(ryumoves[KO][4],1,0)
        if player1[RIGHT] == True:
            player1[SPRITE] = ryumoves[KO][4]

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1hitbox[Y] = 670 - ryumoves[KO][4].get_size()[1]



    if player1[ALIVE] == False and player2[CHAR] == "ryu":
        
        p2frames[ANI] = "win"
        p2frames[NUM] += 0.1
        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True

        if round(p2frames[NUM],0) >= 6:
            p2frames[NUM] = 6
            score[1] += 1

        player2[RIGHT] = True
        player2[SPRITE] = ryumoves[WIN][int(round(p2frames[NUM],0))]

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

#============================

    if player1[CHAR] == "ken" and player1[ALIVE] == True:
        if player1[HP] <= 0 or p1frames[ANI] == "ko":

            p1frames[ANI] = "ko"
            p1frames[NUM] += 0.1
            player1[ISATT] = True
            player1[CANATT] = False
            player1[MOVING] = True
            p1hitbox[Y] = 670 - kenmoves[KO][0].get_size()[1]

            if round(p1frames[NUM],0) >= 5:
                p1frames[NUM] = 4
                player1[MOVING] = False
                player1[ISATT] = False
                player1[ALIVE] = False

            if player1[RIGHT] == True and p1frames[ANI] == "ko":
                player1[RIGHT] = True
                player1[SPRITE] = kenmoves[KO][int(round(p1frames[NUM],0))]
            elif player1[RIGHT] == False and p1frames[ANI] == "ko":
                player1[RIGHT] = False
                player1[SPRITE] = transform.flip(kenmoves[KO][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

    if player1[CHAR] == "ken" and player1[ALIVE] == False:
        
        if player1[RIGHT] == False:
            player1[SPRITE] = transform.flip(kenmoves[KO][4],1,0)
        if player1[RIGHT] == True:
            player1[SPRITE] = kenmoves[KO][4]

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1hitbox[Y] = 670 - kenmoves[KO][4].get_size()[1]


    if player1[ALIVE] == False and player2[CHAR] == "ken":
        
        p2frames[ANI] = "win"
        p2frames[NUM] += 0.1
        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True

        if round(p2frames[NUM],0) >= 2:
            p2frames[NUM] = 2
            score[1] += 1

        player2[RIGHT] = True
        player2[SPRITE] = kenmoves[WIN][int(round(p2frames[NUM],0))]

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

#============================


    if player1[CHAR] == "bison" and player1[ALIVE] == True:
        if player1[HP] <= 0 or p1frames[ANI] == "ko":

            p1frames[ANI] = "ko"
            p1frames[NUM] += 0.1
            player1[ISATT] = True
            player1[CANATT] = False
            player1[MOVING] = True
            p1hitbox[Y] = 670 - bisonmoves[KO][0].get_size()[1]

            if round(p1frames[NUM],0) >= 4:
                p1frames[NUM] = 3
                player1[MOVING] = False
                player1[ISATT] = False
                player1[ALIVE] = False

            if player1[RIGHT] == True and p1frames[ANI] == "ko":
                player1[RIGHT] = True
                player1[SPRITE] = bisonmoves[KO][int(round(p1frames[NUM],0))]
            elif player1[RIGHT] == False and p1frames[ANI] == "ko":
                player1[RIGHT] = False
                player1[SPRITE] = transform.flip(bisonmoves[KO][int(round(p1frames[NUM],0))],1,0)

            p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

    if player1[CHAR] == "bison" and player1[ALIVE] == False:
        
        if player1[RIGHT] == False:
            player1[SPRITE] = transform.flip(bisonmoves[KO][3],1,0)
        if player1[RIGHT] == True:
            player1[SPRITE] = bisonmoves[KO][3]

        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        p1hitbox[Y] = 670 - bisonmoves[KO][3].get_size()[1]


    if player1[ALIVE] == False and player2[CHAR] == "bison":
        
        p2frames[ANI] = "win"
        p2frames[NUM] += 0.1
        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True

        if round(p2frames[NUM],0) >= 3:
            p2frames[NUM] = 3
            score[1] += 1

        player2[RIGHT] = True
        player2[SPRITE] = bisonmoves[WIN][int(round(p2frames[NUM],0))]

        p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

#============================

def kop2():

    if player2[CHAR] == "ryu" and player2[ALIVE] == True:
        if player2[HP] <= 0 or p2frames[ANI] == "ko":

            p2frames[ANI] = "ko"
            p2frames[NUM] += 0.1
            player2[ISATT] = True
            player2[CANATT] = False
            player2[MOVING] = True
            p2hitbox[Y] = 670 - ryumoves[KO][0].get_size()[1]

            if round(p2frames[NUM],0) >= 5:
                p2frames[NUM] = 4
                player2[MOVING] = False
                player2[ISATT] = False
                player2[ALIVE] = False

            if player2[RIGHT] == True and p2frames[ANI] == "ko":
                player2[RIGHT] = True
                player2[SPRITE] = ryumoves[KO][int(round(p2frames[NUM],0))]
            elif player2[RIGHT] == False and p2frames[ANI] == "ko":
                player2[RIGHT] = False
                player2[SPRITE] = transform.flip(ryumoves[KO][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

    if player2[CHAR] == "ryu" and player2[ALIVE] == False:
        
        if player2[RIGHT] == False:
            player2[SPRITE] = transform.flip(ryumoves[KO][4],1,0)
        if player2[RIGHT] == True:
            player2[SPRITE] = ryumoves[KO][4]

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2hitbox[Y] = 670 - ryumoves[KO][4].get_size()[1]



    if player2[ALIVE] == False and player1[CHAR] == "ryu":
        
        p1frames[ANI] = "win"
        p1frames[NUM] += 0.1
        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True
        
        if round(p1frames[NUM],0) >= 6:
            p1frames[NUM] = 6
            score[0] += 1

        player1[RIGHT] = True
        player1[SPRITE] = ryumoves[WIN][int(round(p1frames[NUM],0))]

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

        

#============================

    if player2[CHAR] == "ken" and player2[ALIVE] == True:
        if player2[HP] <= 0 or p2frames[ANI] == "ko":

            p2frames[ANI] = "ko"
            p2frames[NUM] += 0.1
            player2[ISATT] = True
            player2[CANATT] = False
            player2[MOVING] = True
            p2hitbox[Y] = 670 - kenmoves[KO][0].get_size()[1]

            if round(p2frames[NUM],0) >= 5:
                p2frames[NUM] = 4
                player2[MOVING] = False
                player2[ISATT] = False
                player2[ALIVE] = False

            if player2[RIGHT] == True and p2frames[ANI] == "ko":
                player2[RIGHT] = True
                player2[SPRITE] = kenmoves[KO][int(round(p2frames[NUM],0))]
            elif player2[RIGHT] == False and p2frames[ANI] == "ko":
                player2[RIGHT] = False
                player2[SPRITE] = transform.flip(kenmoves[KO][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

    if player2[CHAR] == "ken" and player2[ALIVE] == False:
        
        if player2[RIGHT] == False:
            player2[SPRITE] = transform.flip(kenmoves[KO][4],1,0)
        if player2[RIGHT] == True:
            player2[SPRITE] = kenmoves[KO][4]

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2hitbox[Y] = 670 - kenmoves[KO][4].get_size()[1]


    if player2[ALIVE] == False and player1[CHAR] == "ken":
        
        p1frames[ANI] = "win"
        p1frames[NUM] += 0.1
        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True

        if round(p1frames[NUM],0) >= 2:
            p1frames[NUM] = 2
            score[0] += 1

        player1[RIGHT] = True
        player1[SPRITE] = kenmoves[WIN][int(round(p1frames[NUM],0))]

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

#============================


    if player2[CHAR] == "bison" and player2[ALIVE] == True:
        if player2[HP] <= 0 or p2frames[ANI] == "ko":

            p2frames[ANI] = "ko"
            p2frames[NUM] += 0.1
            player2[ISATT] = True
            player2[CANATT] = False
            player2[MOVING] = True
            p2hitbox[Y] = 670 - bisonmoves[KO][0].get_size()[1]

            if round(p2frames[NUM],0) >= 4:
                p2frames[NUM] = 3
                player2[MOVING] = False
                player2[ISATT] = False
                player2[ALIVE] = False

            if player2[RIGHT] == True and p2frames[ANI] == "ko":
                player2[RIGHT] = True
                player2[SPRITE] = bisonmoves[KO][int(round(p2frames[NUM],0))]
            elif player2[RIGHT] == False and p2frames[ANI] == "ko":
                player2[RIGHT] = False
                player2[SPRITE] = transform.flip(bisonmoves[KO][int(round(p2frames[NUM],0))],1,0)

            p2hitbox[WID],p2hitbox[HEI] = player2[SPRITE].get_size()[0],player2[SPRITE].get_size()[1]

    if player2[CHAR] == "bison" and player2[ALIVE] == False:
        
        if player2[RIGHT] == False:
            player2[SPRITE] = transform.flip(bisonmoves[KO][3],1,0)
        if player2[RIGHT] == True:
            player2[SPRITE] = bisonmoves[KO][3]

        player2[ISATT] = True
        player2[CANATT] = False
        player2[MOVING] = True
        p2hitbox[Y] = 670 - bisonmoves[KO][3].get_size()[1]


    if player2[ALIVE] == False and player1[CHAR] == "bison":
        
        p1frames[ANI] = "win"
        p1frames[NUM] += 0.1
        player1[ISATT] = True
        player1[CANATT] = False
        player1[MOVING] = True

        if round(p1frames[NUM],0) >= 3:
            p1frames[NUM] = 3
            score[0] += 1

        player1[RIGHT] = True
        player1[SPRITE] = bisonmoves[WIN][int(round(p1frames[NUM],0))]

        p1hitbox[WID],p1hitbox[HEI] = player1[SPRITE].get_size()[0],player1[SPRITE].get_size()[1]

#============================


def border():
    if p1hit.colliderect(outright):
        p1hitbox[X] = 0
    if p2hit.colliderect(outright):
        p2hitbox[X] = 0
    if p1hit.colliderect(outleft):
        p1hitbox[X] = 1024 - player1[SPRITE].get_size()[0]
    if p2hit.colliderect(outleft):
        p2hitbox[X] = 1024 - player2[SPRITE].get_size()[0]
        
        
def yval():
    if player1[ONGROUND] == True and player1[CHAR] != "bison":
        p1hitbox[Y] = 670 - player1[SPRITE].get_size()[1]
    if player2[ONGROUND] == True and player2[CHAR] != "bison":
        p2hitbox[Y] = 670 - player2[SPRITE].get_size()[1]
    
















#========================================


player1[CHAR] = "ken"
player2[CHAR] = "bison"



ground = Rect(0,670,1024,168)

myClock = time.Clock()
screen = display.set_mode((1024,720))

loadimages()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
            
    keys = key.get_pressed()

    #if oldscore != score and score[0] != 2 and score[1] != 2:
        
    
    jumpp1()
    jumpp2()

    movep1()
    p1hit = Rect(p1hitbox)
    movep2()
    p2hit = Rect(p2hitbox)

    gravity()
        
    chargeAttp1()
    chargeAttp2()

    hadoukenp1()
    hadoukenp2()

    attp1()
    attp2()
        
    idlep1()
    idlep2()

    p2hitp1()
    p1hitp2()

    kop1()
    kop2()

    wait()

    border()
    yval()
        
    drawScene()























    oldscore = score

    
    myClock.tick(60)
    display.flip()
quit()
