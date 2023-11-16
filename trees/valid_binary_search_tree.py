# from typing import NewType

# Node = NewType("Node", int)

# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.__right_node = None
#         self.__left_node = None
#     def set_node(self, node):
#         if self.__left_node == None and node.value < self.value:
#             self.__left_node = node
#         elif self.__right_node == None and node.value > self.value:
#             self.__right_node = node
#         elif 

import sys

class Node:
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
        

class Solution:
    def answer(self, node, _min=float("-inf"), _max=float("inf")):
        if not node:
            return True
        val = node.value
        if ((val>_min and val<_max) and 
            self.answer(node.left_node, _min, val) and self.answer(node.right_node, val, _max)):
            return True
        return False

node2 = Node(7, Node(6), Node(8))
node = Node(5, Node(3), node2)
sol = Solution()
print(sol.answer(node, _min=0, _max=100))
# print(sol.answer(node))


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
