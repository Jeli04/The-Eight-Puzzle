import numpy as np
from n_puzzle import Node
from n_puzzle import puzzleProblem
from a_star import a_star

def main():
    print("Welcome to N-Puzzle Solver")
    puzzleChoice = int(input("Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n"))
    if(puzzleChoice==1):
        initial = Node()
        initial.printPuzzle()
    if(puzzleChoice == 2):
        dim = int(input("Enter the dimension of your n x n puzzle. Ex. (3 x 3) puzzle, enter 3\n"))
        print("Enter your puzzle, use a zero to represent the blank")
        print("Enter your rows, use space or tabs between numbers 1 2 3")
        
        # Collect puzzle input as a list of lists
        matrix_input = []
        for _ in range(dim):
            row = list(map(int, input().split()))
            matrix_input.append(row)
        
        # Convert the list of lists to a NumPy array
        matrix = np.array(matrix_input)
        
        initial = Node(dim=int(dim), n_puzzle=matrix)
        initial.printPuzzle()
    problem = puzzleProblem(initial)
    print("The location of the blank spot is: ")
    problem.expandNode(initial)
        

    print("1 for Uniform Cost Search")
    print("2 for A* with the Misplaced Tile heuristic.")
    print("3 for A* with the Euclidean distance heuristic")
    
    algo = int(input("Enter your choice of algorithm: ")) 
    

if __name__ == '__main__':
    main()