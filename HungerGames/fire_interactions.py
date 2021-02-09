import pygame,sys,os, time, random, sqlite3, datetime
from pygame.locals import *       

import main

def fire(nameList,mainSurface): #FIRE
    print("FLASH FIRE")
    main.showTitleText("FLASH FIRE",mainSurface)
    
    playersToInteract = nameList[:]
    interactionNumber = 0
    while len(playersToInteract) > 0:
        
            if len(playersToInteract) == 1: #only one player left to assign
                randomNumber = random.randint(1,2)
                if len(nameList) == 1:
                    randomNumber = 1
                if playersToInteract[0][4] == 'Ignis':
                    string = playersToInteract[0][0] + " is an Ignis, they were made for this."
                    main.showInteractionText(string, interactionNumber,mainSurface)
                elif randomNumber == 1:
                    string = playersToInteract[0][0] + " survives the fire"
                    main.showInteractionText(string, interactionNumber,mainSurface)
                else:
                    string = playersToInteract[0][0] + " burns to death"
                    main.showInteractionText(string, interactionNumber,mainSurface)
                    nameList.remove(playersToInteract[0])
                main.showImageLeft(playersToInteract[0][2], interactionNumber,mainSurface)
                playersToInteract = []
                
            else:
                randomNumber1 = random.randint(1,3)
                if randomNumber1 == 1:
                    randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
                    playersToInteract.remove(randomPlayer)
                    string = randomPlayer[0] + " survives the fire"
                    main.showInteractionText(string, interactionNumber,mainSurface)
                    main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
                    
                elif randomNumber1 == 2:
                    randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
                    playersToInteract.remove(randomPlayer)
                    if randomPlayer[4] == 'Aqua':
                        string = randomPlayer[0] + " is an Ignis, they were made for this."
                        main.showInteractionText(string, interactionNumber,mainSurface)
                    else:
                        string = "The fire defeats " + randomPlayer[0]
                        main.showInteractionText(string, interactionNumber,mainSurface)
                        nameList.remove(randomPlayer)
                    main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
                    
                elif randomNumber1 == 3:
                    randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
                    playersToInteract.remove(randomPlayer1)
                    randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
                    playersToInteract.remove(randomPlayer2)
                    main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
                    main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
                    if randomPlayer1[3] == randomPlayer2[3]:
                        string = randomPlayer1[0] + " was about to sacrifice " + randomPlayer2[0] + " to the flames, before remembering they're on the same team."
                        main.showInteractionText(string, interactionNumber,mainSurface)
                    else:
                        string = randomPlayer1[0] + " sacrifices " + randomPlayer2[0] + " to the blaze"
                        main.showInteractionText(string, interactionNumber,mainSurface)
                        nameList.remove(randomPlayer2)
                        
            interactionNumber += 1
                    
                  
    random.shuffle(nameList)
    return nameList,interactionNumber
    
