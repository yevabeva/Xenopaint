#Eva Yeverovich
#Xenopaint
#NOTE THAT IF SOME ITEMS ARE IN STRANGE POSITIONS (LIKE THE MUSIC), IT WASN'T WORKING ELSEWHERE SO I PLACED IT IN THE CODE WHERE IT WAS ABLE TO WORK FOR ME
#ALSO NOTE THAT IF IT SAYS STARTX OR STARTY ISN'T WORKING, THAT'S NOT ACTUALLY THE CASE AND ALL YOU HAVE TO DO IS RETRY TO OPEN IT AND IT'LL WORK
from pygame import *
from math import *
from random import *
from tkinter import * 
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
root = Tk() 
root.withdraw()
import os
screen = display.set_mode((1024,576))
undolist=[]
redolist=[]
tool = "pencil" #every paint program has pencil as its default tool
color = (0,0,0)
size = 1           #just setting some default sizes 
brushsize = 1
erythstamps = False #these are for the stamps
colony = True       #so that they don't mix up with each other
noponn = False
opened = False #tells the program if a file has been opened or not
soundon = True #checks if music is on or not
init() 
mixer.music.load("In-Game Music/XenobladeTitleTheme.mp3")
mixer.music.play()
#------------------------BUTTONS AND STUFF--------------------------
pic = image.load("Backgrounds/shulkbackground.jpg")
titlepic = image.load("Backgrounds/xenobladetitlescreen.jpg")
titlepic1 = image.load("Backgrounds/xenobladetitlescreen1.jpg")
titlepic2 = image.load("Backgrounds/xenobladetitlescreen2.jpg")
titlehoverbutton = image.load("Buttons/firstbuttoncopy.gif")
continuebutton = image.load("Buttons/continuebutton.png")
loading = image.load("Backgrounds/loadingscreen.jpg")
erythbutton = image.load("Buttons/erythbutton.jpg")
noponbutton = image.load("Buttons/noponbutton.jpg")
colonybutton = image.load("Buttons/colonybutton.jpg")
soundbutton = image.load("Buttons/soundon.jpg")
soundoffbutton = image.load("Buttons/soundoff.jpg")
eryth = image.load("Backgrounds/erythsea.jpg")
palette = image.load("Buttons/colorpalette.jpg")
pixelsize = image.load("Buttons/pixelsize_300.jpg")
noponvillage = image.load("Backgrounds/noponvillage.jpg")
homsstamps = image.load("Buttons/homsstamps.png")
entiastamps = image.load("Buttons/entiastamps.png")
noponstamps = image.load("Buttons/noponstamps.png")

redo = image.load("Buttons/redo.jpg")
redohighlight = image.load("Buttons/redohighlight.jpg")

undo = image.load("Buttons/undo.jpg")
undohighlight = image.load("Buttons/undohighlight.jpg")

save = image.load("Buttons/save.jpg")
savehighlight = image.load("Buttons/savehighlight.jpg")

pencil = image.load("Buttons/pencil.jpg")
pencilhighlight = image.load("Buttons/pencilhighlight.jpg")
selected_pencil = image.load("Buttons/selected_pencil.jpg")
pencilinfo = image.load("Buttons/info_pencil.jpg")

eraser = image.load("Buttons/eraser.jpg")
eraserhighlight = image.load("Buttons/eraserhighlight.jpg")
selected_eraser = image.load("Buttons/selected_eraser.jpg")
eraserinfo = image.load("Buttons/info_eraser.jpg")

paintbrush = image.load("Buttons/paintbrush.jpg")
paintbrushhighlight = image.load("Buttons/paintbrushhighlight.jpg")
selected_paintbrush = image.load("Buttons/selected_paintbrush.jpg")
paintbrushinfo = image.load("Buttons/info_paintbrush.jpg")

