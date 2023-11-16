from collections import defaultdict, deque
import collections
class Solution:
    def proper_topological(self, numCourses, prerequisites):
        adj = defaultdict(list)
        response = []
        indegree = {}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] = indegree.get(course, 0) + 1
            # if course not in indegree:
            #     indegree[course] = 1
            # else:
            #     indegree[course] += 1
        
        queue = deque([n for n in range(numCourses) if n not in indegree])
        
        while queue:
            current = queue.popleft()
            response.append(current)
            for child in adj[current]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                
        return response if len(response) == numCourses else []

    def custom_topical(self, numCourses, prerequisites):
        self.adj = defaultdict(list)
        self.seen = set()
        self.seen_recent = set()
        self.response = []
        for course, prereq in prerequisites:
            self.adj[course].append(prereq)
            
        for i in range(numCourses):
            if i not in self.seen:
                if self.dfs(i):
                    return []
        return self.response
    
    def dfs(self, index):
        self.seen.add(index)
        self.seen_recent.add(index)
        for child in self.adj[index]:
            if child not in self.seen and self.dfs(child):
                return True
            elif child in self.seen_recent:
                return True
        self.seen_recent.remove(index)
        self.response.append(index)
        return False
        
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

# print("w".__len__ < "e".__len__)

# from collections import defaultdict, Counter, deque

# words = ["wrt","wrf","er","ett","rftt"]

# adj_list = defaultdict(set)
# in_degree = Counter({c : 0 for word in words for c in word})
# print(in_degree)
# for first_word, second_word in zip(words, words[1:]):
#     print(first_word, second_word)
    # for c, d in zip(first_word, second_word):
    #     print(c, d)