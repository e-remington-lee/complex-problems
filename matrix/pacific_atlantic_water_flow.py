class Solution:
    '''
    time: O(n^2 * m ^2) we do a double for loop on m and n, then we in each function we do a DFS, which at worst case could call each other matrix value
    again
    space: O(n * m), recusion stack and the self.seen value
    '''
    def brute(self, heights):
        out = []
        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = heights
        self.seen = [[False for i in range(self.n)] for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.helper(i, j, 0, 0, float('inf')) and self.helper(i, j, self.m-1, self.n-1, float('inf')):
                    out.append([i, j])
        return out
    
    def helper(self, i, j, goalY, goalX, ph):
        if i >= 0 and i < self.m and j >= 0 and j < self.n and self.heights[i][j] <= ph:
            if not self.seen[i][j]:
                self.seen[i][j] = True
            else:
                return False
    
            if i is goalY or j is goalX:
                self.seen[i][j] = False
                return True
            
            else:
                # up, down, left, right
                if (self.helper(i -1, j, goalY, goalX, self.heights[i][j])
                    or self.helper(i, j - 1, goalY, goalX, self.heights[i][j])
                    or self.helper(i + 1, j, goalY, goalX, self.heights[i][j])
                    or self.helper(i , j + 1, goalY, goalX, self.heights[i][j])):
                    self.seen[i][j] = False
                    return True
                else:
                    self.seen[i][j] = False
                    return False
        else:
            return False

    def i_tried_might_work_but_bad(self, heights):
        out = []
        height = len(heights)
        width = len(heights[0])
        seen = [[None for _ in range(height)] for _ in range(width)]
        deltas = [(-1 , 0), (1, 0), (0, 1), (0, -1)]
        for row in range(height):
            for col in range(width):
                stack = []
                stack.append((row, col))
                pacific, atlantic = False, False
                while stack:
                    cur = stack.pop()
                    for dr, dc in deltas:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < height and 0 <= new_col < width:
                            if seen[new_row][new_col] is not None:
                                if seen[new_row][new_col]:
                                    out.append((row, col))
                                else:
                                    continue # we saw this before, and it was False
                            '''
                            Here we would fiture out if we can go from row to new_row and such based off the 
                            heights, then we could make the seen matrix work for us using DP to say if we had seen
                            a bad or good point
                            
                            problem is, if the first row is 7,5,4,3,2,1, we eventually get to 1 which works! but we have no
                            way of knowing 7,5,4,3,2 also lead to a solution bc we cannot intelligently cache this. There
                            could be a solution to this, but unsure
                            ''' 

class BFS:
    def BFS(self, heights):
        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = heights
        pacific = []
        atlantic = []
        
        for i in range(self.m):
            pacific.append([i, 0])
            atlantic.append([i, self.n-1])
        for i in range(self.n):
            pacific.append([0, i])
            atlantic.append([self.m-1, i])
            
        pacific_set = self.helper(pacific)
        atlantic_set = self.helper(atlantic)
        
        return list(pacific_set.intersection(atlantic_set))
        
    def helper(self, li):
        response = set()
        while li:
            y, x = li.pop()
            response.add((y, x))
            for yy, xx in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                cy, cx = y + yy, x + xx
                if cy < 0 or cy >= self.m or cx < 0 or cx >= self.n:
                    continue
                if (cy, cx) in response:
                    continue
                if self.heights[cy][cx] >= self.heights[y][x]:
                    li.append([cy, cx])
        return response

class DFS:
    def DFS(self, heights):
        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = heights
        pacific = set()
        atlantic = set()
        
        for i in range(self.m):
            self.helper(i, 0, pacific)
            self.helper(i, self.n-1, atlantic)
        for i in range(self.n):
            self.helper(0, i, pacific)
            self.helper(self.m-1, i, atlantic)
        
        return list(pacific.intersection(atlantic))
        
    def helper(self, y, x, ocean):
        ocean.add((y, x))
        for yy, xx in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            cy, cx = y + yy, x + xx
            if cy < 0 or cy >= self.m or cx < 0 or cx >= self.n:
                continue
            if (cy, cx) in ocean:
                continue
            if self.heights[cy][cx] >= self.heights[y][x]:
                self.helper(cy, cx, ocean)


x = Solution().brute([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
assert x == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

j = set([1,2,3])
y = set([2,3,4])
print(list(j.intersection(y)))


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

