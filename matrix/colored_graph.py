'''
Given a 2d array with colors, find the largest continuous path of a single color and return the length of that path
'''
class Solution:
    def answer(self, grid):
        max_count = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                # count = self.__traverse(x, y, grid, {})
                count = self.__traverse_iterative(x, y, grid, {})
                max_count = max(max_count, count)
        return max_count


    def __traverse(self, x, y, grid, seen):
        key = (x,y)
        if seen.get(key) != None:
            return 0
        seen[key] = True
        neighbors = self.__get_neighbors(x, y, grid, seen)
        _sum = 1
        for point in neighbors:
            xx = point[0]
            yy = point[1]
            if grid[yy][xx] == grid[y][x]:
                _sum += self.__traverse(xx, yy, grid, seen)
            else:
                continue
        return _sum


    def __traverse_iterative(self, x, y, grid, seen):
        stack = []
        color = grid[y][x]
        stack.append([x,y])
        _sum = 0
        while len(stack)>0:
            cords = stack.pop()
            itemX = cords[0]
            itemY = cords[1]
            key = (itemX, itemY)
            if seen.get(key) != None or grid[itemY][itemX] != color:
                continue
            # if grid[itemY][itemX] != color:
            #     continue
            neighbors = self.__get_neighbors(cords[0], cords[1], grid, seen)
            seen[key] = True
            _sum+=1
            for point in neighbors:
                xx = point[0]
                yy = point[1]
                if grid[yy][xx] == color:
                    stack.append([xx,yy])
                # seen[(xx,yy)]=True
        return _sum
        

    def __get_neighbors(self, x, y, grid, seen):
        cords = []
        neighbors = [
            [0, -1],
            [0, 1],
            [-1, 0],
            [1, 0]
        ]
        for n in neighbors:
            cordX = x + n[0]
            cordY = y + n[1]
            if cordX < 0 or cordY < 0 or cordX >= len(grid[0]) or cordY >= len(grid) or seen.get((cordX, cordY)) != None:
                continue
            cords.append([cordX, cordY])

            # if cordX >= 0 and cordY >= 0 and cordX < len(grid[0]) and cordY < len(grid):
            #     if seen.get((cordX, cordY)) == None:
            #         cords.append([cordX, cordY])
            #     else:
            #         continue
            # else:
            #     continue
        return cords


def main():
    grid = [
        ['r', 'g', 'b'],
        ['r', 'r', 'r'],
        ['g', 'r', 'r']
        ]

    sol = Solution()
    print(sol.answer(grid))

main()