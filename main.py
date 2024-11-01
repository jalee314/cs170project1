from problem import Problem
from node import Node 

def main():
    choice = input("Welcome to Jason Lee's (862249342) 8 puzzle solver.\nType \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n")

    if choice == 1: 
        puzzle = [[1, 0, 3],
                  [4, 2, 6],
                  [7, 5, 8]]
    else:
        puzzle = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]

    choice = input("\nEnter your choice of algorithm\n1)Uniform Cost Search\n2)A* w/ Misplaced Tile Heuristic\n3)A* w/ Euclidean distance Heuristic\n")

    problem = Problem(puzzle, choice)
    goal, nodes_searched, max_nodes, sol_trace = problem.search()
    
if __name__ == "__main__":
    main()