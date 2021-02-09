import pygame,sys,os, time, random, sqlite3, datetime
from pygame.locals import *                

import flood_interactions as flood
import squirrel_interactions as squirrel
import main_interactions as interactions
import fire_interactions as fire

pygame.init()
defaultHeight = 800
defaultWidth = 830
displayHeight = 800
displayWidth = 830
FPS = 60

scaleHeight = int(displayHeight / defaultHeight)
scaleWidth = int(displayWidth / defaultWidth)

print()
print()

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
gameDisplayRect = gameDisplay.get_rect()
pygame.display.set_caption('Arcadia Unleashed Hunger Games Simulator')

clock = pygame.time.Clock()

gameEnd = False

miscDistricts = ['Doom', 'Wings', 'Sky', 'Corruption', 'War', 'Claw', 'Fang', 'Eclipse', 'Abyss', 'Snow', 'Rain']

def terminate():      
    pygame.quit()
    sys.exit()

#-----SETUP--------------------------------------------------------------------------------

def getFiles():    #Get names, pronouns, groups, etc

    nameList = []
    districtList = []
    unassignedCats = 0
    
    for fileFolder in os.listdir('headshots'):
        if (os.path.isdir('headshots\\' + fileFolder)) & (fileFolder != 'STORAGE'):
        
            for fileFolder2 in os.listdir('headshots\\' + fileFolder):
                name = ((fileFolder2.split('_'))[0]).title()
                pronouns = ((fileFolder2.split('_'))[1])
                spirit = (((fileFolder2.split('_'))[2]).split('.'))[0]
                image = (pygame.image.load('headshots\\'+fileFolder+'\\'+fileFolder2))
                nameList.append((name, pronouns, image, fileFolder, spirit))
                if fileFolder not in districtList:
                    districtList.append(fileFolder)
                
        elif os.path.isfile('headshots\\' + fileFolder): 
        
            name = ((fileFolder.split('_'))[0]).title()
            pronouns = ((fileFolder.split('_'))[1])
            spirit = ((((fileFolder.split('_'))[2]).split('.'))[0]).title()
            image = (pygame.image.load('headshots\\' + fileFolder))
            nameList.append((name, pronouns, image, 'UNASSIGNED', spirit))
            unassignedCats += 1
            
    random.shuffle(nameList)
    return nameList,districtList,unassignedCats
       
def assignCats(miscDistricts,districtList,unassignedCats,nameList):
  
    if unassignedCats > 0:
        perDistrict = (len(nameList) - unassignedCats) / len(districtList)
        #if perDistrict == 0:
            #perDistrict = 3
        
        while unassignedCats > 0:
            try:
                newDistrict = miscDistricts.pop(random.randint(0,len(miscDistricts)-1))
            except:
                newDistrict = "theRestOfYou"
                
            districtList.append(newDistrict)
            x = 0
            
            while x < perDistrict:
                x,unassignedCats,nameList = assignDistrict(x,newDistrict,unassignedCats,nameList)
                
    random.shuffle(nameList)
    return nameList,districtList
    
def assignDistrict(x,newDistrict,unassignedCats,nameList):
    i = 0
    temp_nameList = nameList
    while i < len(temp_nameList):
    
        if nameList[i][3] == 'UNASSIGNED':
            x += 1
            unassignedCats -= 1
            name, pronouns, file, district,spirit = nameList[i]
            nameList.remove((name,pronouns,file,district,spirit))
            nameList.append((name,pronouns,file,newDistrict,spirit))
            return x, unassignedCats, nameList
        else:
            i += 1
            
    return 10000,0, nameList
    
#-------TEXT BOX FUNCTIONS-------------------------------------------------------------------------------
    
#this function draws supplied text onto the surface supplied at the height supplied, centred
def drawCentredText(text, font, surface, y, colour): 
    textobj = font.render(text, 1, colour)
    
    leftOverText,textsToDisplay = wrapAroundText(surface, text, colour, (134*scaleWidth,y,410,80), font)
    if leftOverText != "":
        print(leftOverText)
    
    for text,y in textsToDisplay:
        textrect = text.get_rect()
        centre = 410 - (textrect.width / 2)
        textrect.topleft = (centre, y)
        surface.blit(text, textrect)
    