ellipse = image.load("Buttons/ellipse.jpg")
ellipsehighlight = image.load("Buttons/ellipsehighlight.jpg")
selected_ellipse = image.load("Buttons/selected_ellipse.jpg")
ellipseinfo = image.load("Buttons/info_ellipse.jpg")

filledEllipse = image.load("Buttons/ellipse_filled.jpg")
filled_ellipsehighlight = image.load("Buttons/ellipsehighlight_filled.jpg")
selected_filledellipse = image.load("Buttons/selected_filledellipse.jpg")
filledEllipseinfo = image.load("Buttons/info_filledellipse.jpg")

rectangle = image.load("Buttons/rect.jpg")
rectanglehighlight = image.load("Buttons/recthighlight.jpg")
selected_rectangle = image.load("Buttons/selected_rect.jpg")
rectangleinfo = image.load("Buttons/info_rectangle.jpg")

filledRectangle = image.load("Buttons/filledRect.jpg")
filled_rectanglehighlight = image.load("Buttons/recthighlight_filled.jpg")
selected_filledrectangle = image.load("Buttons/selected_filledRect.jpg")
filledRectangleinfo = image.load("Buttons/info_filledrectangle.jpg")

line = image.load("Buttons/line.jpg")
linehighlight = image.load("Buttons/linehighlight.jpg")
selected_line = image.load("Buttons/selected_line.jpg")
lineinfo = image.load("Buttons/info_line.jpg")

spraycan = image.load("Buttons/spraycan.jpg")
spraycanhighlight = image.load("Buttons/spraycanhighlight.jpg")
selected_spraycan = image.load("Buttons/selected_spraycan.jpg")
spraycaninfo = image.load("Buttons/info_spraycan.jpg")
#----------------------------------------------------------------------------

#-------------------------------CHARACTER STAMPS-----------------------------
Reyn = image.load("Character Stamps/Homs/reyn.png")
info_reyn = image.load("Character Stamps/Homs/info_reyn.jpg")
Shulk = image.load("Character Stamps/Homs/shulk.png")
info_shulk = image.load("Character Stamps/Homs/info_shulk.jpg")
Fiora = image.load("Character Stamps/Homs/Fiora.png")
info_fiora = image.load("Character Stamps/Homs/info_fiora.jpg")
Dunban = image.load("Character Stamps/Homs/dunban.png")
info_dunban = image.load("Character Stamps/Homs/info_dunban.jpg")
Sharla = image.load("Character Stamps/Homs/sharla.png")
info_sharla = image.load("Character Stamps/Homs/info_sharla.jpg")
Monado = image.load("Character Stamps/Homs/monado.png")
info_monado = image.load("Character Stamps/Homs/info_monado.jpg")

Alvis = image.load("Character Stamps/High Entia/Alvis.png")
info_alvis = image.load("Character Stamps/High Entia/info_alvis.jpg")
Kallian = image.load("Character Stamps/High Entia/kallian.png")
info_kallian = image.load("Character Stamps/High Entia/info_kallian.jpg")
Lorithia = image.load("Character Stamps/High Entia/Lorithia.png")
info_lorithia = image.load("Character Stamps/High Entia/info_lorithia.jpg")
Melia = image.load("Character Stamps/High Entia/melia2.png")
info_melia = image.load("Character Stamps/High Entia/info_melia.jpg")
Melia_2 = image.load("Character Stamps/High Entia/melia.png")
info_melia = image.load("Character Stamps/High Entia/info_melia.jpg")
Sorean = image.load("Character Stamps/High Entia/Sorean.png")
info_sorean = image.load("Character Stamps/High Entia/info_sorean.jpg")

chiefdunga = image.load("Character Stamps/Nopon/chiefdunga.png")
info_dunga = image.load("Character Stamps/Nopon/info_dunga.jpg")
nopon1 = image.load("Character Stamps/Nopon/nopon1.png")
info_nopon1 = image.load("Character Stamps/Nopon/info_nopon1.jpg")
nopon2 = image.load("Character Stamps/Nopon/nopon2.png")
info_nopon2 = image.load("Character Stamps/Nopon/info_nopon2.jpg")
riki = image.load("Character Stamps/Nopon/riki.png")
info_riki = image.load("Character Stamps/Nopon/info_riki.jpg")
riki2 = image.load("Character Stamps/Nopon/riki2.png")
info_riki = image.load("Character Stamps/Nopon/info_riki.jpg")

