import pygame,sys,os, time, random, sqlite3, datetime
from pygame.locals import *       

import main

def interactions(nameList,mainSurface):
    print("NO EVENT")
    main.showTitleText("NO EVENT",mainSurface)
    
    playersToInteract = nameList[:]
    interactionNumber = 0
    
    while len(playersToInteract) > 0:
        if len(playersToInteract) == 1:
            randomNumber = random.randint(0,400)
        elif len(playersToInteract) == 2:
            randomNumber = random.randint(0,800)
        elif len(playersToInteract) == 3:
            randomNumber = random.randint(0,1000)
        else:
            randomNumber = random.randint(0,1200)
            
        if len(nameList) == 1: #guarantees survivor
            randomNumber = 200
        
        
        #SINGLE PLAYER 0 - 400
        if randomNumber < 10: #single player water death (or not)
            randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer)
            
            playerDead = singlePlayerWaterDeaths(randomPlayer[0],interactionNumber,mainSurface, randomPlayer[4])
            if playerDead == 1:
                nameList.remove(randomPlayer)
                
            main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
            
        elif randomNumber < 20: #single player fire death (or not)
            randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer)
            
            playerDead = singlePlayerFireDeaths(randomPlayer[0],interactionNumber,mainSurface, randomPlayer[4])
            if playerDead == 1:
                nameList.remove(randomPlayer)
                
            main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
            
        elif randomNumber < 30: #single player darkness death (or not)
            randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer)
            
            playerDead = singlePlayerDarknessDeaths(randomPlayer[0],interactionNumber,mainSurface, randomPlayer[4])
            if playerDead == 1:
                nameList.remove(randomPlayer)
                
            main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
        
        elif randomNumber < 40: #single player earth death (or not)
            randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer)
            
            playerDead = singlePlayerEarthDeaths(randomPlayer[0],interactionNumber,mainSurface, randomPlayer[4])
            if playerDead == 1:
                nameList.remove(randomPlayer)
                
            main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
        
        elif randomNumber < 50: #single player life death (or not)
            randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer)
            
            playerDead = singlePlayerLifeDeaths(randomPlayer[0],interactionNumber,mainSurface, randomPlayer[4])
            if playerDead == 1:
                nameList.remove(randomPlayer)
                
            main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
        
        elif randomNumber < 100: #single player dies
            randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer)
            
            singlePlayerDies(randomPlayer[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer)
            
            main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
            
        elif randomNumber <= 400: #single player lives
            randomPlayer = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer)
            
            singlePlayerLives(randomPlayer[0],interactionNumber,mainSurface,randomPlayer[4])
            
            main.showImageLeft(randomPlayer[2], interactionNumber,mainSurface)
                    
                    
        #TWO PLAYERS 401 - 800
        elif randomNumber < 500: #p1 kills p2 (or attempted)
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            
            if randomPlayer1[3] == randomPlayer2[3]:
                twoTryKillTeammate(randomPlayer1[0],randomPlayer2[0],interactionNumber,mainSurface)
            else:
                firstKillsSecond(randomPlayer1[0],randomPlayer2[0],interactionNumber,mainSurface)
                nameList.remove(randomPlayer2)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            
        elif randomNumber < 550: #p1 and p2 die
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            
            allTwoDie(randomPlayer1[0],randomPlayer2[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer1)
            nameList.remove(randomPlayer2)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            
        elif randomNumber < 760: #p1 and p2 live
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            
            allTwoLive(randomPlayer1[0],randomPlayer2[0],interactionNumber,mainSurface)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            
        elif randomNumber < 800: #p1 and p2 suicide pact
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            
            twoPlayerSuicidePact(randomPlayer1[0],randomPlayer2[0],interactionNumber,mainSurface,nameList)
            
            if len(nameList) == 2:
                print("2 player suicide pact success - ADD THIS OPTION")
            else:
                nameList.remove(randomPlayer1)
                nameList.remove(randomPlayer2)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
        
        
        #THREE PLAYERS 801 - 1000
        elif randomNumber < 830: #p1 kills p2 and p3
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            
            
            oneKillsTwo(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer2)
            nameList.remove(randomPlayer3)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            
        elif randomNumber < 880: #p1 is killed by p2 and p3 
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            
            
            twoKillsOne(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer1)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            
        elif randomNumber < 900: #p1 p2 p3 die
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            
            
            allThreeDie(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer1)
            nameList.remove(randomPlayer2)
            nameList.remove(randomPlayer3)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            
        elif randomNumber < 980: #p1 p2 p3 live
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            
            
            allThreeLive(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],interactionNumber,mainSurface)
           
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            
        elif randomNumber <= 1000: #p1 p2 p3 suicide pact
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            
            threePlayerSuicidePact(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],interactionNumber,mainSurface,nameList)
            
            if len(nameList) == 3:
                print("3 player suicide pact success - ADD THIS OPTION")
            else:
                nameList.remove(randomPlayer1)
                nameList.remove(randomPlayer2)
                nameList.remove(randomPlayer3)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            
            
        #FOUR PLAYERS 1001 - 1200
        elif randomNumber < 1020: #p1 kills p2 p3 p4
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            randomPlayer4 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer4)
            
            oneKillsThree(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],randomPlayer4[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer2)
            nameList.remove(randomPlayer3)
            nameList.remove(randomPlayer4)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            #add fourth image
            
        elif randomNumber < 1060: #p1 p2 kills p3 p4
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            randomPlayer4 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer4)
            
            twoKillsTwo(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],randomPlayer4[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer3)
            nameList.remove(randomPlayer4)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            #add fourth image
            
        elif randomNumber < 1100: #p1 killed by p2 p3 p4
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            randomPlayer4 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer4)
            
            threeKillsOne(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],randomPlayer4[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer1)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            #add fourth image
            
        elif randomNumber < 1110: #p1 p2 p3 p4 die 
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            randomPlayer4 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer4)
            
            allFourDie(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],randomPlayer4[0],interactionNumber,mainSurface)
            nameList.remove(randomPlayer1)
            nameList.remove(randomPlayer2)
            nameList.remove(randomPlayer3)
            nameList.remove(randomPlayer4)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            #add fourth image
            
        elif randomNumber < 1190: #p1 p2 p3 p4 live
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            randomPlayer4 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer4)
            
            allFourLive(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],randomPlayer4[0],interactionNumber,mainSurface)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            #add fourth image
            
        elif randomNumber <= 1200: #p1 p2 p3 p4 suicide pact
            randomPlayer1 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer1)
            randomPlayer2 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer2)
            randomPlayer3 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer3)
            randomPlayer4 = playersToInteract[random.randint(0,len(playersToInteract)-1)]
            playersToInteract.remove(randomPlayer4)
            
            fourPlayerSuicidePact(randomPlayer1[0],randomPlayer2[0],randomPlayer3[0],randomPlayer4[0],interactionNumber,mainSurface,nameList)
            
            if len(nameList) == 4:
                print("4 player suicide pact success - ADD THIS OPTION")
            else:
                nameList.remove(randomPlayer1)
                nameList.remove(randomPlayer2)
                nameList.remove(randomPlayer3)
                nameList.remove(randomPlayer4)
            
            main.showImageLeft(randomPlayer1[2], interactionNumber,mainSurface)
            main.showImageRight(randomPlayer2[2], interactionNumber,mainSurface)
            #add third image
            #add fourth image

         
        interactionNumber += 1
    
    random.shuffle(nameList)
    return nameList,interactionNumber
    
