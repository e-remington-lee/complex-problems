from functools import lru_cache
class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph) - 1
        response = []
        
        self.backtrack(graph, 0, [], response, n)
        return response
    
    def backtrack(self, graph, index, carry_list, response, n):        
        carry_list.append(index)
        if index == n:
            response.append(list(carry_list))
            carry_list.pop()
            return
        
        for child in graph[index]:
            self.backtrack(graph, child, carry_list, response, n)
            
        carry_list.pop()

    def dynamic_programming(self, graph):
        self.n = len(graph) - 1
        self.memo = {}
        self.graph = graph
        response = self.helper(0)
        
        return response
        
    @lru_cache(maxsize=None)
    def helper(self, current):
        # if current in self.memo:
        #     return self.memo[current]
        
        if current == self.n:
            return [[current]]
        
        result = []
        for child in self.graph[current]:
            for r in self.helper(child):
                result.append([current] + r)
        # self.memo[current] = result
        return result

    def BFS(self, graph):
        n = len(graph) - 1
        response = []
        
        queue = [[0]]        
        while queue:
            current = queue.pop(0)
            paths = graph[current[-1]]
            for path in paths:
                if path == n:
                    response.append(current + [path])
                else:
                    queue.append(current + [path])
        return response

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
# li = []
# if True: li.append(5)
# print(li) 


def displaysublist(str_list): 
   # store all the sublists  
   response = [""] 
      
   # first loop  
   for i in range(len(str_list)):   
      # second loop  
      for j in range(i + 1, len(str_list) + 1):         
         # slice the subarray  
         sub = str_list[i:j] 
         response.append(sub) 
   return response 

print(displaysublist("abcd"))