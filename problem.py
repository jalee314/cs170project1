import node.py

'''
Problem Class:
Initial State: Parameter that accepts 2D matrix of whatever initial state your feeble mind desires
Goal State is always just gonna be the puzzle in order
There are only 4 possible operators here
'''


class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]] #star in this context represented by 0.
        self.operators = ["UP", "DOWN", "LEFT", "RIGHT"]
    
    def check_goal(self, state):
        return state == self.goal_state
    
    def move(self, state, operator, n):
        row, col = 0 

        for r in range(n):
            for c in range(n):
                if state[r][c] == 0:
                    row, col = r, c
                    
        new_state = [row[:] for row in state]
        

        return 