mechon = image.load("Character Stamps/Mechon.png")
mechonattack = image.load("Buttons/mechonattack.png")

screen.blit(titlepic1,(0,0))
startgame = Rect(458,388,111,20)
continuegame = Rect(465,418,111,20)
running = True
mx,my=0,0
sx,sy = 0,0 #to make sure it recognizes it

#INTRO
while True:
    event.pump()
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    if continuegame.collidepoint((mx,my)):
        screen.blit(titlepic2,(0,0))
        screen.blit(continuebutton,(465,418))                    
    else:
        screen.blit(titlepic1,(0,0))
        if startgame.collidepoint((mx,my)):
            screen.blit(titlepic,(0,0))
            screen.blit(titlehoverbutton,(456,385))
        else:
            screen.blit(titlepic1,(0,0))
    if mb[0]==1 and startgame.collidepoint((mx,my)):
        screen = display.set_mode((1280,750))
        screen.blit(pic,(0,0))
        break
    if mb[0]==1 and continuegame.collidepoint((mx,my)):           #the continue option in the starting screen is where people can load a previous "safe file" or image
        opened = True
        openfileName = askopenfilename(parent=root,title="Open a Creation:")
        openpic = image.load(openfileName)
        screen = display.set_mode((1280,750))
        screen.blit(pic,(0,0))
        break
    display.flip()
mixer.music.stop()  #to switch to the new music, turn the old one off 
running = True
#SETTING TOOLS
subsurface = screen.subsurface(0,0,1280,750)
canvas = draw.rect(screen,(255,255,255),(10,10,900,550))
screen.set_clip(canvas)
if opened == True:               #if someone opened a picture using continue
    screen.blit(openpic,(10,10)) #start with that instead of the white canvas
screen.set_clip(None)            #makes sure the image doesnt go beyond the canvas
subcanvas = screen.subsurface(10,10,900,550)
loading = transform.scale(loading,(1280,750))
eryth = transform.scale(eryth,(1280,750))
mechon = transform.scale(mechon,(60,60))
#RECT SETTER
pencilRect = Rect(10,570,60,60)
eraseRect = Rect(80,570,60,60)
paintbrushRect = Rect(150,570,60,60)
rectangleRect = Rect(220,570,60,60)
filledRectangleRect = Rect(290,570,60,60)
ellipseRect = Rect(10,640,60,60)
filledEllipseRect = Rect(80,640,60,60)
lineRect = Rect(150,640,60,60)
spraycanRect = Rect(220,640,60,60)
redoRect = Rect(290,640,60,60)
undoRect = Rect(360,640,60,60)
saveRect = Rect(430,640,60,60)
paletteRect = Rect(652,572,262,142)
mechonRect = Rect(500,640,60,60)
soundonRect = Rect(920,400,30,30)
soundoffRect = Rect(920,440,30,30)
#--pixel sizes---
onepx = Rect(369,597,9,9)
threepx = Rect(384,593,17,17)
fivepx = Rect(409,590,22,22)
sevenpx = Rect(438,586,30,30)
ninepx = Rect(475,584,36,36)
elevenpx = Rect(521,582,40,40)
#----location----
erythRect = Rect(920,572,110,70)
noponRect =Rect(1040,572,110,70)
colonyRect = Rect(1160,572,110,70)
#----stamps----
reynRect = Rect(930,76,99,97)
shulkRect = Rect(930,190,99,97)
fioraRect = Rect(1050,76,99,97)
sharlaRect = Rect(1157,76,99,97)
dunbanRect = Rect(1165,190,99,97)
monadoRect = Rect(1040,175,125,110)
alvisRect = Rect(930,79,99,97)
kallianRect = Rect(1042,80,99,97)
meliaRect1 = Rect(1155,80,99,97)
soreanRect = Rect(929,191,99,97)
lorithiaRect = Rect(1040,193,99,97)
meliaRect2 = Rect(1160,192,99,97)
elderRect = Rect(930,76,99,97)
bluenoponRect = Rect(1157,76,99,97)
greennoponRect = Rect(1160,192,99,97)
rikiRect1 = Rect(1042,140,105,97)
rikiRect2 = Rect(929,191,99,97)
def drawLayout():
    #IMAGE BLITTING
    screen.blit(pencil,(10,570))
    screen.blit(eraser,(80,570))
    screen.blit(paintbrush,(150,570))
    screen.blit(palette,(650,570))
    screen.blit(ellipse,(10,640))
    screen.blit(filledEllipse,(80,640))
    screen.blit(rectangle,(220,570))
    screen.blit(filledRectangle,(290,570))         #I used functions to blit the tools and stamp images
    screen.blit(line,(150,640))                    #when changing backgrounds, allows for avoiding re-blit issues
    screen.blit(pixelsize,(360,570))
    screen.blit(redo,(290,640))
    screen.blit(undo,(360,640))
    screen.blit(save,(430,640))
    draw.rect(screen,(0,0,0),(500,640,60,60))
    screen.blit(mechon,(500,640))
    screen.blit(erythbutton,(920,572))
    screen.blit(noponbutton,(1040,572))
    screen.blit(colonybutton,(1160,572))
    screen.blit(soundbutton,(920,400))
    screen.blit(soundoffbutton,(920,440))

