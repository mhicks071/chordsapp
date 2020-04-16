#Chord switching app by Mason W. Hicks, dev 4/16/2020.
#Original link:

#Imports
import pygame
import os
from random import randint
from numpy import loadtxt

#Get local username
path = str(os.getlogin())

#Root file of chords-App folder. This allows later parts of the program to point to your specific root location.
root = "/Users/" + path + "/chords-App/"

#Opens chord info as readable text under the variable "lines".
text_file = open(root + "chordsdata.txt", "r")
lines = text_file.readlines()

#Lists
chord_list = []
img_list = []

#Main Function
def main():
    #Initialize Pygame
    pygame.font.init()

    #Load logo & app name
    logo = pygame.image.load(root + "logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Chords!")

    #Create 240 x 180 surface (background)
    screen = pygame.display.set_mode((500,400))
    screen.fill((255,255,255))

    #Define variable to control main loop
    running = True

    #x and y positions
    xpos1 = 50
    ypos1 = 100

    xpos2 = 325
    ypos2 = 100

    xpos3 = 200
    ypos3 = 300

    #Incorporate default font
    myfont = pygame.font.SysFont(None, 30)

    #Load images from "lines" into lists from line 20
    for i in range(0,len(lines)):
        [note,png,placeholder]=lines[i].split("/") #dependent on chordsdata.txt
        chord_list.append(str(note))
        img_list.append(str(png))

    #Randomly generate some integer based on amount of chords inmported
    int1 = randint(0,len(chord_list)-1)
    #Determine what chord to play based upon random list index
    chord1 = root + "chords-Storage/" + str(img_list[int1])
    #Determine the name of the chord based upon random list index
    text1 = myfont.render(chord_list[int1], False, (0, 0, 0))

    int2 = randint(0,len(chord_list)-1)
    #Loop to assure that the two chords aren't the same
    if int2 == int1:
        while int2 == int1:
            int2 = randint(0,len(chord_list)-1)
    chord2 = root + "chords-Storage/" + str(img_list[int2])
    text2 = myfont.render(chord_list[int2], False, (0, 0, 0))

    #time variables (in seconds)
    t = 60
    dt = 1

    #main loop
    while running:
        #event handling
        for event in pygame.event.get():
            #only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                #exits the main loop
                running = False
        #font based upon how much of minute remains
        text3 = myfont.render(str(t), False, (0, 0, 0))
        #blit all images and texts onto the screen in their respective positions
        screen.fill((255,255,255))
        blit1 = pygame.image.load(chord1)
        screen.blit(blit1, (xpos1,ypos1))
        screen.blit(text1, (xpos1,ypos1+100))
        blit2 = pygame.image.load(chord2)
        screen.blit(blit2, (xpos2,ypos2))
        screen.blit(text2, (xpos2,ypos2+100))
        screen.blit(text3, (xpos3,ypos3))
        #update screen
        pygame.display.flip()
        #delay for 1000ms before changing time
        pygame.time.delay(1000)
        t -= dt
        #reset time loop
        if t == 0:
            #redefine time
            t = 60
            #redefine int 1 as previous int 2/info
            int1 = int2
            chord1 = root + "chords-Storage/" + str(img_list[int1])
            text1 = myfont.render(chord_list[int1], False, (0, 0, 0))
            #regenerate int 2/info
            int2 = randint(0,len(chord_list)-1)
            if int2 == int1:
                while int2 == int1:
                    int2 = randint(0,len(chord_list)-1)
            chord2 = root + "chords-Storage/" + str(img_list[int2])
            text2 = myfont.render(chord_list[int2], False, (0, 0, 0))




#run function only if designated as the main script...
if __name__=="__main__":
    main()
