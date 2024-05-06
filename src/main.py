import numpy as np
from n_puzzle import Node
from n_puzzle import puzzleProblem
from a_star import a_star
from uniform_cost_search import uniform_cost_search

def calc_depth(puzzle, seen):
    if seen==None: return 0
    depth = 0
    curr_state = seen["123456780"] # goal
    while curr_state != puzzle.root:
        depth+=1
        print(curr_state.n_puzzle)
        curr_state = curr_state.parent

    return depth
    

def main():
    print("Welcome to N-Puzzle Solver")
    puzzleChoice = int(input("Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n"))
    
    if(puzzleChoice==1):
        initial = Node()
    if(puzzleChoice == 2):
        dim = int(input("Enter the dimension of your n x n puzzle. Ex. (3 x 3) puzzle, enter 3\n"))
        print("Enter your puzzle, use a zero to represent the blank")
        print("Enter your rows, use space or tabs between numbers 1 2 3")
        
        # Collect puzzle input as a list of list1s
        matrix_input = []
        for _ in range(dim):
            row = list(map(int, input().split()))
            matrix_input.append(row)
        
        # Convert the list of lists to a NumPy array
        matrix = np.asmatrix(np.array(matrix_input))
        
        initial = Node(dim=dim, n_puzzle=matrix)


        while (not initial.Solvable()):
            print("Puzzle not solvable, please re-enter your puzzle:\n")
            print("Enter your puzzle, use a zero to represent the blank")
            print("Enter your rows, use space or tabs between numbers 1 2 3")
            
            # Collect puzzle input as a list of list1s
            matrix_input = []
            for _ in range(dim):
                row = list(map(int, input().split()))
                matrix_input.append(row)
            
            # Convert the list of lists to a NumPy array
            matrix = np.array(matrix_input)
            
            initial = Node(dim=int(dim), n_puzzle=matrix)
        
    
    problem = puzzleProblem(initial)
    
    print("\n")
    print("Choose your searching algorithm: ")
    print("\n1 for Uniform Cost Search")
    print("2 for A* with the Misplaced Tile heuristic.")
    print("3 for A* with the Euclidean distance heuristic.")
    
    algo = int(input("Enter your choice of algorithm: "))
    print("\n")
    
    problem.expandNode(initial)
    
    if (algo == 1):
        print(f"Starting State:\n {initial.n_puzzle}")
        object = uniform_cost_search()
        output = object.execute_ucs(problem)
    elif (algo == 2):
        object = a_star()
        print(f"Starting State:\n {initial.n_puzzle}")
        output = object.call_a_star(problem, "misplaced")
    elif (algo == 3):
        print(f"Starting State:\n {initial.n_puzzle}")
        object = a_star()
        output = object.call_a_star(problem, "euclidean")
    
    print("Nodes expanded: ", problem.numOfExpandedNodes)
    print("Max queue size: ", problem.maxQueueSize)
    print("Depth: ", calc_depth(problem, output))

if __name__ == '__main__':
    main()