drawLayout()

def homs():
    screen.blit(homsstamps,(920,10))
homs()
def highentia():
    screen.blit(entiastamps,(920,10))
def nopon():
    screen.blit(noponstamps,(920,10))
while running:
    if mixer.music.get_busy() == False:   #if there is no music playing, then play the new music
        if soundon == True:
            if colony == True:
                mixer.music.load("In-Game Music/Hometownmusic.mp3")
                mixer.music.play()
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN and canvas.collidepoint((mx,my)):
            copy = screen.subsurface(canvas).copy()
            undolist.append(copy)
            sx,sy = e.pos
        if e.type == MOUSEBUTTONUP:
            if undoRect.collidepoint((mx,my)) and mb[0]==1:
                if len(undolist) > 1:#it blits the last thing that was undone and then appends what just happened to the redo list
                    screen.blit(undolist[-1],(10,10))
                    redolist.append(undolist.pop())
                else:
                    pass
            if redoRect.collidepoint((mx,my)) and mb[0]==1:
                if len(redolist) > 0:                               #vice versa, it blits the last thing that was redone, and appens that to the undo list
                    screen.blit(redolist[-1],(10,10))
                    undolist.append(redolist.pop())
                else:
                    pass
    #PICKING COLOR FOR EVERYTHING#
    if paletteRect.collidepoint((mx,my)) and mb[0]==1:
        color = screen.get_at((mx,my))
    colorViewer = draw.rect(screen,(color),(580,570,60,60))
#----
    if soundonRect.collidepoint((mx,my)) and mb[0]==1:
        soundon = True
        if mixer.music.get_busy() == True: #if there's already music playing, skip this
            pass
        else:
            mixer.music.play()
    if soundoffRect.collidepoint((mx,my)) and mb[0]==1:
        soundon = False
        if mixer.music.get_busy() == True:
            mixer.music.pause()
        else:
            pass
