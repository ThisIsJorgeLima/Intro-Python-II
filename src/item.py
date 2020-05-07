class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        s = f"{self.name}\n"
        return s

    def __repr__(self):
        return f'Player({repr(self.name)})'

    def on_take(self):
        print(f"\n    You have picked up {self.name}: {self.description}")

    def on_drop(self):
        print(f"\n    You have dropped {self.name}: {self.description}")
