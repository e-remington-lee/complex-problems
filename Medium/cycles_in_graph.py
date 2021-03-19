# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given an undirected graph, determine if a cycle exists in the graph.

# Here is a function signature:

# def find_cycle(graph):
#   # Fill this in.

# graph = {
#   'a': {'a2':{}, 'a3':{} },
#   'b': {'b2':{}},
#   'c': {}
# }
# print find_cycle(graph)
# # False
# graph['c'] = graph
# print find_cycle(graph)
# # True

# Can you solve this in linear time, linear space?
import sys
sys.path.append("..")
import os
print(os.getcwd())
print(os.listdir())
import Easy.pythagorean_triplets
import Subclass


class Solution:
    def answer(self, x):
        print(x)

def main():
    Solution().answer(2)
    Solution().answer(4)

print(__name__)
if __name__ == "__main__":
    main()
