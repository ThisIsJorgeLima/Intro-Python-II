# Implement a class to hold room information. This should have name and
# description attributes.

"""
Import Statements:
"""
from item import Item

item = {
    'journal': Item("Journal", "A notebook containing a series of maps and renders of THE AMBER ROOM documented by a Dr. Perkins."),

    'bullwhip': Item("Bullwhip",
                     "No. 455 10 ft. Bull Whip."),
    'flame torch': Item("Flame Torch", "Wrapped in cloth around the end of a stick that ignites the darkness")
}


class Room():
    ''' A room class that a player can interact with'''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []

    def __str__(self):
        return f'{self.name}.\n{self.description}'

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def items_in_room(self):
        message = ''
        if self.inventory:
            for i in self.inventory:
                message += f'{i.name}, '
            return message.rstrip(', ')

        else:
            return 'nothing'


if __name__ == '__main__':
    room = Room("Outside Cave Entrance",
                "North of you, the cave mouth beckons...")
    bullwhip = item['bullwhip']
    room.add_item(bullwhip)
    print(room.inventory)
    room.remove_item(bullwhip)
    print(room.inventory)
