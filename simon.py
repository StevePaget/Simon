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
    orange = makeSprite("orange.png")
    moveSprite(orange,230,500,centre=True)
    green = makeSprite("green.png")
    moveSprite(green,450,720,centre=True)
    blue = makeSprite("blue.png")
    moveSprite(blue,670,500,centre=True)

    TONE1 = makeSound("TONE1.wav")
    TONE2 = makeSound("TONE2.wav")
    TONE3 = makeSound("TONE3.wav")
    TONE4 = makeSound("TONE4.wav")
    return red, green, blue, orange, roundLabel, TONE1, TONE2, TONE3, TONE4


def lightColour(colour):
    tones = {red:TONE1, orange:TONE2, blue:TONE3, green:TONE4}
    showSprite(colour)
    playSound(tones[colour])

def getClicked():
    value = None
    while not value:
            if mousePressed():
                for colour in (red, orange, green,blue):
                    if spriteClicked(colour):
                        lightColour(colour)
                        value = colour
                        break
            pause(10)
    while mousePressed():
        pause(10)
    hideAll()
    return value

def playGame():
    round = 0
    pattern = []
    while True:
        round +=1
        changeLabel(roundLabel, "Round " + str(round))
        # Add a random colour to the pattern
        pattern.append(red)  # change this so it's random
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