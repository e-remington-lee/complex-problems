from collections import defaultdict
class TopologicalSort(object):
    def answer(self, graph):
        visited=defaultdict(lambda: False)
        recent_stack=defaultdict(lambda: False)
        stack=[]
        for vertex in graph.keys():
            if not visited[vertex]:
                if self.answer_helper(vertex, graph, visited, recent_stack, stack):
                    return None
        return stack

    def answer_helper(self, vertex, graph, visisted, recent_stack, stack):
        visisted[vertex]=True
        recent_stack[vertex]=True
        for vertex2 in graph[vertex]:
            if not visisted[vertex2]:
                if self.answer_helper(vertex2, graph, visisted, recent_stack, stack):
                    return True
            elif recent_stack[vertex2]:
                return True
        recent_stack[vertex]=False
        stack.append(vertex)
        return False
            

g= {
    5: [0, 2],
    4: [0, 1],
    3: [1],
    2: [3],
    1: [],
    0: []
    }

x=TopologicalSort()
print(x.answer(g))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
# print(flashcard)