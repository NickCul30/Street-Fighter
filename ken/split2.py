from pygame import *
import sys, os, glob

os.environ['SDL_VIDEO_WINDOW_POS'] = '10,30'

init()
fname = glob.glob("*.png")[0]
#fname = "naruto.png"
pic = image.load(fname)   

wid,hi = pic.get_size()
back = Surface((wid+2,hi+2),SRCALPHA)
back.fill((pic.get_at((0,0))))
back.blit(pic,(1,1))
bgCol = back.get_at((0,0))
screen = display.set_mode((wid+2,hi+2))
screen.blit(pic,(1,1))
display.flip()

''' -------------------------------------------------------------
    getName
    -------------------------------------------------------------
    Because pygame likes to crash you can copy and paste my getName
    function into your program and use it, free of charge.  You
    may want to change the size of the rectange, it's location, the
    font, and the colour so that it matches your program.
    ------------------------------------------------------------- '''
def getName():
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(5,5,200,25) # make changes here.
    
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    typing = False
                    ans = ""
                elif e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            #
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans

def lineHasPixel(y,area):
    for x in range(area[0],area[2]+1):
        if back.get_at((x,y))!=bgCol:
            return True
    return False

def findPixelLine(y,area):
    while y<area[3] and not lineHasPixel(y,area):
        y+=1
    return y

def findOpenLine(y,area):
    while y<area[3] and lineHasPixel(y,area):
        y+=1
    return y

def colHasPixel(top,bott,x):
    for y in range(top,bott+1):
        if back.get_at((x,y))!=bgCol:
            return True
    return False

def findPixelCol(top,bott,x):
    while x<wid and not colHasPixel(top,bott,x):
        x+=1
    return x

def findOpenCol(top,bott,x):
    while x<wid and colHasPixel(top,bott,x):
        x+=1
    return x

def showMove(pics):
    running = True
    #cop = screen.copy()
    width = max([p.get_width() for p in pics])
    height = max([p.get_height() for p in pics])
    rects = []
    anchors = []
    yy = height
    frame = 0
    screen.fill(bgCol)
    for i in range(len(pics)):
        rects.append(Rect(i*width,height*2,width,height))
        anchors.append((width//2,height//2))
        
    while running:
        for evnt in event.get():               
            if evnt.type == QUIT or evnt.type == KEYDOWN:
                running = False

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        if mb[0]==1:
            for i,r in enumerate(rects):
                if r.collidepoint(mpos):
                    anchors[i] = (mpos[0]-r.left,mpos[1]-height*2)
        frame+=1
        draw.rect(screen,bgCol,(0,0,screen.get_width(),height*2))

        maxax = max([a[0] for a in anchors])
        maxay = max([a[1] for a in anchors])

        f = frame//10%len(pics)
        screen.blit(pics[f],((maxax-anchors[f][0])%screen.get_width(),maxay-anchors[f][1]))

        for i,pic in enumerate(pics):
            screen.blit(pics[i],(i*width,height*2))
            
        for i,a in enumerate(anchors):
            draw.circle(screen,(0,0,0),(i*width+a[0],height*2+a[1]),4)
            draw.circle(screen,(255,0,0),(i*width+a[0],height*2+a[1]),3)
        
        time.wait(20)
        display.flip()
    return anchors
    #screen.blit(cop,(0,0))

def getMove(area):
    cnt=0
    pics = []
    
    top = findPixelLine(area[1],area)
    bott = findOpenLine(top,area)
    right = area[0]
    while right<area[2]:
        left = findPixelCol(top,bott,right)
        if left >= area[2]:break
        right = findOpenCol(top,bott,left)
        if right-left>5:
            pics.append(back.subsurface((left,top,right-left+1,bott-top+1)))

        draw.rect(screen,(255,0,0), (left,top-offy,right-left+1,bott-top+1),1)
        display.flip()
    if len(pics)==0:return
    anchors=showMove(pics)
    maxax = max([a[0] for a in anchors])
    maxay = max([a[1] for a in anchors])

    name = getName()
    if name == "":
        return
    else:
        if name not in os.listdir("."):
            os.mkdir(name)
        for i,pic in enumerate(pics):
            extrax = maxax-anchors[i][0]
            extray = maxay-anchors[i][1]
            tmp = Surface((pic.get_width()+extrax,pic.get_height()+extray),SRCALPHA)
            tmp.fill((0,0,0,0))
            pic = pic.convert()
            pic.set_colorkey((bgCol))
            tmp.blit(pic,(extrax,extray))
            image.save(tmp,name+"/"+name+str(i)+".png")
            
running = True

cop = screen.copy()
stx,sty = 0,0
offx,offy = 0,0
while running:
    for evnt in event.get():               
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN and evnt.button==4 and offy>0:
            offy -= 10
        if evnt.type == MOUSEBUTTONDOWN and evnt.button==5:
            offy += 10
        if evnt.type == MOUSEBUTTONDOWN and evnt.button==1:
            stx,sty = evnt.pos
            
            #cop = screen.copy()
        if evnt.type == MOUSEBUTTONUP and evnt.button==1:
            ex,ey = evnt.pos
            ex = max(1,ex)
            ex = min(back.get_width()-2,ex)
            ey = max(1,ey)
            ey = min(back.get_height()-2,ey)
            getMove([min(stx,ex),min(sty+offy,ey+offy),max(ex,stx),max(sty+offy,ey+offy)])
            #screen.blit(cop,(0,0))
            
    mx,my = mouse.get_pos()

    keys = key.get_pressed()
    if keys[K_DOWN]:
        offy += 10
    if keys[K_UP] and offy>0:
        offy -= 10

    screen.fill((255,0,255))
    screen.blit(back,(0,-offy))
        
    if mouse.get_pressed()[0]==1:
        draw.rect(screen, (0,255,0), (stx,sty, mx-stx+1,my-sty+1),1)
      
    display.flip()
    
     
quit()
