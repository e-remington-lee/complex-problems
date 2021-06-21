from collections import defaultdict
class TopologicalSort(object):
    def answer(self, graph):
        visited=defaultdict(lambda: False)
        recent_stack=defaultdict(lambda: False)
        queue=[]
        for vertex in graph.keys():
            if not visited[vertex]:
                if self.answer_helper(vertex, graph, visited, recent_stack, queue):
                    return None
        return queue

    def answer_helper(self, vertex, graph, visisted, recent_stack, queue):
        visisted[vertex]=True
        recent_stack[vertex]=True
        for vertex2 in graph[vertex]:
            if not visisted[vertex2]:
                if self.answer_helper(vertex2, graph, visisted, recent_stack, queue):
                    return True
            elif recent_stack[vertex2]:
                return True
        recent_stack[vertex]=False
        queue.insert(0, vertex)
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