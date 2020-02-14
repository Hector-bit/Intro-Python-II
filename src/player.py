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
        else:
            print(self.inventory)
    #function look will find items in the room
    def look(self, room):
        if len(self.current_room.item) != 0:
            print(f'You found a {self.current_room.item[0]} in the {self.current_room.name}')
        else:
            print('Nothing was found in this room')
    #pick up item will need to know which room it is in
    #order to see if there is an item available to pick up
    def pick_up_item(self, room):
        picking_up = input("What item would you like to pick up: ")
        print(self.current_room.item, 'item of room')
        if picking_up == self.current_room.item[0]:
            self.inventory.insert(0, self.current_room.item[0])
            player_grab = self.current_room.item.copy()
            self.current_room.item.remove(player_grab[0]) 
            print(f"You picked it up")
        else:
            print('That item does not appear to be here')
    def drop_item(self, room):
        print('does nothing up')