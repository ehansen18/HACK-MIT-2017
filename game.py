import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255, 255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)
car_width = 73

#sets screen size
gameDisplay = pygame.display.set_mode((display_width,display_height))
#displays game name
pygame.display.set_caption('Race Game')
#this creates the clock for throughout the game
clock = pygame.time.Clock()

carImg = pygame.image.load('nemo-icon.png')

def quitgame():
    pygame.quit()
    quit()


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

###########################################
#this creates the object (that will later fly)
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
###########################################

def car(x,y):
    gameDisplay.blit(carImg,(x,y))


def text_objects(text, font):
    textSurfacae = font.render(text, True, black)
    return textSurfacae, textSurfacae.get_rect()

def message_display(text):
    # this method describes the size of the font and here is where you choose the type of font
    sizeText = pygame.font.Font('freesansbold.ttf', 25)
    TextSurf, TextRect = text_objects(text, sizeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()


def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

#this creates the buttons, and also makes it so when you click on the green button, it changes colors
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, bright_green,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("comicsanms", 15)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        gameDisplay.blit(textSurf, textRect)

def crash():
    message_display('Your adventure has lead to your untimely demise.')

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        sizedText = pygame.font.SysFont('comicsansms',50)
        TextSurf, TextRect = text_objects('Begin your Adventure', sizedText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Begin",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)


        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
#####
    #this creates the object in a random space along with determining its speed
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1
    dodged = 0
#####
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            #allows the user to quit and leave the loop
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

    ###############################################
            #here are the key commands
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
    #############################################
        ## this code moves your car which is represented as x
        x += x_change
        gameDisplay.fill(white)

    ###########################################
        # things (thingx, thingy, thingw, thingh, color)
        things(thing_startx,thing_starty, thing_width, thing_height, black)

        #moves the object your character is trying to avoid
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

    ##########################################
        # this makes it so the car can't go off the screen without crashing
        if x > display_width - car_width or x <0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            #adds to the dodged count, and speeds up the object while making it wider as well
            dodged += 1
            thing_speed += 1
            thing_width += (dodged* 1.2)

    #################
            ###this code recognizes when the character has crashed
        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        #####
        #Displays a running update
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()


