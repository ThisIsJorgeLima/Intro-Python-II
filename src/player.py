# Write a class to hold player information, e.g. what room they are in
# currently."""
"""
Import Statments:
"""
from item import Item

item = {
    'journal': Item("Journal", "A notebook containing a series of maps and renders of THE AMBER ROOM documented by a Dr. Perkins."),

    'bullwhip': Item("Bullwhip",
                     "No. 455 10 ft. Bull Whip."),
    'flame torch': Item("Flame Torch", "Wrapped in cloth around the end of a stick that ignites the darkness")
}


class Player():
    ''' A player class with name, current room'''

    def __init__(self, name, current_room):
        ''' Constructor'''

        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name} is at the {self.current_room}'

    def add_item(self, item):
        self.inventory.append(item)
        print(f"\n{item.name} was added to {self.name}'s inventory.")

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"\n{item.name} was removed from {self.name}'s inventory.")

    def items_in_inventory(self):
        message = ''
        if self.inventory:
            for i in self.inventory:
                message += f'{i.name}, '
            return message.rstrip(', ')

        else:
            return 'nothing'


if __name__ == '__main__':
    player = Player(name='Jorge', current_room='Outside')
    bullwhip = item['Bullwhip']
    player.add_item(Bullwhip)
    print(player.inventory[0].name)
    player.drop_item(bullwhip)
    print(player.inventory)
