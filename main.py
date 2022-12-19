from asyncio.windows_events import NULL
from multiprocessing.connection import wait
from pickletools import long1
import random
from tokenize import Double
from xmlrpc.client import boolean
import pygame
from PIL import Image,ImageGrab 
import time
import requests

pygame.init

#variables

temp = int
light = int
rain = False

#taking in all the information


enteries = []
# Replace with your Thingspeak API key
api_key = 'RAAVPDMVCSJ9KA5G'

# Replace with the ID of the channel you want to retrieve data from
channel_id = '1964022'

# Set the number of results you want to retrieve (up to a maximum of 8000)
results = 100

# Set the URL for the Thingspeak API
url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key={}&results={}'.format(channel_id, api_key, results)

# Send a GET request to the Thingspeak API
response = requests.get(url)

# If the request was successful, print the data
if response.status_code == 200:
  data = response.json()
  #for feed in data['feeds']:
    #print(feed['created_at'], feed['field1'])
for feed in data['feeds']:
    enteries.append(feed['field1'])
else:
#print('Failed to retrieve data from Thingspeak')
    NULL
#print(enteries)
newEnterries = [x for x in enteries if x != None]
#print("\n\n")
temp = newEnterries[len(newEnterries)-1][0:2]
print("temp: " + temp)

#for feed in data['feeds']:
    #print(feed['created_at'], feed['field2'])
for feed in data['feeds']:
    enteries.append(feed['field2'])
else:
  #print('Failed to retrieve data from Thingspeak')
    NULL
#print(enteries)
newEnterries = [x for x in enteries if x != None]
#print("\n\n")
light = newEnterries[len(newEnterries)-1][0:2]
print("Light: " + light)

#for feed in data['feeds']:
    #print(feed['created_at'], feed['field2'])
for feed in data['feeds']:
    enteries.append(feed['field3'])
else:
  #print('Failed to retrieve data from Thingspeak')
  NULL

#print(enteries)
newEnterries = [x for x in enteries if x != None]
#print("\n\n")
humidity = newEnterries[len(newEnterries)-1][0:2]
print("Humidity: " + humidity)

headx = random.randint(1,7)
bodyx = random.randint(1,8)
pantx = random.randint(1,6)
footx = random.randint(1,8)
text = r'images\clothing'

#if int(light) > 50:
#    headx = random.randint(1,4)
#NULL


#if temp < 40 & light > 70:
#    headx = 


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

#def rain():
#    choice = random.randint(1,3)
#    if choice == 1: #chooses a rain prevention specific clothing
 #       bodyx = random.randint(1,2)
  #      bodyChoice = text + r"\bodyRain" + str(bodyx) + ".png"
   # elif choice == 2: #gives you a hat
    #    headx = random.randint(1,2)
     #   headChoice = text + r"\head" + str(headx) + ".png"
   # else: #gives you an umbrella
        #does nothing rn
    #    NULL

#def glass():
 #   NULL
    
    #create code to put sunglasses onto the image
    

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


#setting the background dimensions
surface.fill((0,0,0))
surface.blit(displayHead, (displayWidth / 2 - headWidth / 2 , 0))
surface.blit(displayBody, (displayWidth / 2 - bodyWidth / 2 , headHeight))
surface.blit(displayPant, (displayWidth / 2 - pantWidth / 2 , bodyHeight))
surface.blit(displayFoot, (displayWidth / 2 - footWidth / 2, pantHeight))
pygame.display.update()


#pic = ImageGrab.grab(bbox=(1000,1500,1200,1500))
#pic.show()
#pic.save("ss.png")

#pic = pyscreenshot.grab(bbox=(1000, 1400, 1200, 1500))
#pic.show()
#pic.save("ss.png")

#ends the window once ESC has been hit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
        