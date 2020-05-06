# name: Jorge Lima
# date: 2020-05-06
# description: Adventure Game

"""
Import Statements:
"""
import random
import time
from room import Room


def displayIntro():
    print("An archaeologist Indy sets out to rescue his father, ")
    print("a medievalist who vansihed while in search of the Holy Grail")
    print("you have to follow clues from his father's journal")
    print("which was left behind.")
    print("you come to crossroads on your trip, leading to several paths.")
    print("One of the paths leads you to the hidden treasure!")
    print("and the other leads may lead you to the kidnappers ")
    print("You've lost the journal!")

# def choosePath():
#     path = ""
#     while path != "1" and path != "2":  # input validation
#         path = input("Which path will you choose? (1 or 2): ")
#
#     return path
#
#
# def checkPath(chosenPath):
#     print("You head down the path")
#     time.sleep(2)
#     print("there's an asteroid nearby that looks familar, that must be a good sign...")
#     print("But your skin begins to tingle...")
#     time.sleep(2)
#
#     correctPath = random.randint(1, 2)
#
#     if chosenPath == str(correctPath):
#         print("That tingling was just the feeling of admiration from")
#         print("the citizens of the galaxy!")
#         print("Welcome home!")
#     else:
#         print("Ax extremely enegetic burst of gamma rays pass through you")
#         print("casuing all of the atoms in your body to dissociate")
#         print("there is no record left to tingle...")
#         print()
#         # time.sleep()
#
#
# playAgain = "yes"
# while playAgain == "yes" or playAgain == "y":
#     displayIntro()
#     choice = choosePath()
#     checkPath(choice)  # choic is equal to "1" or "2"
#     playAgain = input("Do you want to play again? (yes or y to continue  playing): ")


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Enter Player Name: ")
# if player doesn't add a name, user Player 1:
if name == "":
    name = "Ready Player One"

print(f'Welcome, {name}!')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def choosePath():
    path = ""
    while path != "q":  # input validation
        path = input("Which path will you choose? ('n', 's', 'e', 'w'): ")
        commands = ['n', 's', 'e', 'w', 'i', 'Item'',Quit', 'q', ]
     # return path
     #
     #    print(f"\n You are currently in {player.room()}\n"}
     #    move = input("\nChoose your destination, {player.who}?".lower())
     #    if move == 'q':
     #        print("The treasure awaits. Play again soon!")
     #        exit()