#----             HIGHLIGHT COLLIDEPOINT CHECKING
    if pencilRect.collidepoint((mx,my)):
        if tool!="pencil":
            screen.blit(pencilhighlight,(10,570))
        else:                                                #to sum up one of these (out of many)
            pass                                             #if your tool isn't already pencil, it highlights it
    else:                                                    #clicking changes to a darker highlight to show 'selected'
        screen.blit(pencil,(10,570))
    if pencilRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "pencil"
            screen.blit(selected_pencil,(10,570))            #if the tool is pencil, print the information about it and highlight it as you work with it
    if tool=="pencil":                                       #this is the same for all the other tools. 
         screen.blit(selected_pencil,(10,570))
         screen.blit(pencilinfo,(920,650))
#----
    if eraseRect.collidepoint((mx,my)):
        if tool!="eraser":
            screen.blit(eraserhighlight,(80,570))
        else:
            pass
    else:
        screen.blit(eraser,(80,570))
    if eraseRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "eraser"
            screen.blit(selected_eraser,(80,570))
    if tool=="eraser":
         screen.blit(selected_eraser,(80,570))
         screen.blit(eraserinfo,(920,650))
#----
    if paintbrushRect.collidepoint((mx,my)):
        if tool!="paintbrush":
            screen.blit(paintbrushhighlight,(150,570))
        else:
            pass
    else:
        screen.blit(paintbrush,(150,570))
    if paintbrushRect.collidepoint((mx,my)) and mb[0]==1:
        tool = "paintbrush"
        screen.blit(selected_paintbrush,(150,570))
    if tool=="paintbrush":
        screen.blit(selected_paintbrush,(150,570))
        screen.blit(paintbrushinfo,(920,650))
#----
    if spraycanRect.collidepoint((mx,my)):
        if tool!="spraycan":
            screen.blit(spraycanhighlight,(220,640))
        else:
            pass
    else:
        screen.blit(spraycan,(220,640))
    if spraycanRect.collidepoint((mx,my)) and mb[0]==1:
        tool = "spraycan"
        screen.blit(selected_spraycan,(220,640))
    if tool=="spraycan":
        screen.blit(selected_spraycan,(220,640))
        screen.blit(spraycaninfo,(920,650))
#----
    if ellipseRect.collidepoint((mx,my)):
        if tool!="ellipse":
            screen.blit(ellipsehighlight,(10,640))
        else:
            pass
    else:
        screen.blit(ellipse,(10,640))
    if ellipseRect.collidepoint((mx,my)) and mb[0]==1:
        tool = "ellipse"
        screen.blit(selected_ellipse,(10,640))
    if tool=="ellipse":
        screen.blit(selected_ellipse,(10,640))
        screen.blit(ellipseinfo,(920,650))
#----
    if filledEllipseRect.collidepoint((mx,my)):
        if tool!="filled ellipse":
            screen.blit(filled_ellipsehighlight,(80,640))
        else:
            pass
    else:
        screen.blit(filledEllipse,(80,640))
    if filledEllipseRect.collidepoint((mx,my)) and mb[0]==1:
        tool = "filled ellipse"
        screen.blit(selected_filledellipse,(80,640))
    if tool == "filled ellipse":
        screen.blit(selected_filledellipse,(80,640))
        screen.blit(filledEllipseinfo,(920,650))
#----
    if rectangleRect.collidepoint((mx,my)):
        if tool!="rectangle":
            screen.blit(rectanglehighlight,(220,570))
        else:
            pass
    else:
        screen.blit(rectangle,(220,570))
    if rectangleRect.collidepoint((mx,my)) and mb[0]==1:
        tool = "rectangle"
        screen.blit(selected_rectangle,(220,570))
    if tool == "rectangle":
        screen.blit(selected_rectangle,(220,570))
        screen.blit(rectangleinfo,(920,650))
#----
    if filledRectangleRect.collidepoint((mx,my)):
        if tool!="filled rectangle":
            screen.blit(filled_rectanglehighlight,(290,570))
        else:
            pass
    else:
        screen.blit(filledRectangle,(290,570))
    if filledRectangleRect.collidepoint((mx,my)) and mb[0]==1:
        tool = "filled rectangle"
        screen.blit(selected_filledrectangle,(290,570))
    if tool == "filled rectangle":
        screen.blit(selected_filledrectangle,(290,570))
        screen.blit(filledRectangleinfo,(920,650))
