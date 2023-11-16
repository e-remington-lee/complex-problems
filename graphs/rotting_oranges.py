from collections import deque
class Solution:
    def modify_input(self, grid):
        answer = 0
        y = len(grid)
        x = len(grid[0])
        ones = 0
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for row in range(y):
            for col in range(x):
                if grid[row][col] == 1:
                    ones += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))    
        
        if ones == 0:
            return 0
        
        while queue:
            size = len(queue)
            answer += 1
            for _ in range(size):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc
                    if not (y - 1 >= nr >= 0 and x - 1 >= nc >= 0):
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        ones -= 1
                        if ones == 0:
                            return answer
        return -1


    def orangesRotting(self, grid):
        '''
        search through the matrix, add all 1s to map and 2s to queue
        we pop items off the queue from the left to get the most recent items, do a 4-way grid search, checking if the 
        grid number is in the ones map
        if the grid number is in the ones map, we add that to the queue and remove it from the ones map, this will 
        preserve the input and act as us changing it to a 2's value. This way if 2 2's are located close to eachother, the first
        will see the 1's item in the map and add it to the queue, but the second wont because the grid value is not in the 
        1's map
        
        each time we iterate over the queue, we only iterate over the queue for the length that it was when we started, this 
        will help us keep track of the time table in which the oranges are rotting so we can return the right value
        '''
        #make answer -1 or at each queue while-loop check if the queue is exhausted before adding to it
        answer = -1
        # This lets us not modify the initial input, if we are allowed to, we can forgo this method and just edit the grid
        # to have a rotten value instead of a 1
        ones_map = set()
        y = len(grid)
        x = len(grid[0])
        queue = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for row in range(y):
            for col in range(x):
                if grid[row][col] == 1:
                    ones_map.add((row, col))
                elif grid[row][col] == 2:
                    queue.append((row, col))
        
        if len(ones_map) == 0:
            return 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                cr, cc = queue.pop(0)
                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc
                    if not (y - 1 >= nr >= 0 and x - 1 >= nc >= 0):
                        continue
                    if (nr, nc) in ones_map:
                        queue.append((nr, nc))
                        ones_map.remove((nr, nc))
            answer += 1
        #here, if you decided to modify the input, you could keep a count of fresh oranges to begin with and make sure that value is 0 instead of
        # the len of the set
        return answer if len(ones_map) == 0 else -1

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)