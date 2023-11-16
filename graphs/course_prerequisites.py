'''
Do this one too https://leetcode.com/problems/course-schedule/

Hi, here's your problem today. This problem was recently asked by Google:

You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

Example:
{
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}

This input should return the order that we need to take these courses:
 ['CSC100', 'CSC200', 'CSCS300']

Here's your starting point:

def courses_to_take(course_to_prereqs):
  # Fill this in.

courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print courses_to_take(courses)
# ['CSC100', 'CSC200', 'CSC300']

https://leetcode.com/problems/course-schedule/
'''
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
c3 = {
'g': ['e', 'f'], 
'f': [], 
'e': [],
'd': [],
'c': [],
'b': ['a'],
'a': []
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
# import sys
# sys.path.append(".")
# from utilities import to_string
# flashcard=to_string.file_to_string(__file__)
# print(flashcard)