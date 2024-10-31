'''
Node Class:
State: Current configuration of the puzzle, represented by 2D matrix
g: Cost of reaching current node from starting node
h: Cost of heuristic, estimates cost to get to the goal
Move: Keeps track of what move was used to get to current state
parent: Points to the parent node if applicable, will allow me to trace through the final solution path

Default parameters are for starting node, every other node will get those values replaced in code 
'''

class Node:
    def __init__(self, state, g=0, h=0, move=None, parent=None, depth=0):
        self.state = state                      
        self.g = g
        self.h = h
        self.f = g + h
        self.move = move
        self.parent = parent
        self.depth = depth

    def change_cost(self, f, g, h):
        self.g = g
        self.h = h
        self.f = g + h



