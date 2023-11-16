# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.first, self.current = None, None
        self.inorder(root)
        self.current.right=self.first
        self.first.left=self.current
        return self.first
        
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if not self.first:
                self.first=root
            else:
                self.current.right = root
                root.left = self.current
            self.current=root
            self.inorder(root.right)

    def custom(self, root: 'Node') -> 'Node':
        if not root:
            return None
        node_list=[]
        self.inorder(root, node_list)
        head = self.create_ll(node_list)  
        return head
    
    def inorder(self, root, node_list):
        if root:
            self.inorder(root.left, node_list)
            node_list.append(root.val)
            self.inorder(root.right, node_list)
            
    def create_ll(self, node_list):
        _next=None
        current=head=None
        
        for x in node_list:
            if not head:
                head = Node(x)
                current=head
            else:
                current.right=Node(x, left=current)
                current=current.right
        current.right=head
        head.left=current
        return head

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)