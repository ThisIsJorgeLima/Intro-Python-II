# name: Jorge Lima
# date: 2020-05-07
# description: Ward-Perkins and the search of The Lost Amber Room

"""
Import Statements:
"""
from room import Room
from player import Player
from item import Item

# Utility func clears screen for graphics
# include <windows.h>
# include <linux + Mac>
from utils import clear_terminal


# Display intro


def displayIntro():
    print("An archaeologist, Ward-Perkins, sets out to rescue his father, ")
    print("an artist who vanished while in search of THE AMBER ROOM,")
    print("you have to follow clues from his father's journal, which was left behind. ")
    print("You come to crossroads on your trip to Saint Petersburg,")
    print("leading to several paths.")
    print("One of the paths leads you to the hidden treasure,")
    print("it was sometimes called the Eighth Wonder of the World.")
    print("And the other leads may lead you to the kidnappers... ")


# Declare items
item = {
    'journal': Item("Journal",
                    """A notebook containing a series of maps and renders of THE AMBER RROM
    documented by a Dr. Perkins."""),

    'bullwhip': Item("Bullwhip",
                     """No. 455 10 ft. Bull Whip."""),
    'flame torch': Item("Flame Torch", """Wrapped in cloth around the end of a stick""")
}


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
# Clears screen for opening logo for the game:
clear_terminal()

print("""

████████╗██╗░░██╗███████╗  ██╗░░░░░░█████╗░░██████╗████████╗
╚══██╔══╝██║░░██║██╔════╝  ██║░░░░░██╔══██╗██╔════╝╚══██╔══╝
░░░██║░░░███████║█████╗░░  ██║░░░░░██║░░██║╚█████╗░░░░██║░░░
░░░██║░░░██╔══██║██╔══╝░░  ██║░░░░░██║░░██║░╚═══██╗░░░██║░░░
░░░██║░░░██║░░██║███████╗  ███████╗╚█████╔╝██████╔╝░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝░╚════╝░╚═════╝░░░░╚═╝░░░

░█████╗░███╗░░░███╗██████╗░███████╗██████╗░  ██████╗░░█████╗░░█████╗░███╗░░░███╗
██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗████╗░████║
███████║██╔████╔██║██████╦╝█████╗░░██████╔╝  ██████╔╝██║░░██║██║░░██║██╔████╔██║
██╔══██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
██║░░██║██║░╚═╝░██║██████╦╝███████╗██║░░██║  ██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝

                           𝗖𝗢𝗣𝗬𝗥𝗜𝗚𝗛𝗧 𝟮𝟬𝟮𝟬 𝗝𝗥𝗚𝗟.𝗜𝗠 """
      )

# Make a new player object that is currently in the 'outside' room.
name = input("Enter Player Name: ")
player = Player(name=name, current_room=room['outside'])
# if player doesn't add a name, user Player 1:
if name == "":
    name = "Ready Player One"

print(f'Welcome, {name}!')

# displayIntro()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

location = f"""\nYou find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground."""
# Make a new player object that is currently in the 'outside' room.

# clear_terminal()
displayIntro()
print(f'Welcome, {name}!')

# Welcoming Player
print(
    f"""Welcome, {player.name}! You find yourself at the {player.current_room}"""
)

while True:

    selection = input(
        """
Please select a passage, course of action, or select item from your inventory:
North (n), South (s), East (e), West (w), Quit (q)
Select item (take [name]) Drop item(drop [name])
View Inventory(i)
--> """
    )

    if selection == 'q':
        clear_terminal()
        print(f' 𝐔𝐡 𝐨𝐡❗ 𝐘𝐨𝐮𝐯𝐞 𝐛𝐞𝐞𝐧 𝐤𝐢𝐝𝐧𝐚𝐩𝐩𝐞𝐝, {player.name}❗')
        break
    selection = selection.strip().split()
    if selection[0] in ('n', 's', 'e', 'w', 'q'):
        clear_terminal()

        if hasattr(player.current_room, f'{selection[0]}_to'):
            player.current_room = getattr(player.current_room, f'{selection[0]}_to')
            print(player)

    elif selection[0] in ('take'):
        clear_terminal()
        for item in player.current_room.inventory:
            if selection[1] in item.name:
                player.add_item(item)
                player.current_room.remove_item(item)
                print(f"""You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")

            else:
                print(f'\n{selection[1]} not in room.')
                print(f"""You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")

    elif selection[0] in ('drop', 'd'):
        clear_terminal()
        for item in player.inventory:
            if selection[1] in item.name:
                player.drop_item(item)
                player.current_room.add_item(item)
                print(f"""You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")

            else:
                clear_terminal()
                print(f'\n{selection[1]} not in inventory')
                print(f"""You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")

    elif selection[0] in ('i', 'inventory'):
        clear_terminal()
        print(f"\n{player.name}'s inventory:\n{player.items_in_inventory()}")

    else:
        clear_terminal()
        print(f"""That is not a valid command\n
You find yourself at the {player.current_room}
There is {player.current_room.items_in_room()} on the ground.""")
