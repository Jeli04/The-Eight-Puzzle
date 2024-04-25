import heapq

class Tile:
    def __init__(self, num, cost, heuristic):
        self.num = num  # Number of the tile
        self.cost = cost
        self.heuristic = heuristic #0
–
def uniform_cost_search(matrix) -> string:
    Node = initial state
    cost = 0
    
    heapq pq()
    pq.heappush(node)
    seen = set() #empty to start
    
    while (pq):
        if (pq.is_empty):
            return "No solution"
        
        curNode = pq.top()
        pq.pop()
        
        if isGoal(curNode):
            return "Solution found"
        
        seen.add(curNode)
        
        for (every operator in Operators):
            
    
    
# string uniformCostSearch(vector<vector<int>> puzzle) {
    # priority_queue<Node*, vector<Node*>, compFunction> pq;
    # pq.push(some node);

    # int cost = 0;
    # unordered_set<string> seen; //empty
# }