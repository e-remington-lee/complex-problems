from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for x, y, in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        leaves = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        nodes = n
        # you must know that the any tree has at most 2 centroid nodes, which have the min height, otherwise idfk
        while nodes > 2:
            size = len(leaves)
            for i in range(size):
                nodes -= 1
                current = leaves.popleft()
                child = graph[current].pop()
                graph[child].remove(current)
                if len(graph[child]) == 1:
                    leaves.append(child)
        return leaves


    # V(V+E), where V = n and edges = n-1 (valid trees have n-1 edges)
    def custom(self, n, edges):
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        for x, y, in edges:
            graph[x].append(y)
            graph[y].append(x)
        global_min = float('inf')
        min_dict = defaultdict(list)
        
        for root in range(n):
            count = 0
            queue = deque([root])
            recent_seen = defaultdict(lambda: False)
            while queue:
                size = len(queue)
                for _ in range(size):
                    current = queue.popleft()
                    recent_seen[current] = True
                    for child in graph[current]:
                        if not recent_seen[child]:
                            queue.append(child)
                if len(queue) > 0: 
                    count += 1
            min_dict[count].append(root)
            global_min = min(global_min, count)
        
        return min_dict[global_min]

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

x = set()
x.add("a")
x.add("b")
x.add("c")
print(x.pop())
print(x.pop())
print(x.pop())
                        
                            
                    
        
        