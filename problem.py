from node import Node

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
        row, col = None 

        for r in range(n):
            for c in range(n):
                if state[r][c] == 0:
                    row, col = r, c
                    break
            if row is not None:
                break

        new_state = [row[:] for row in state]
        
        if operator == "UP" and row > 0:
            new_state[row][col] = new_state[row - 1][col]
            new_state[row-1][col] = 0

        if operator == "DOWN" and row < n - 1:
            new_state[row][col] = new_state[row + 1][col]
            new_state[row + 1][col] = 0

        if operator == "LEFT" and col > 0: 
            new_state[row][col] = new_state[row][col - 1]
            new_state[row][col - 1] = 0 

        if operator == "RIGHT" and col < n - 1:
            new_state[row][col] = new_state[row][col + 1]
            new_state[row][col + 1] = 0
        
        return new_state
    
    def heuristic_check():
