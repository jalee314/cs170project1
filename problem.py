from node import Node
import math

'''
Problem Class:
Initial State: Parameter that accepts 2D matrix of whatever initial state your feeble mind desires
Goal State is always just gonna be the puzzle in order
There are only 4 possible operators here
Type will correlate to which heuristic we're using 0 -> uniform, 1 -> misplaced, 2 -> euclidean
'''


class Problem:
    def __init__(self, initial_state, heuristic):
        self.initial_state = Node(initial_state) 
        self.goal_state = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]] #star in this context represented by 0.
        self.operators = ["UP", "DOWN", "LEFT", "RIGHT"]
        self.heuristic = heuristic
    
    def check_goal(self, state):
        return state == self.goal_state
    
    def move(self, state, operator, n):
        row, col = None #set row and column pointers to none 

        for r in range(n): #traverse through the current puzzle and find where the star currently is 
            for c in range(n):
                if state[r][c] == 0:
                    row, col = r, c
                    break
            if row is not None: #check only one, if one is none so is the other 
                break

        new_state = [row[:] for row in state] #deep copy a new matrix into a deep matrix. 
        
        if operator == "UP" and row > 0: #top row all have row index 0, can't be any less than that if trying to switch a piece up
            new_state[row][col] = new_state[row - 1][col]
            new_state[row-1][col] = 0

        elif operator == "DOWN" and row < n - 1: #bottom row all have row index n - 1, can't be any more than that if trying to switch a piece down
            new_state[row][col] = new_state[row + 1][col]
            new_state[row + 1][col] = 0

        elif operator == "LEFT" and col > 0: #left col all have col index 0, can't be any less if trying to swtich a piece left
            new_state[row][col] = new_state[row][col - 1]
            new_state[row][col - 1] = 0 

        elif operator == "RIGHT" and col < n - 1: #right col all have col index n - 1, can't be any less than that if tryint o switch a piece down 
            new_state[row][col] = new_state[row][col + 1]
            new_state[row][col + 1] = 0
        else:
            return None #if none of those conditions are met, state is invalid, and returned as null pointer 

        return new_state #return new puzzle state with swapped pieces 
    
    def apply_operators(self, node):
        n = len(node.state) #take length of node state since this puzzle can be dynamically sized if we choose to
        node_branches = [] #create a list to store all possible legal state branches

        for choice in self.operators: #iterate through each possible operator and see if we get a valid state
            new_state = self.move(node.state, choice, n) 
            if new_state is not None: #valid state check
                child_node = Node( #create a child node for each legal branch with appropriate attributes updated
                    state = new_state,
                    g = node.g + 1,
                    h = 0,
                    move = choice,
                    parent = node,
                    depth = node.depth + 1
                )
                self.calculate_heuristic(child_node) 
                node_branches.append(child_node)
         
        return node_branches
     
    
    def calculate_heuristic(self, node): 
        h = 0
        if self.type == 1: #misplaced
             n = len(node.state)

             for row in range(n):
                 for col in range(n):
                     if node.state[row][col] != self.goal_state[row][col] and node.state[row][col] != 0:
                         h += 1

        if self.type == 2: #euclidean
            n = len(node.state)
            goal_state_tile = {}

            for row in range(n):
                for col in range(n):
                    goal_state_tile[self.goal_state[row][col]] = (row, col) 

            for row in range(n):
                for col in range(n):
                    curr_state_tile = node.state[row][col] #
                    if curr_state_tile != 0:
                        goal_state_tile_row, goal_state_tile_col = goal_state_tile[curr_state_tile]

                        dist = math.sqrt(pow((goal_state_tile_row - row), 2) + pow(goal_state_tile_col - col, 2))
                        h += dist

        else: #uniform cost heuristic
            pass #don't need to do anything for uniform cost since h = 0  

        node.change_cost(node.g, h)

    def search(self):
        frontier = queue.
        