def wrapAroundText(surface, text, color, rect, font, bkg=None):

    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2
    textsToDisplay = []

    # get the height of the font (tallest and lowest characters)
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1
        if y + fontHeight > rect.bottom:
            break
        while (font.size(text[:i])[0] < rect.width) & (i < len(text)):
            i += 1
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], 1, color)
            
        textsToDisplay.append((image,y))
        y += fontHeight + lineSpacing
        text = text[i:]

    return text, textsToDisplay
    
    
#------User Interface---------------------------------------------------------------------------------    
    
    
def showImageLeft(image,interactionNumber,mainSurface):

    pygame.draw.rect(mainSurface, (255,255,255), (36*scaleWidth,(56*scaleHeight+interactionNumber*100),88*scaleWidth,88*scaleHeight),7)
    
    mainSurface.blit(pygame.transform.smoothscale(image, (80*scaleWidth,80*scaleHeight)), (40*scaleWidth,(60*scaleHeight+interactionNumber*100)))  
    
def showImageRight(image, interactionNumber,mainSurface):

    pygame.draw.rect(mainSurface, (255,255,255), (696*scaleWidth,(56*scaleHeight+interactionNumber*100),88*scaleWidth,88*scaleHeight),7)
    
    mainSurface.blit(pygame.transform.smoothscale(image, (80*scaleWidth,80*scaleHeight)), (700*scaleWidth,(60*scaleHeight+interactionNumber*100)))  
    
def showImageCentre(image, interactionNumber,mainSurface):

    pygame.draw.rect(mainSurface, (255,255,255), (366*scaleWidth,(56*scaleHeight+interactionNumber*100),88*scaleWidth,88*scaleHeight),7)
    
    mainSurface.blit(pygame.transform.smoothscale(image, (80*scaleWidth,80*scaleHeight)), (370*scaleWidth,(60*scaleHeight+interactionNumber*100)))  
    
def showTitleText(string,mainSurface):
    drawCentredText(string, pygame.font.SysFont('ariel', (int(50*(scaleWidth+scaleHeight)/2))),mainSurface,(10*scaleHeight),(255,255,255))
    

def showInteractionText(string, interactionNumber,mainSurface): 
    drawCentredText(string, pygame.font.SysFont('ariel', (int(25*(scaleWidth+scaleHeight)/2))),mainSurface, (80*scaleHeight+interactionNumber*100), (255,255,255))
 
#-------------WINNER CHECKS-----------------------------------------------------------

def checkWin(nameList,mainSurface):
    if len(nameList) == 1:
        print()
        print("We have a winner! " + nameList[0][0] + " is victorious!")
        gameDisplay.fill((25,25,25))
        showImageCentre(nameList[0][2], 0,mainSurface)
        showTitleText(nameList[0][0] + " WINS!",mainSurface)
        gameDisplay.blit(mainSurface,(0,0))
        clock.tick(FPS)
        pygame.display.update()
        while True:
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    terminate()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()

def checkLose(nameList,mainSurface):
    if len(nameList) == 0:
        print()
        print("Oh no...everyone's dead. Need to stop that happening.")
        gameDisplay.fill((25,25,25))
        showTitleText("NO-ONE WINS!",mainSurface)
        gameDisplay.blit(mainSurface,(0,0))
        clock.tick(FPS)
        pygame.display.update()
        while True:
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    terminate()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()

#--------WAIT FOR CONTINUE------------------------------------------------------------

