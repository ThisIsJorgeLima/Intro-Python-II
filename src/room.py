# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    """
    This defines the room class.
    Input: loc = name of the room
    description = infor about the location
    """

    def __init__(self, room_name, description, items=None):
        self.room_name = room_name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
