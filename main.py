import random
import pygame
from PIL import Image

pygame.init

#variables
headx = random.randint(1,2)
bodyx = random.randint(1,4)
pantx = random.randint(1,4)
footx = random.randint(1,4)
text = r'C:\Users\benbu\Documents\GitHub\clothingRandomizer\images\clothing'

#determining displayed images
headChoice = text + r"\head" + str(headx) + ".png"
bodyChoice = text + r"\body" + str(bodyx) + ".png"
pantChoice = text + r"\pant" + str(pantx) + ".png"
footChoice = text + r"\foot" + str(footx) + ".png"
#print(capturedImage)

#img = Image.open(capturedImage)

# get width and height
#width = img.width
#height = img.height

#setting up the window stuff
displayWidth = 400
displayHeight = 600
surface = pygame.display.set_mode((displayWidth, 2 * displayHeight))
pygame.display.set_caption("Fit 4 2 day")



displayHead = pygame.image.load(headChoice)
displayBody = pygame.image.load(bodyChoice)
displayPant = pygame.image.load(pantChoice)
displayFoot = pygame.image.load(footChoice)

displayHeadO = Image.open(headChoice)
displayBodyO = Image.open(bodyChoice)
displayPantO = Image.open(pantChoice)
displayFootO = Image.open(footChoice)

headHeight = displayHeadO.height
bodyHeight = displayHeadO.height + displayBodyO.height
pantHeight = displayHeadO.height + displayBodyO.height + displayPantO.height

headWidth = displayHeadO.width
bodyWidth = displayBodyO.width
pantWidth = displayPantO.width
footWidth = displayFootO.width
while True:
    surface.fill((0,0,0))
    surface.blit(displayHead, (displayWidth / 2 - headWidth / 2 , 0))
    surface.blit(displayBody, (displayWidth / 2 - bodyWidth / 2 , headHeight))
    surface.blit(displayPant, (displayWidth / 2 - pantWidth / 2 , bodyHeight))
    surface.blit(displayFoot, (displayWidth / 2 - footWidth / 2, pantHeight))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()