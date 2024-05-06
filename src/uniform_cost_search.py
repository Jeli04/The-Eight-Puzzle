import math
import heapq
import numpy as np
import sys
from n_puzzle import Node
from n_puzzle import puzzleProblem

sys.setrecursionlimit(1000000000)

class uniform_cost_search:
    def execute_ucs(self, game):
        
        heapq.heappush(game.frontier, (0, game.root))
        
        while game.frontier:
            pair = heapq.heappop(game.frontier)
            game.numOfExpandedNodes+=1
            print("Number of Expanded Nodes: ", game.numOfExpandedNodes)
            node = pair[1] # we actually want current!
            cur_cost = node.cost
            
            # mark current node as visited
            game.seen[game.toString(node)] = node

            # return current state if goal is found
            if game.isGoal(node):
                print("I'm the goal:")
                print(node.printPuzzle())
                print("Number of Expanded Nodes: ", game.numOfExpandedNodes)
                return game.seen
       

            # obtain child node from all 4 possible operators
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
            
                child_cost = child.parent.cost + 1
                visited = False
                
               
                puzzleString = game.toString(child)
                # if visited == False and puzzleString in game.seen and child_cost < cur_cost:
                #     if len(game.frontier) > 2: return
                #     visited = True
                #     seenNode = game.seen[puzzleString]
                #     seenNode.cost = child_cost
                #     seenNode.parent = node
                #     heapq.heappush(game.frontier, (child_cost, seenNode))
                #     del game.seen[puzzleString]
                #     game.maxQueueSize = max(game.maxQueueSize, len(game.frontier))
                # else:
                #     for pair in game.frontier:
                #         if np.array_equal(pair[1].n_puzzle, child.n_puzzle):
                #             visited = True
                #             if child_cost < cur_cost:
                #                 pair[1].cost = child_cost
                #                 pair[1].parent = node
                #                 break

                # # add into frontier if never seen yet
                # if visited == False:
                #     # print("push into heap")
                #     # print(puzzle.frontier)
                #     child.cost = child_cost         
                #     heapq.heappush(game.frontier, (child_cost, child))
                #     game.maxQueueSize = max(game.maxQueueSize, len(game.frontier))
                
                if puzzleString not in game.seen or child.cost < game.seen[puzzleString].cost:
                    heapq.heappush(game.frontier, (child.cost, child))
                    game.seen[puzzleString] = child
                    game.maxQueueSize = max(game.maxQueueSize, len(game.frontier))

            game.seen[game.toString(node)] = node

        return None

    