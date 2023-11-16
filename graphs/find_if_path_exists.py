from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges, start: int, end: int):
        if not edges:
            return True
        graph = defaultdict(lambda: [])
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        if self.find_path(start, end, graph, visited):
            return True 
        return False
        
    def find_path(self, root, target, graph, visited):
        visited.add(root)
        if root == target:
            return True
        
        children = graph[root]
        for child in children:
            if child not in visited:
                if self.find_path(child, target, graph, visited):
                    return True
        return False

    def BFS(self, n: int, edges, start: int, end: int):
        if not edges:
            return True
        graph = defaultdict(lambda: [])
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        queue = [start]
        
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                for child in graph[current]:
                    if child == end:
                        return True
                    queue.append(child)
        return False   

# import sys
# sys.path.append(".")
# from utilities import to_string
# flashcard=to_string.file_to_string(__file__)
# print(flashcard)

