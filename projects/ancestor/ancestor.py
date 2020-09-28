
import sys
import os
myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
if(sys.path.__contains__(parentDir)):
    pass
else:
    sys.path.append(parentDir)

from graph.graph import Graph

def find_farthest(tree, vertex, distance=None):
    if distance is None:
        if len(tree.get_neighbors(vertex)) == 0:
            return -1
        else:
            distance = 0
    oldest = (vertex, distance)
    for ancestor in tree.vertices[vertex]:
        pair = find_farthest(tree, ancestor, distance+1)
        if pair[1] > oldest[1]:
            oldest = pair
        if pair[1] == oldest[1]:
            if pair[0] < oldest[0]:
                oldest = pair
    return oldest


def earliest_ancestor(ancestors, starting_node):
    tree = Graph()
    for pairing in ancestors:
        tree.add_vertex(pairing[0])
        tree.add_vertex(pairing[1])
        tree.add_edge(pairing[1], pairing[0])
    result = find_farthest(tree, starting_node)
    if result == -1:
        return -1
    else:
        return result[0]
