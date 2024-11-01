from problem import Problem
from node import Node 

def main():
    print("Welcome to Jason Lee's (862249342) 8 puzzle solver.\nType \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n")
    choice = int(input(""))

    if choice == 1: 
        puzzle = [[1, 2, 3],
                  [4, 0, 5],
                  [6, 7, 8]]
    else:
        puzzle = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]

    print("\nEnter your choice of algorithm\n1)Uniform Cost Search\n2)A* w/ Misplaced Tile Heuristic\n3)A* w/ Euclidean distance Heuristic\n")
    choice = int(input(""))
    problem = Problem(puzzle, choice)
    goal_node, nodes_searched, max_nodes = problem.search()

    if goal_node:
        solution_path = []
        curr_node = goal_node
        while(curr_node):
            solution_path.append(curr_node)
            curr_node = curr_node.parent
        solution_path.reverse()

        if solution_path[0].state != goal_node.state:
            print("\nExpanding State\n")
            for row in solution_path[0].state:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
            print("Expanding this node...\n")

            for node in solution_path[1:]:
                print(f"The best state to expand with g(n) = {node.g} and h(n) = {node.h}")
                for row in node.state:
                    print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
                if(node.state == goal_node.state):
                    print("\nGOAL!!!!\n")
                    break
                print("\nExpanding this node...\n")
        else:
            print("\nExpanding State\n")
            for row in solution_path[0].state:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))   
            print("\nGOAL!!!!\n")

    print(f"To solve this problem the search algorithm expanded a total of {nodes_searched} nodes.\nThe maximum number of nodes in the queue at one time was {max_nodes}.\nThe depth of the goal node was {goal_node.depth}\n")

    print(f"Correct sequence of Actions:\n")
    for node in solution_path:
        for row in node.state:
            print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
        print(f"\nAction Taken: {node.move}\n")    
        if node.state == goal_node.state:
            print("Finished\n")        
    
if __name__ == "__main__":
    main()