#------SINGLE PLAYER OPTIONS------------------------------------------------------------------------------
    
def singlePlayerLives(playerName,interactionNumber,mainSurface,spiritGroup):
    everyoneOptions =  ["PLAYER thinks of home",
                "PLAYER looks at the deathmoon",
                "PLAYER cries",
                "PLAYER receives RANDOMITEM from a sponsor"]
    notAquaOptions = ["PLAYER struggles to find water"]
    notIgnisOptions = ["PLAYER fails to start a fire"]
    notVentusOptions = ["PLAYER struggles to see in the darkness"]
    notTerraOptions = ["PLAYER searches for a shelter"]
    notVitaOptions = ["PLAYER wishes they had a companion",
                      "PLAYER licks their wounds"]
    aquaOptions = ["PLAYER finds some water"]
    ignusOptions = ["PLAYER easily starts a fire"]
    ventusOptions = ["PLAYER walks through the darkness because it feels right",
                     "PLAYER creates a light to ward off beasts"]
    terraOptions = ["PLAYER makes a shelter"]
    vitaOptions = ["PLAYER tends to their wounds"]
    items = ["spinch", "bombs", "knives", "soap", "water", "a torch", "fresh food"]
    
    if spiritGroup == 'Aqua':
        options = everyoneOptions + notIgnisOptions + notVentusOptions + notTerraOptions + notVitaOptions + aquaOptions
        selectedOption = options[random.randint(0,(len(options)-1))]
    elif spiritGroup == 'Ignis':
        options = everyoneOptions + notAquaOptions + notVentusOptions + notTerraOptions + notVitaOptions + ignisOptions
        selectedOption = options[random.randint(0,(len(options)-1))]
    elif spiritGroup == 'Ventus':
        options = everyoneOptions + notAquaOptions + notIgnisOptions + notTerraOptions + notVitaOptions + ventusOptions
        selectedOption = options[random.randint(0,(len(options)-1))]
    elif spiritGroup == 'Terra':
        options = everyoneOptions + notAquaOptions + notIgnisOptions + notVentusOptions + notVitaOptions + terraOptions
        selectedOption = options[random.randint(0,(len(options)-1))]
    elif spiritGroup == 'Vita':
        options = everyoneOptions + notAquaOptions + notIgnisOptions + notVentusOptions + notTerraOptions + vitaOptions
        selectedOption = options[random.randint(0,(len(options)-1))]
    else:
        options = everyoneOptions + notAquaOptions + notIgnisOptions + notVentusOptions + notTerraOptions + notVitaOptions
        selectedOption = options[random.randint(0,(len(options)-1))]
    
    selectedOption = selectedOption.replace("PLAYER", playerName)
    selectedOption = selectedOption.replace("RANDOMITEM", items[random.randint(0,(len(items)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
    
def singlePlayerDies(playerName,interactionNumber,mainSurface):
    options =  ["PLAYER  falls off a cliff",
                "While trying to escape the arena, PLAYER falls down a hole",
                "PLAYER dies from an infection",
                "PLAYER is killed by RANDOMANIMAL"]
    animals = ["a moose", "a wolf", "an eagle"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER", playerName)
    selectedOption = selectedOption.replace("RANDOMANIMAL", animals[random.randint(0,(len(animals)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
#------SG PREVENTABLE SINGLE PLAYER DEATHS-----------------------------------------------------------------    
    
def singlePlayerWaterDeaths(playerName,interactionNumber,mainSurface, spiritGroup):
    aquaOptions = ["PLAYER uses their powers to find some water",
                    "PLAYER went for a swim"]
    otherOptions = ["PLAYER dies of thirst",
                    "PLAYER drowned"]
                    
    if spiritGroup == 'Aqua':
        selectedOption = aquaOptions[random.randint(0,(len(aquaOptions)-1))]
        dead = 0
    else:
        selectedOption = otherOptions[random.randint(0,(len(otherOptions)-1))]
        dead = 1
        
    selectedOption = selectedOption.replace("PLAYER", playerName)
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    return dead
    
def singlePlayerFireDeaths(playerName,interactionNumber,mainSurface, spiritGroup):
    ignisOptions = ["PLAYER uses their powers to start a fire"]
    otherOptions = ["PLAYER died of from the cold",
                    "PLAYER couldn't start a fire and died"]
                    
    if spiritGroup == 'Ignis':
        selectedOption = ignisOptions[random.randint(0,(len(ignisOptions)-1))]
        dead = 0
    else:
        selectedOption = otherOptions[random.randint(0,(len(otherOptions)-1))]
        dead = 1
        
    selectedOption = selectedOption.replace("PLAYER", playerName)
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    return dead
    
def singlePlayerDarknessDeaths(playerName,interactionNumber,mainSurface, spiritGroup):
    ventusOptions = ["PLAYER uses their powers to make a light",
                    "PLAYER makes a light to keep monsters away"]
    otherOptions = ["PLAYER is killed in the darkness"]
                    
    if spiritGroup == 'Ventus':
        selectedOption = ventusOptions[random.randint(0,(len(ventusOptions)-1))]
        dead = 0
    else:
        selectedOption = otherOptions[random.randint(0,(len(otherOptions)-1))]
        dead = 1
        
    selectedOption = selectedOption.replace("PLAYER", playerName)
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    return dead
    
def singlePlayerEarthDeaths(playerName,interactionNumber,mainSurface, spiritGroup):
    terraOptions = ["PLAYER uses their powers to make a shelter",
                    "PLAYER to hide from the elements",
                    "PLAYER takes a nap in a shelter they made"]
    otherOptions = ["PLAYER died from exposure",
                    "PLAYER couldn't find shelter and died"]
                    
    if spiritGroup == 'Terra':
        selectedOption = terraOptions[random.randint(0,(len(terraOptions)-1))]
        dead = 0
    else:
        selectedOption = otherOptions[random.randint(0,(len(otherOptions)-1))]
        dead = 1
        
    selectedOption = selectedOption.replace("PLAYER", playerName)
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    return dead
    
def singlePlayerLifeDeaths(playerName,interactionNumber,mainSurface, spiritGroup):
    vitaOptions = ["PLAYER uses their powers to regain health",
                    "PLAYER heals themself"]
    otherOptions = ["PLAYER dies from their wounds",
                    "PLAYER bleeds out"]
                    
    if spiritGroup == 'Vita':
        selectedOption = vitaOptions[random.randint(0,(len(vitaOptions)-1))]
        dead = 0
    else:
        selectedOption = otherOptions[random.randint(0,(len(otherOptions)-1))]
        dead = 1
        
    selectedOption = selectedOption.replace("PLAYER", playerName)
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    return dead

#------TWO PLAYERS---------------------------------------------------------------------------

def firstKillsSecond(playerName1,playerName2,interactionNumber,mainSurface):
    options =  ["PLAYER1 kills PLAYER2 with RANDOMWEAPON",
                "PLAYER1 and PLAYER2 enter a suicide pact, PLAYER1 doesn't follow through",
                "PLAYER2 and PLAYER1 enter a suicide pact, PLAYER1 doesn't follow through"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)

def allTwoLive(playerName1,playerName2,interactionNumber,mainSurface):
    options =  ["PLAYER1 chases PLAYER2 with RANDOMWEAPON",
                "PLAYER1 lets PLAYER2 into their shelter",
                "PLAYER1 distracts PLAYER2 with a laser pointer and runs away"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "a rock", "a pebble"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)

def allTwoDie(playerName1,playerName2,interactionNumber,mainSurface):
    options =  ["PLAYER1 gets into a fight with PLAYER2 but they both fall down a hole"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def twoTryKillTeammate(playerName1,playerName2,interactionNumber,mainSurface):
    options =  ["PLAYER1 is about to kill PLAYER2, when they remember they're on the same team"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def twoPlayerSuicidePact(playerName1,playerName2,interactionNumber,mainSurface,nameList):
    if len(nameList) == 2:
        options =  ["PLAYER1 and PLAYER2 enter a suicide pact, the gamemakers need a victor"]
    else:
        options =  ["PLAYER1 and PLAYER2 enter a suicide pact, but the gamemakers don't care"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
#------THREE PLAYERS----------------------------------------------------------------------------

def oneKillsTwo(playerName1,playerName2,playerName3,interactionNumber,mainSurface):
    options =  ["PLAYER1 gets into a fight with PLAYER2 and PLAYER3, and kills both of them"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def twoKillsOne(playerName1,playerName2,playerName3,interactionNumber,mainSurface):
    options =  ["PLAYER1 gets into a fight with PLAYER2 and PLAYER3, but they kill PLAYER1"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def allThreeDie(playerName1,playerName2,playerName3,interactionNumber,mainSurface):
    options =  ["PLAYER1, PLAYER2, and PLAYER3 get into a fight and they all die"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def allThreeLive(playerName1,playerName2,playerName3,interactionNumber,mainSurface):
    options =  ["PLAYER1,PLAYER2, and PLAYER3 run into each other and form an alliance",
                "PLAYER1 sees PLAYER2 and PLAYER3 fighting and walks away",
                "PLAYER1 meets PLAYER2 and PLAYER3 and spends the night with them"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def threePlayerSuicidePact(playerName1,playerName2,playerName3,interactionNumber,mainSurface,nameList):
    if len(nameList) == 3:
        options =  ["PLAYER1, PLAYER3, and PLAYER2 enter a suicide pact, the gamemakers need a victor"]
    else:
        options =  ["PLAYER1,PLAYER3, and PLAYER2 enter a suicide pact, but the gamemakers don't care"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
    
#------FOUR PLAYERS-----------------------------------------------------------------------------

def oneKillsThree(playerName1,playerName2,playerName3,playerName4,interactionNumber,mainSurface):
    options =  ["PLAYER1 gets into a fight with PLAYER2, PLAYER3, and PLAYER4, and kills all of them"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("PLAYER4", playerName4)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)

def twoKillsTwo(playerName1,playerName2,playerName3,playerName4,interactionNumber,mainSurface):
    options =  ["PLAYER1 and PLAYER3 get into a fight with PLAYER2 and PLAYER4, PLAYER3 and PLAYER4 are killed"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("PLAYER4", playerName4)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def threeKillsOne(playerName1,playerName2,playerName3,playerName4,interactionNumber,mainSurface):
    options =  ["PLAYER1 gets into a fight with PLAYER2, PLAYER3, and PLAYER4, they kill PLAYER1"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("PLAYER4", playerName4)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def allFourDie(playerName1,playerName2,playerName3,playerName4,interactionNumber,mainSurface):
    options =  ["PLAYER1, PLAYER2, PLAYER3, and PLAYER4 start fighting, and they all die"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("PLAYER4", playerName4)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def allFourLive(playerName1,playerName2,playerName3,playerName4,interactionNumber,mainSurface):
    options =  ["PLAYER1, PLAYER2, PLAYER3, and PLAYER4 share a shelter",
                "PLAYER1, PLAYER2, and PLAYER3 raid PLAYER4's shelter",
                "PLAYER1, PLAYER2, and PLAYER3 stalk PLAYER4",
                "PLAYER1, PLAYER2, PLAYER3, and PLAYER4 search for others",
                "PLAYER1, PLAYER2, PLAYER3, and PLAYER4 go fishing"]
    weapons = ["a knife", "a sword", "a gun", "a crossbow", "their powers", "a rock", "a pebble", "their claws", "their fangs"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("PLAYER4", playerName4)
    selectedOption = selectedOption.replace("RANDOMWEAPON",weapons[random.randint(0,(len(weapons)-1))])
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)
    
def fourPlayerSuicidePact(playerName1,playerName2,playerName3,playerName4,interactionNumber,mainSurface,nameList):
    if len(nameList) == 3:
        options =  ["PLAYER1, PLAYER3, PLAYER4, and PLAYER2 enter a suicide pact, the gamemakers need a victor"]
    else:
        options =  ["PLAYER1,PLAYER3, PLAYER4, and PLAYER2 enter a suicide pact, but the gamemakers don't care"]
    
    selectedOption = options[random.randint(0,(len(options)-1))]
    selectedOption = selectedOption.replace("PLAYER1", playerName1)
    selectedOption = selectedOption.replace("PLAYER2", playerName2)
    selectedOption = selectedOption.replace("PLAYER3", playerName3)
    selectedOption = selectedOption.replace("PLAYER4", playerName4)
    
    main.showInteractionText(selectedOption, interactionNumber,mainSurface)