#----
    if redoRect.collidepoint((mx,my)):
        if tool!="redo":
            screen.blit(redohighlight,(290,640))
        else:
            pass
    else:
        screen.blit(redo,(290,640))
    if redoRect.collidepoint((mx,my)) and mb[0]==1:
        tool = "redo"
#----
    if undoRect.collidepoint((mx,my)):
            screen.blit(undohighlight,(360,640))
    else:
        screen.blit(undo,(360,640))

#----
    alreadysaved = False  # so that it closes upon demand
    if saveRect.collidepoint((mx,my)):
        if tool!="save":
            screen.blit(savehighlight,(430,640))
        else:
            pass
    else:
        screen.blit(save,(430,640))
    if saveRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "save"
    if tool == "save":
        fileName = asksaveasfilename(parent=root,title="Be sure to save as .jpg , .png or any kind of image file.")
        if len(fileName)>0:
            image.save((copy),fileName)
            alreadysaved = True
        if alreadysaved:
            tool = "pencil"
#----
    if lineRect.collidepoint((mx,my)):
        if tool!="line":
            screen.blit(linehighlight,(150,640))
        else:
            pass
    else:
        screen.blit(line,(150,640))
    if lineRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "line"
            screen.blit(selected_line,(150,640))
    if tool=="line":
         screen.blit(selected_line,(150,640))
         screen.blit(lineinfo,(920,650))
#----
    if onepx.collidepoint((mx,my))and mb[0]==1:
        size = 1
        brushsize = 3
    if threepx.collidepoint((mx,my))and mb[0]==1:
        size = 3
        brushsize = 5
    if fivepx.collidepoint((mx,my))and mb[0]==1:      #brushsize to make things like eraser and paintbrush a little bigger and more comfortable
        size = 5
        brushsize = 7
    if sevenpx.collidepoint((mx,my))and mb[0]==1:
        size = 7
        brushsize = 9
    if ninepx.collidepoint((mx,my))and mb[0]==1:
        size = 9
        brushsize = 11
    if elevenpx.collidepoint((mx,my))and mb[0]==1:
        size = 11
        brushsize = 13
#----
    if colonyRect.collidepoint((mx,my)) and mb[0]==1:
        if soundon == True:                                         #there are three of these blocks of code but to sum it up,
            if colony == True:
                mixer.music.load("In-Game Music/Hometownmusic.mp3")  #play music specific to that area
                mixer.music.play()
        colony = True
        erythstamps = False  #all the other stamps and things specific to one place are false
        noponn = False
        tool = "pencil"      #you start back off with pencil
        canCopy = subcanvas.copy()
        subsurface.blit(loading,(0,0))  #loading screen
        display.flip()
        time.wait(900)
        subsurface.blit(pic,(0,0))
        subcanvas.blit(canCopy,(0,0))   #blit the last thing you had done on the canvas onto the new canvas
        drawLayout()                   #redraw all the tools and stamps
        homs()
#----
    if erythRect.collidepoint((mx,my)) and mb[0]==1:
        if soundon == True:
            if erythstamps == True:
                mixer.music.load("In-Game Music/ErythSeaMusic.mp3")
                mixer.music.play()
        erythstamps = True
        colony = False
        noponn = False
        tool = "pencil"
        canCopy = subcanvas.copy()
        subsurface.blit(loading,(0,0))
        display.flip()
        time.wait(900)
        subsurface.blit(eryth,(0,0))
        subcanvas.blit(canCopy,(0,0))
        drawLayout()
        highentia()

    if colony == True:
        erythstamps = False
        noponn = False           #this is just saying that when one is true, the other two are false
    if erythstamps == True:
        colony = False
        noponn = False
    if noponn == True:
        erythstamps = False
        colony = False
