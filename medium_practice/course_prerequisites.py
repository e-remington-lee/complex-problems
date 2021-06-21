from collections import defaultdict

class Solution:
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


c = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
c2 = {
  'g': ['e', 'f'], 
  'f': ['d', 'c'], 
  'e': ['d', 'c', 'b'],
  'd': ['b', 'a'],
  'c': ['b', 'a'],
  'b': ['a'],
  'a': []
}
x=Solution()
print(x.answer(c2))