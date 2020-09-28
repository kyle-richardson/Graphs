from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

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
# world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']


def reverse(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


def dft_recursive(graph, curr, prev = None, direction = None, visited = None, path = None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    exits = {}
    if curr in visited:
        return
    for d in curr.get_exits():
        exits[d]="?"
    graph[curr.name] = exits
    visited.add(curr)
    if prev is not None:
        path.append(direction)
        graph[prev.name][direction] = curr.name
        graph[curr.name][reverse(direction)] = prev.name
    for e in curr.get_exits():
        if graph[curr.name][e] =="?":
            if curr.get_room_in_direction(e) not in visited:
                dft_recursive(graph, curr.get_room_in_direction(e), curr, e, visited, path)
                path.append(reverse(e))

    return path

trav_graph = {}
traversal_path = dft_recursive(trav_graph,player.current_room)

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
    # unvisited = [room for room in room_graph if room not in visited_rooms]
    # print(unvisited)



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