#----
    if noponRect.collidepoint((mx,my)) and mb[0]==1:
        if soundon == True:
            if noponn == True:
                mixer.music.load("In-Game Music/FrontierVillageMusic.mp3")
                mixer.music.play()
        noponn = True
        erythstamps = False
        colony = False
        tool = "pencil"
        canCopy = subcanvas.copy()
        subsurface.blit(loading,(0,0))
        display.flip()
        time.wait(900)
        subsurface.blit(noponvillage,(0,0))
        subcanvas.blit(canCopy,(0,0))
        drawLayout()
        nopon()
#----
    if mechonRect.collidepoint((mx,my)) and mb[0]==1:
            screen.blit(mechonattack,(10,10))
            display.flip()
            time.wait(900)                              #my clear all button (an "attack" by the enemy)
            subcanvas.fill((255,255,255))
#-----------------STAMP SETTING------------------
    if colony == True:
        if reynRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "reyn"
            screen.blit(info_reyn,(920,650))
        if shulkRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "shulk"
            screen.blit(info_shulk,(920,650))
        if fioraRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "fiora"
            screen.blit(info_fiora,(920,650))
        if sharlaRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "sharla"
            screen.blit(info_sharla,(920,650))
        if dunbanRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "dunban"
            screen.blit(info_dunban,(920,650))
        if monadoRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "monado"
            screen.blit(info_monado,(920,650))
    if erythstamps == True:
        if alvisRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "alvis"
            screen.blit(info_alvis,(920,650))
        if kallianRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "kallian"
            screen.blit(info_kallian,(920,650))
        if meliaRect1.collidepoint((mx,my)) and mb[0]==1:
            tool = "melia1"
            screen.blit(info_melia,(920,650))
        if soreanRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "sorean"
            screen.blit(info_sorean,(920,650))
        if lorithiaRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "lorithia"
            screen.blit(info_lorithia,(920,650))
        if meliaRect2.collidepoint((mx,my)) and mb[0]==1:
            tool = "melia2"
            screen.blit(info_melia,(920,650))
    if noponn == True:
        if elderRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "chiefdunga"
            screen.blit(info_dunga,(920,650))
        if bluenoponRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "nopon2"
            screen.blit(info_nopon2,(920,650))
        if greennoponRect.collidepoint((mx,my)) and mb[0]==1:
            tool = "nopon1"
            screen.blit(info_nopon1,(920,650))
        if rikiRect1.collidepoint((mx,my)) and mb[0]==1:    #i got these two mixed up so i just switched around the "tool =" part
            tool = "riki2"
            screen.blit(info_riki,(920,650))
        if rikiRect2.collidepoint((mx,my)) and mb[0]==1:
            tool = "riki"
            screen.blit(info_riki,(920,650))
#-------------------------------------------------
    omx,omy = mx,my
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    #sx-mx and sy-my is just getting the legth for the ellipse as well as the rectangle (since ellipse fills the space of a rect)
    rectthing = Rect(sx,sy,mx-sx,my-sy)
    rectthing.normalize()
    if mb[0]==1 and canvas.collidepoint((mx,my)):
        screen.set_clip(canvas) #sets you only able to use tools within the canvas itself
