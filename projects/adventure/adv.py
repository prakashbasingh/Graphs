from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from utils import Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# list for current path
current_path = []
# list of reversed command to go backwards/opposite direction
opposite_direction = {"n": "s", "e": "w", "s": "n", "w": "e"}
# to hold the visited rooms
visited_rooms = set()
# stablishing a stack
stack = Stack()
# pushing current_room into stack
stack.push(player.current_room)

while stack.size() > 0:
    current_room = stack.pop()
    target_room = None
    last_moved_direction = None

    # setting current room as visited
    visited_rooms.add(current_room.id)

    # looping through the exits of the current room
    for exit in current_room.get_exits():
        # checking if each room that has exit leads is visited
        room_in_direction = current_room.get_room_in_direction(exit)
        # if id of room_in_directions not in visited room
        if room_in_direction.id not in visited_rooms:
            # set last moved direction as exit
            last_moved_direction = exit
            # and setting room in direction as terget room
            target_room = room_in_direction
    # if last moved direction is not none
    if last_moved_direction is not None:
        # append last moved direction to current path and traversal path
        current_path.append(last_moved_direction)
        traversal_path.append(last_moved_direction)

    # now setting current room as previous room
    prev_room = current_room
    # when target room is none and length of current path is more than 0
    while target_room is None and len(current_path) > 0:
        #remove current path and set as last direction
        last_direction = current_path.pop()
        #set last direction in opposite direction as go_back_direction
        go_back_direction = opposite_direction[last_direction]

                    #passing go back direction in get room in direction and setting as prev room
        prev_room = prev_room.get_room_in_direction(go_back_direction)
        traversal_path.append(go_back_direction)

        # now looping through the exit in prev_room
        for exit in prev_room.get_exits():
            # checking if each room that exit leads is visited
            room_in_direction = prev_room.get_room_in_direction(exit)

            # if room in direction is not in visited room
            if room_in_direction.id not in visited_rooms:
                # setting previous room as target room
                target_room = prev_room

    # if target room is not empty
    if target_room is not None:
        # push target room into stack
        stack.push(target_room)
    # else print the message
    else:
        print("there is no path to explore any more this way")    



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
