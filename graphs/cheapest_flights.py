from collections import defaultdict
import heapq
class Solution:
    def bellman_ford(self, n, flights, src, dst, k):
        prev = [float('inf') for _ in range(n)]
        current = [float('inf') for _ in range(n)]
        
        prev[src], current[src] = 0, 0
        
        for _ in range(k+1):
            for e in flights:
                root, to, price = e
                current[to] = min(prev[root] + price, current[to])
            prev, current = current, prev
            # prev = current.copy()
        
        return -1 if prev[dst] == float('inf') else prev[dst]


    def dijkstras(self, n, flights, src, dst, k):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for x, y, z in flights:
            matrix[x][y] = z
            
        distances = [float('inf') for _ in range(n)]
        stops_list = [float('inf') for _ in range(n)]
        distances[src], stops_list[src] = 0, 0
        
        heap = [(0, 0, src)]
        
        while heap:
            cost, stops, current = heapq.heappop(heap)
            if current == dst:
                return cost
            if stops == k + 1:
                continue  
            for neighbor in range(n):
                if matrix[current][neighbor] > 0:
                    dU, dV, wUV = cost, distances[neighbor], matrix[current][neighbor]
                    if dU + wUV < dV:
                        distances[neighbor] = dU + wUV
                        heapq.heappush(heap, (dU + wUV, stops + 1, neighbor))                
                    elif stops < stops_list[neighbor]:
                        '''
                    this prevents extremely large heaps, if each vertex could continually add their values to the heap each time
                    they weren't less, the heap just keeps growing for a very long time
                    ALSO, more importantly, there can be a situation where we get to a vertex and the cost is large but the flights taken is less.
                    Since we care about the number of flights taken, there is a scenario where even if we do not take the most efficient path to get to 
                    a location in terms of cost, we can still get to the destination in a less costly matter while maintaing the criteria of less stops if
                    the flights from that location are really cheap.
                     The testcase below shows this, not when you get to distantion 4 the second time, when the the cost to get there before was 
                     5 with 2 stops vs 6 with 1. Then the next flight from 4 costs 1, making it 7 cost with only 2 stops, beating the previously
                      best one of 9 cost with 2 stops. This is only found because we allowed it on the heap if it was worse cost but less stops
                    5
                    [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
                    0
                    2
                    2
                    '''   
                        heapq.heappush(heap, (dU + wUV, stops + 1, neighbor))
                    stops_list[neighbor] = stops
                    
        return -1 if distances[dst] == float('inf') else distances[dst]

    def IAmMasterOfCode_CodeDoesWhatIWant(self, n, flights, src, dst, k):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for x, y, z in flights:
            matrix[x][y] = z
         
        distances = {src:0}
        stops_list = {src:0}
        heap = [(0, 0, src)]
        
        while heap:
            cost, stops, current = heapq.heappop(heap)
            if current == dst:
                return cost
            if stops == k + 1:
                continue
            for neighbor in range(n):
                if matrix[current][neighbor] > 0:
                    if neighbor in distances:
                        if cost + matrix[current][neighbor] < distances[neighbor]:
                            distances[neighbor] = cost + matrix[current][neighbor]
                            heapq.heappush(heap, (cost + matrix[current][neighbor], stops + 1, neighbor))
                        elif stops < stops_list[neighbor]:
                            heapq.heappush(heap, (cost + matrix[current][neighbor], stops + 1, neighbor))
                    else:
                        distances[neighbor] = cost + matrix[current][neighbor]
                        heapq.heappush(heap, (cost + matrix[current][neighbor], stops + 1, neighbor))
                    stops_list[neighbor] = stops
                    
        return -1 if dst not in distances else distances[dst]


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)