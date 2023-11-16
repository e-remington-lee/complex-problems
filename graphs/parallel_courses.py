from collections import defaultdict, deque
class Solution:
    def minimumSemesters(self, n, relations):
        graph = defaultdict(list)
        indegree = {}
        for pre, _next in relations:
            graph[pre].append(_next)
            indegree[_next] = indegree.get(_next, 0) + 1
        
        seen = set()
        queue = deque([x for x in range(1, n + 1) if x not in indegree])
        count = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                seen.add(current)
                for child in graph[current]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)
            count += 1
            
        return count if len(seen) == n else -1


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)