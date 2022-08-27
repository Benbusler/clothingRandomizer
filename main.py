import random
import pygame
from PIL import Image

pygame.init

#variables
x = random.randint(2,5)
text = r'C:\Users\benbu\Documents\GitHub\clothingRandomizer\images\image'

#determining displayed image
capturedImage = text + str(x) + ".jpg"
print(capturedImage)

img = Image.open(capturedImage)

# get width and height
width = img.width
height = img.height

#setting up the window stuff
displayWidth = width
displayHeight = height
surface = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("images")
displayImage = pygame.image.load(capturedImage)

while True:
    surface.fill((255,255,255))
    surface.blit(displayImage, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()