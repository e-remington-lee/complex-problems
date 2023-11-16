from collections import deque, defaultdict
import heapq
class Solution:
    def ShorestPathFindingAlgo(self, times, n, k):
        graph = defaultdict(list)
        for root, target, weight in times:
            graph[root].append((target, weight))
        
        distance_map = {}
        for i in range(1, n+1):
            distance_map[i] = [float('inf'), None]
            
        distance_map[k][0] = 0
        distance_map[k][1] = None
        queue = deque([k])
        
        while queue:       
            current = queue.popleft()
            for target, weight in graph[current]:
                parent_distance = distance_map[current][0]
                edge = distance_map[target]
                new_distance = parent_distance + weight
                if new_distance < edge[0]:
                    edge[1] = current
                    edge[0] = new_distance
                    queue.append(target)
           
        total_distance = max(distance_map.values(), key=lambda x: x[0])

        return total_distance[0] if total_distance[0] != float('inf') else -1

    def dijkstra_heap(self, times, n, k):
        graph = defaultdict(list)
        for root, target, weight in times:
            graph[root].append((target, weight))

        heap = [(0, k)]
        distances = {}

        while heap:
            dist, node = heapq.heappop(heap)
            if node in distances: continue
            distances[node] = dist
            for target, weight in graph[node]:
                if target not in distances:
                    heapq.heappush(heap, (dist + weight, target))
        
        return max(distances.values()) if len(distances) == n else -1

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

# from itertools import combinations
# li = [1,2,3,4,5]
# out = set()
# for r in range(1, len(li)+1):
#     for c in combinations(li, r):
#         out.add("".join(str(c)))
# print(out)

# out = []
# for i in range(len(li)):
#     for j in range(i+1, len(li)+1):
#         out.append(li[i:j])
# x = out.copy()
# x[0]= "f"
# print(x)
# print(out)
