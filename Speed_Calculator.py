
import random as rd
from time import *


def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def dealy(time_1, time_2, user_input):
    time_delay = time_2 - time_1
    time_r = round(time_delay, 2)
    speed = len(user_input) / time_r
    return round(speed)


while True:

    check = input('Press y to Start Programme n to Stop : ')
    if check =='y':


        paragraph = ['Oceanographers split the ocean into vertical and horizontal zones based on physical and biological',
                     "The pelagic zone is the open ocean's water column from the surface to the ocean floor",
                     'The water column is further divided into zones based on depth and the amount of light present',
                     'Human activity has a greater impact on the continental shelf',
                     'The continental shelf and coastal waters most affected by human activity are particularly vulnerable']

        test = rd.choice(paragraph)

        print('~~~~~~~~~~~~~~Typing Speed~~~~~~~~~~~~~')

        print(test)
        print()
        print()
        time_1 = time()
        user_input = input('Start Type Here : ')
        time_2 = time()

        print('Time Taken : ', dealy(time_1, time_2, user_input), 'w/s')
        print('Error : ', mistake(test, user_input))
    elif check == 'n':
        print('Programmed End')
        break
    else:
        print('Invalid Input')