#----------------ACTUAL TOOLS---------------------
        if tool == "pencil" and mb[0]==1:
            draw.line(screen,(color),(omx,omy),(mx,my),size)
        elif tool == "eraser":
            dist = hypot(omx-mx,omy-my)
            for i in range(int(dist)):         #same as the paintbrush, fills in the gaps left by the circles
                x = int(mx+i/dist*(omx-mx))
                y = int(my+i/dist*(omy-my))
                draw.circle(screen,(255,255,255),(x,y),brushsize)
        elif tool == "paintbrush":
            dist = hypot(omx-mx,omy-my)        #finds distance between old mx and the current mx
            for i in range(int(dist)):         #this fills in the gaps between the circles so that the paintbrush is consistent
                x = int(mx+i/dist*(omx-mx))    #the distances is added onto the mx and my to get coordinates between the circles
                y = int(my+i/dist*(omy-my))
                draw.circle(screen,(color),(x,y),brushsize)
        elif tool == "spraycan":
            dist = hypot(omx-mx,omy-my)
            for i in range(20):
                    dotx=mx-randint(-20,20)
                    doty=my-randint(-20,20)                    #for spraypaint, dotx and doty are the position of the random dots
                    dist=int(sqrt((mx-dotx)**2 +(my-doty)**2)) 
                    if dist<20:                                #if the distance is within the specified radius around the circle
                        draw.line(screen,(color),(dotx,doty),(dotx,doty),1)
        elif tool == "line":
            screen.blit(copy,(10,10))
            draw.line(screen,(color),(sx,sy),(mx,my),size)  #sx and sy are the starting point 
        elif tool == "ellipse":
            screen.blit(copy,(10,10))
            if min(abs(sx-mx),abs(sy-my))<size*2:           #the ellipse cannot exceed the size of its rect 
                draw.ellipse(screen,(color),(rectthing))
            else:
                draw.ellipse(screen,(color),(rectthing),size)
        elif tool == "filled ellipse":
            screen.blit(copy,(10,10))
            draw.ellipse(screen,(color),(rectthing))
        elif tool == "rectangle":
            screen.blit(copy,(10,10))
            draw.rect(screen,(color),(rectthing),size)
        elif tool == "filled rectangle":
            screen.blit(copy,(10,10))
            draw.rect(screen,(color),(rectthing))

        #stamps
        elif tool == "reyn":
            screen.blit(copy,canvas)
            subcanvas.blit(Reyn,(mx-130,my-200))
        elif tool == "shulk":
            screen.blit(copy,canvas)
            subcanvas.blit(Shulk,(mx-130,my-200))
        elif tool == "fiora":
            screen.blit(copy,canvas)
            subcanvas.blit(Fiora,(mx-150,my-200))
        elif tool == "sharla":
            screen.blit(copy,canvas)
            subcanvas.blit(Sharla,(mx-90,my-200))
        elif tool == "dunban":
            screen.blit(copy,canvas)
            subcanvas.blit(Dunban,(mx-130,my-200))
        elif tool == "monado":
            screen.blit(copy,canvas)
            subcanvas.blit(Monado,(mx-250,my-50))
        elif tool == "alvis":
            screen.blit(copy,canvas)
            subcanvas.blit(Alvis,(mx-90,my-200))
        elif tool == "kallian":
            screen.blit(copy,canvas)
            subcanvas.blit(Kallian,(mx-150,my-200))
        elif tool == "melia1":
            screen.blit(copy,canvas)
            subcanvas.blit(Melia,(mx-100,my-200))
        elif tool == "sorean":
            screen.blit(copy,canvas)
            subcanvas.blit(Sorean,(mx-170,my-200))
        elif tool == "lorithia":                            #stamps
            screen.blit(copy,canvas)
            subcanvas.blit(Lorithia,(mx-180,my-200))
        elif tool == "melia2":
            screen.blit(copy,canvas)
            subcanvas.blit(Melia_2,(mx-170,my-200))
        elif tool == "chiefdunga":
            screen.blit(copy,canvas)
            subcanvas.blit(chiefdunga,(mx-200,my-300))
        elif tool == "nopon1":
            screen.blit(copy,canvas)
            subcanvas.blit(nopon1,(mx-110,my-200))
        elif tool == "nopon2":
            screen.blit(copy,canvas)
            subcanvas.blit(nopon2,(mx-150,my-100))
        elif tool == "riki":
            screen.blit(copy,canvas)
            subcanvas.blit(riki,(mx-150,my-220))
        elif tool == "riki2":
            screen.blit(copy,canvas)
            subcanvas.blit(riki2,(mx-150,my-220))
            
        screen.set_clip(None)
    display.flip()
quit()
