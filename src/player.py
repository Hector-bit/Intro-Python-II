# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You can't move in that direction")
    #pick up item will need to know which room it is in
    #order to see if there is an item available to pick up
    def pick_up_item(self, room):
        print('nothing here yet')