def waitForContinue(track,knob,scrolling,ratio,mainSurface,interactionNumber):
    continueToNext = False
    
    ratio = gameDisplay.get_height() / (60*scaleHeight+interactionNumber*100)
    scrollThick = 20 #thickness of scroll bar
    track = pygame.Rect(gameDisplayRect.left,gameDisplayRect.top,scrollThick,gameDisplayRect.height)   
    knob = pygame.Rect(track)  
    knob.height = track.height * ratio
    scrolling   = False
    
    while not continueToNext:
        
        gameDisplay.blit(mainSurface,(0,(knob.top / ratio)* -1))
        pygame.draw.rect(gameDisplay, (255,0,0), track, 0 )
        pygame.draw.rect(gameDisplay, (180,180,180), knob.inflate(0,-5), 2)
    
        clock.tick(FPS)
        pygame.display.update()
        
        for event in pygame.event.get():   
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_SPACE:
                    continueToNext = True
                    gameDisplay.fill((25,25,25))
                    mainSurface.fill((25,25,25))
                    
            if (event.type == MOUSEMOTION and scrolling):
                if event.rel[1] != 0:
                    move = max(event.rel[1], track.top - knob.top)
                    move = min(move, track.bottom - knob.bottom)
                    if move != 0:
                        knob.move_ip((0, move))
                                        
            elif event.type == MOUSEBUTTONDOWN and knob.collidepoint(event.pos):
                scrolling = True
                                
            elif event.type == MOUSEBUTTONUP:
                scrolling = False
                    
#-------------SCROLLING-----------------------------------------------------------------                   
                    
def scrollStuff(mainSurface):

    ratio = gameDisplay.get_height() / mainSurface.get_height()
    scrollThick = 20 #thickness of scroll bar
    track = pygame.Rect(gameDisplayRect.left,gameDisplayRect.top,scrollThick,gameDisplayRect.height)   
    knob = pygame.Rect(track)  
    knob.height = track.height * ratio
    scrolling   = False
    
    return track,knob,scrolling,ratio
    
#---------IMAGE SAVING----------------------------------------------------------------    
    
def saveSurface(mainSurface,roundCounter,folderName,interactionNumber):
    croppedImage = cropSurface(displayWidth*scaleWidth,(60*scaleHeight+interactionNumber*100),mainSurface,(0,0))
    pygame.image.save(croppedImage,('game_rounds\\' + folderName + '\\' + str(roundCounter) + '.jpeg'))
   
   
def createFolder():
    currentDate = (datetime.date.today()).strftime("%Y-%m-%d")
    currentTime = (datetime.datetime.now()).strftime("%H-%M-%S")
    os.makedirs('game_rounds\\' + currentDate + '_' + currentTime)
    return currentDate + '_' + currentTime
    
def cropSurface(newWidth,newHeight,image,origin):
    cropped = pygame.Surface((newWidth,newHeight))
    cropped.blit(image,origin)
    return cropped 
    

#-------------MAIN--------------------------------------------------------------------    
def main():

    nameList,districtList,unassignedCats = getFiles()
    nameList,districtList = assignCats(miscDistricts,districtList,unassignedCats,nameList)
    
    roundCounter = 0
    folderName = createFolder()

    while True:
        
        #setup surface size to always be long enough
        lenMinusSeven = len(nameList) - 7
        if len(nameList) < 8:
            mainSurfaceHeightExtra = 0
        else:
            mainSurfaceHeightExtra = 100*lenMinusSeven
           
        mainSurface = pygame.Surface((displayWidth*scaleWidth,(displayHeight*scaleHeight + mainSurfaceHeightExtra)))
        track,knob,scrolling,ratio = scrollStuff(mainSurface)
        
        gameDisplay.fill((25,25,25))
        mainSurface.fill((25,25,25))
     
        randomEventRoll = random.randint(1,100)
        if randomEventRoll < 5: #squirrels
            nameList,interactionNumber = squirrel.squirrel(nameList,mainSurface)
            
        elif randomEventRoll < 10: #flood
            nameList,interactionNumber = flood.flood(nameList,mainSurface)
            
        elif randomEventRoll < 15: #fire
            nameList,interactionNumber = fire.fire(nameList,mainSurface)
            
        else: #no event
            nameList,interactionNumber = interactions.interactions(nameList,mainSurface)
            
        roundCounter += 1
        saveSurface(mainSurface,roundCounter,folderName,interactionNumber)
        
        waitForContinue(track,knob,scrolling,ratio,mainSurface,interactionNumber)  
            
        checkWin(nameList,mainSurface)
        checkLose(nameList,mainSurface)                   
     
        pygame.display.update()
        clock.tick(FPS)
        
        for event in pygame.event.get():      
                if event.type == QUIT:
                    terminate()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()
                

if __name__ == '__main__': main()