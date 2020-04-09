from pygame_functions import *


def makeScreen():
    screenSize(900,990)
    setBackgroundImage("background.PNG")
    title = makeLabel("Welcome to Simon", 48,10,10,"white", font="Impact")
    showLabel(title)
    roundLabel = makeLabel("", 48,10,850,"white", font="Impact")
    showLabel(roundLabel)
    red = makeSprite("red.png")
    moveSprite(red,450,280,centre=True)
    showSprite(red)
    orange = makeSprite("orange.png")
    moveSprite(orange,230,500,centre=True)
    showSprite(orange)

    green = makeSprite("green.png")
    moveSprite(green,450,720,centre=True)
    showSprite(green)

    blue = makeSprite("blue.png")
    moveSprite(blue,670,500,centre=True)
    showSprite(blue)
    TONE1 = makeSound("TONE1.wav")
    TONE2 = makeSound("TONE2.wav")
    TONE3 = makeSound("TONE3.wav")
    TONE4 = makeSound("TONE4.wav")
    return red, green, blue, orange, roundLabel, TONE1, TONE2, TONE3, TONE4



def drawBlankCircles():
    drawEllipse(450,280,300,300,"grey",linewidth=0)
    drawEllipse(450,720,300,300,"grey",linewidth=0)
    drawEllipse(230,500,300,300,"grey",linewidth=0)
    drawEllipse(670,500,300,300,"grey",linewidth=0)

def lightColour(colour):
    tones = {red:TONE1, orange:TONE2, blue:TONE3, green:TONE4}
    showSprite(colour)
    playSoundAndWait(tones[colour])
    hideSprite(colour)

def getClicked():
     while True:
            if mousePressed():
                if spriteClicked(red):
                    lightColour(red)
                    return red
                if spriteClicked(blue):
                    lightColour(blue)
                    return blue
                if spriteClicked(orange):
                    lightColour(orange)
                    return orange
                if spriteClicked(green):
                    lightColour(green)
                    return green
            pause(10)

def playGame():
    round = 0
    pattern = []
    hideSprite(red)
    hideSprite(green)
    hideSprite(blue)
    hideSprite(orange)
    while True:
        round +=1
        changeLabel(roundLabel, "Round " + str(round))
        # Add a random colour to the pattern
        pattern.append(red)
        # Play the pattern (use lightColour() to light the button and play the tone)

        # Start getting inputs from the player
        # eg: a loop which gets the next input...
        colourClicked = getClicked()
        # ...and compares it with the next colour in the pattern
        # keep doing this as long as it matches the pattern.

        # if they make a mistake, end the game (break out of this loop)
        # if they make it to the end of the pattern without making a mistake,
        # allow this loop to repeat, for the next round


red, green, blue, orange, roundLabel, TONE1, TONE2, TONE3, TONE4 = makeScreen()
playGame()

endWait()