import numpy as np
import heapq

class Node:
    #Constructor for puzzle node
    def __init__(self, dim = 3, n_puzzle = None, parent = None) -> None:
        if dim == 3 and n_puzzle == None or dim > 3 and n_puzzle == None:
            self.dim = dim
            self.n_puzzle = np.arange(self.dim * self.dim)
            np.random.shuffle(self.n_puzzle)
            self.n_puzzle = self.n_puzzle.reshape(self.dim, self.dim)
        elif dim >= 3 and n_puzzle != None:
            self.dim = dim
            self.n_puzzle = n_puzzle
        elif dim < 3:
            raise ValueError("n_puzzle dimensions must be greater than 2")
        
        self.parent = parent #For A* star algorithm to keep trace of past heuristic values
        self.heuristic = 0
        self.cost = 0 
        self.totalCost = self.heuristic + self.cost   
            
    ##Prints the puzzle at the current state
    def printPuzzle(self):
        print(self.n_puzzle)

    ##Gets the index of the "blank" (for us 0) puzzle piece
    def getInitialStateIndex(self):
        return [np.where(self.n_puzzle == 0)[0][0], np.where(self.n_puzzle == 0)[1][0]]
        #I know this is bad, you don't have to tell me



class puzzleProblem:
    #contains the details of the problem
    #initialize frontier with the first initial state node
    def __init__(self, root) -> None:
        #the puzzle should know its initial and goal states
        self.root = root
        self.goalState = self.createGoalState(root.dim)
        self.frontier = []
        # a list of visited nodes 
        self.seen = set()
   
    #Aditi & Jon: implement priority queue
    def expandNode(node):
        # this function will figure out a list of all the valid next states that we can get
        # and order them by cost to add into frontier
        pass

    def isGoal(self) -> bool:
        return self.root == self.goalState

    def createGoalState(self, dim) -> np.matrix:
        return np.asmatrix(np.arange(dim * dim).reshape(dim, dim))
    
    def printGoalState(self):
        print(self.goalState)

    #Operators to change 0 -> {some index} to achieve goal state (Vaneeeeesha)
    def operator_go_left(self, currNode):
        new_node = currNode
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]
        print(f'Before left operation:\n{new_node.n_puzzle}\n')

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row - 1] = new_node.n_puzzle[currIndex_col, currIndex_row - 1], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1
        if (not(access_node in self.seen)):
            self.seen.add(access_node)

        print(f'After left operation:\n{new_node.n_puzzle}')

        return new_node

            
    
    def operator_go_right(self, currNode):
        new_node = currNode
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]
        print(f'Before right operation:\n{new_node.n_puzzle}\n')

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row + 1] = new_node.n_puzzle[currIndex_col, currIndex_row + 1], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1
        if (not(access_node in self.seen)):
            self.seen.add(access_node)

        print(f'After right operation:\n{new_node.n_puzzle}')

        return new_node

    def operator_go_up(self, currNode):
        new_node = currNode
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]
        print(f'Before up operation:\n{new_node.n_puzzle}\n')

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col - 1, currIndex_row] = new_node.n_puzzle[currIndex_col - 1, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1

        print(f'After up operation:\n{new_node.n_puzzle}')

        return new_node

    def operator_go_down(self, currNode):
        new_node = currNode
        access_node = currNode

        currIndex_col = new_node.getInitialStateIndex()[0]
        currIndex_row = new_node.getInitialStateIndex()[1]
        print(f'Before down operation:\n{new_node.n_puzzle}\n')

        new_node.n_puzzle[currIndex_col, currIndex_row], new_node.n_puzzle[currIndex_col + 1, currIndex_row] = new_node.n_puzzle[currIndex_col + 1, currIndex_row], new_node.n_puzzle[currIndex_col, currIndex_row]
        new_node.parent = access_node

        new_node.cost += 1
        if (not(access_node in self.seen)):
            self.seen.add(access_node)

        print(f'After down operation:\n{new_node.n_puzzle}')

        return new_node
    

new_node = Node(4)
print(new_node.getInitialStateIndex())
new_puzzle = puzzleProblem(new_node)
new_puzzle.operator_go_left(new_node)
new_puzzle.operator_go_right(new_node)
new_puzzle.operator_go_up(new_node)
new_puzzle.operator_go_down(new_node)
