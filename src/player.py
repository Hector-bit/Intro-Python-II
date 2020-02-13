# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You can't move in that direction")
    #the inventory function will list out how items are on the player
    def inventory_check(self):
        if len(self.inventory) == 0:
            print('You do not have any items in your inventory')
    #function look will find items in the room
    def look(self, room):
        if self.current_room.item != None:
            print(f'You found a {self.current_room.item} in the {self.current_room.name}')
        else:
            print('Nothing was found in this room')
    #pick up item will need to know which room it is in
    #order to see if there is an item available to pick up
    def pick_up_item(self, room):
        picking_up = input("What item would you like to pick up: ").lower()
        if picking_up == self.current_room.item.lower():
            push self.current_room.item 
            print(f"You picked up the {self.current_room.item}")
        else:
            print('That item does not appear to be here')