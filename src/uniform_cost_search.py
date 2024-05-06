import heapq
import numpy as np
import sys
from n_puzzle import Node
from n_puzzle import puzzleProblem

sys.setrecursionlimit(1000000000)

class uniform_cost_search:
    def execute_ucs(self, game):
        
        # add root to frontier
        heapq.heappush(game.frontier, (0, game.root))
        
        # iterate until the frontier is empty
        while game.frontier:
            # pop the cheapest cost node from frontier
            pair = heapq.heappop(game.frontier)
            game.numOfExpandedNodes+=1
            print("Number of Expanded Nodes: ", game.numOfExpandedNodes)
            node = pair[1] # pair[1] is the game puzzle
            
            # mark current node as visited
            game.seen[game.toString(node)] = node

            # return current state if goal is found
            if game.isGoal(node):
                print("I'm the goal:")
                print(node.printPuzzle())
                print("Number of Expanded Nodes: ", game.numOfExpandedNodes)
                return game.seen
       

            # obtain child node from all possible operators, and expanding tree
            for action in game.expandNode(node):
                child = None
                
                if action == "right":
                    print("right")
                    child = game.operator_go_right(node)
                elif action == "left":
                    child = game.operator_go_left(node)
                    print("left")
                elif action == "up":
                    child = game.operator_go_up(node)
                    print("up")
                elif action == "down":
                    child = game.operator_go_down(node)
                    print("down")
                
                # get puzzleString to store hash in seen
                puzzleString = game.toString(child)
               
               # only add child to frontier if not in seen or child cost is cheaper
                if puzzleString not in game.seen or child.cost < game.seen[puzzleString].cost:
                    heapq.heappush(game.frontier, (child.cost, child))
                    game.seen[puzzleString] = child
                    game.maxQueueSize = max(game.maxQueueSize, len(game.frontier))

            game.seen[game.toString(node)] = node

        return None
