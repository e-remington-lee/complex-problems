class Solution:
    def calcEquation(self, equations, values, queries):
        mappings = {}
        index = 0
        for x, y in equations:
            if x not in mappings:
                mappings[x] = index
                index += 1
            if y not in mappings:
                mappings[y] = index
                index += 1
        
        dg = Dg(index) 
        for i in range(len(equations)):
            letter1, letter2 = equations[i]
            value = values[i]
            dg.union(mappings[letter1], mappings[letter2], value)
        
        result = []
        for letter1, letter2 in queries:
            if letter1 not in mappings or letter2 not in mappings:
                result.append(-1.0)
            else:
                rootX, weightX = dg.find(mappings[letter1])
                rootY, weightY = dg.find(mappings[letter2])
                if rootX != rootY:
                    result.append(-1.0)
                else:
                    result.append(weightX / weightY)
        return result
  
class Dg:
    def __init__(self, size):
        self.root = [[i, 1] for i in range(size)]
    
    def find(self, x):
        root, weight = self.root[x]
        if x != root:
            new_root, new_weight = self.find(root)
            self.root[x] = [new_root, weight * new_weight]
            return self.root[x]
        return self.root[x]
    
    def union(self, x, y, value):
        rootX, weightX = self.find(x)
        rootY, weightY = self.find(y)
        if rootX != rootY:
            self.root[rootX] = [rootY, value * weightY / weightX]

class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        graph = defaultdict(defaultdict)
        
        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            graph[x][y] = value
            graph[y][x] = 1 / value
            
        response = []
        for x, y in queries:
            if x not in graph or y not in graph:
                value = -1.0
            elif x == y:
                value = 1.0
            else:
                visisted = set()
                value = self.backtracking(x, y, 1, visisted, graph)
            response.append(value)
        return response
        
    def backtracking(self, x, y, value, visited, graph):
        visited.add(x)
        children = graph[x]
        response = -1.0
        if y in children:
            return value * children[y]
        else:
            for child, child_value in children.items():
                if child in visited:
                    continue
                '''
                We do it this way bc there is no guarantee that the recursion finds anything important. It could return -1 
                if the first child has no children since it won't continue through the backtracing. This is a problem if the                        second has the answer. For this reason we have to employ the back tracking base case
                method which is, we need to know what we are looking for, if it isn't -1, we found it
                '''
                response = self.backtracking(child, y, value * child_value, visited, graph)
                if response != -1.0:
                    break
                # else:                
                #     return self.backtracking(child, y, value * child_value, visited, graph)
        # not needed, but it must improve it somehow, I don't see it.
        # visited.remove(x)
        return response

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
