from problem import Problem
from node import Node 
from preset import *

def main():
    print("\n\n\nWelcome to Jason Lee's (862249342) 8 puzzle solver.\nType \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n(Type 3 for a choice of puzzles)")
    choice = int(input(""))

    if choice == 1: 
        puzzle = [[1, 0, 3],                                                                        #default puzzle from pdf 
                  [4, 2, 6],
                  [7, 5, 8]]
    elif choice == 3:
        print("Choices:\n\n1)Trivial")
        for row in trivial:                                                                         #for loop to generate clean output w/ help of chatgpt
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
        print("\n2)Very easy")
        for row in very_easy:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
        print("\n3)Easy")
        for row in easy:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
        print("\n4)Doable")
        for row in doable:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))                
        print("\n5)Oh boy")
        for row in oh_boy:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
        print("\n6)Impossible")
        for row in impossible:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
    
        choice = int(input("\n"))
        
        if choice == 1:
            puzzle = trivial
        elif choice == 2: 
            puzzle = very_easy
        elif choice == 3: 
            puzzle = easy
        elif choice == 4:
            puzzle = doable
        elif choice == 5:
            puzzle = oh_boy
        elif choice == 6:
            puzzle = impossible
    
    elif choice == 2:
        print("Enter your puzzle, using a zero to represent the blank\n")
        row1 = input("Enter the first row, use spaces between numbers: ")
        row2 = input("Enter the second row, use spaces between numbers: ")
        row3 = input("Enter the third row, use spaces between numbers: ")

        puzzle = [list(map(int, row1.split())),
                  list(map(int, row2.split())),
                  list(map(int, row3.split()))
                 ]
    else:
        print("Not a valid number. Will close now.\n")
        return

    print("\nEnter your choice of search\n1)Uniform Cost Search\n2)A* w/ Misplaced Tile Heuristic\n3)A* w/ Euclidean distance Heuristic\n")
    choice = int(input("Choice: "))
   
    if choice > 3 or choice < 1:
        print("Not a valid number. Will close now\n")
        return
    
    problem = Problem(puzzle, choice)
    goal_node, nodes_searched, max_nodes = problem.search()

    if goal_node:                                                                                       #loop won't run if goal state not found
        solution_path = []                                                                              #start from goal node and iterate way back to the starting node
        curr_node = goal_node
        while(curr_node):
            solution_path.append(curr_node)
            curr_node = curr_node.parent
        solution_path.reverse()                                                                         #reverse the list to get the proper trace

        if solution_path[0].state != goal_node.state:
            print("\nExpanding State\n")
            for row in solution_path[0].state:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
            print("Expanding this node...\n")

            for node in solution_path[1:]:
                print(f"The best state to expand with g(n) = {node.g} and h(n) = {node.h}")
                for row in node.state:
                    print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
                if(node.state == goal_node.state):                                                      #stop loop once we print out the goal state
                    print("\nGOAL!!!!\n")
                    break
                print("\nExpanding this node...\n")
        else:
            print("\nExpanding State\n")
            for row in solution_path[0].state:
                print(" ".join(str(tile) if tile != 0 else "0" for tile in row))   
            print("\nGOAL!!!!\n")

    print(f"To solve this problem the search algorithm expanded a total of {nodes_searched} nodes.\nThe maximum number of nodes in the queue at one time was {max_nodes}.\nThe depth of the goal node was {goal_node.depth}\n")

    print(f"Correct sequence of Actions:\n")                                                            #essentially what we did before, but we print out the operator used
    for node in solution_path:
        for row in node.state:
            print(" ".join(str(tile) if tile != 0 else "0" for tile in row))
        print(f"\nAction Taken: {node.move}\n")    
        if node.state == goal_node.state:
            print("Finished\n")        
    
if __name__ == "__main__":
    main()