# name: Jorge Lima
# date: 2020-05-06
# description: Ward-Perkins and the search of The Lost Amber Room

"""
Import Statements:
"""
import random
import time
from room import Room
from player import Player


def displayIntro():
    print("An archaeologist, Ward-Perkins, sets out to rescue his father, ")
    print("an artist who vanished while in search of THE AMBER ROOM,")
    print("you have to follow clues from his father's journal, which was left behind. ")
    print("You come to crossroads on your trip to Saint Petersburg,")
    print("leading to several paths.")
    print("One of the paths leads you to the hidden treasure,")
    print("it was sometimes called the Eighth Wonder of the World.")
    print("And the other leads may lead you to the kidnappers... ")

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

print('Ward-Perkins and the search of The Lost Amber Room')
name = input("Enter Player Name: ")
player = Player(name=name, current_room=room['outside'])
# if player doesn't add a name, user Player 1:
if name == "":
    name = "Ready Player One"

print(f'Welcome, {name}!')

displayIntro()
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


# def choosePath():
#     path = ""
#     while path != "q":  # input validation
#         path = input("Which path will you choose? ('n', 's', 'e', 'w'): ")
#         commands = ['n', 's', 'e', 'w', 'i', 'Item'',Quit', 'q', ]
#
#     print(f"""Welcome {player.name}! You find yourself at the {room['outside'].name}.
# {room['outside'].description}""")
#

while True:

    selection = input(
        """
Please select a direction to advance:
n, s, e, w, q
--> """
    )

    if selection == 'q':
        print(f'Uh oh! Youve been kidnapped, {player.name}!')
        break

    try:
        """ Cast input as a string"""
        selection = str(selection)

        # print(player.current_room.__dict__)

        if selection in ('n', 's', 'e', 'w'):
            if f'{selection}_to' in player.current_room.__dict__:
                player.current_room = getattr(player.current_room, f'{selection}_to')
                print(f'\nYou find yourself at the {player.current_room}')
            else:
                print("\nThat isn't a valid input; Please select the following:")

        else:
            print("\nThat isn't a valid input; Please select the following:")

    except TypeError:
        print('Please reenter one of these alternatives: n, s, e, w, q')
