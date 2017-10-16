"""
1= up
2= down
3= left
4= right
"""

#load modules
from sense_emu import SenseHat
sense = SenseHat()

from time import sleep
from evdev import InputDevice, ecodes, list_devices
from select import select
from random import randint

#from functions import to_do

#functions
def to_do(level):#angeben was gedrückt werden soll
    counter=1
    array=[i for i in range(level)]

    while(counter <= level):
        array[counter-1] = randint(1, 4)

        if array[counter-1] == 1:
            sense.load_image("up.png", redraw = True)

        elif array[counter-1] == 2:
            sense.load_image("down.png", redraw = True)

        elif array[counter-1] == 3:
            sense.load_image("left.png", redraw = True)

        elif array[counter-1] == 4:
            sense.load_image("right.png", redraw = True)

        sleep(1)
        sense.clear()
        sleep(1)
        counter = counter + 1

    return array



def players_turn(array):
    win = True
    step = 1

    while win == True and step <= level:

        richtung = 0
        step_taken = False
        while step_taken == False:
            for event in sense.stick.get_events():
                if event.action == "pressed":

                    if event.direction == "up":
                        richtung = 1
                        step_taken = True
                        sense.load_image("up.png", redraw = True)
                        sleep(1)
                        sense.clear()

                    elif event.direction == "down":
                        richtung = 2
                        step_taken = True
                        sense.load_image("down.png", redraw = True)
                        sleep(1)
                        sense.clear()

                    elif event.direction == "left":
                        richtung = 3
                        step_taken = True
                        sense.load_image("left.png", redraw = True)
                        sleep (1)
                        sense.clear()

                    elif event.direction == "right":
                        richtung = 4
                        step_taken = True
                        sense.load_image("right.png", redraw = True)
                        sleep(1)
                        sense.clear()

        if richtung == array[step-1]:
            step = step + 1
        else:
            win = False

    return win



#initialize variables
game_started = 0
level=1

# mainloop

sense.clear()

while True:
    while game_started == False:            #show a message before the game starts

        #press button to start
        sense.load_image("press_start.png", redraw=True)
        for event in sense.stick.get_events():
            if event.action == "released":
                game_started = True


    sense.show_message("lvl " + str(level))

    trythis = to_do(level)
    win = players_turn(trythis)

    if win == True:
        sense.load_image("correct.png", redraw=True)
        sleep(1)
        level = level + 1

    else:
        sense.load_image("wrong.png", redraw=True)
        sleep(1)
        sense.show_message("Game over")
        game_started = False
        level = 1
