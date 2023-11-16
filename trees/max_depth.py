# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        li=[root]
        c=0
        while li:
            x=len(li)
            for i in range(x-1, -1, -1):
                cur=li.pop(0)
                if cur.left: 
                    li.append(cur.left)
                if cur.right:
                    li.append(cur.right)
            c+=1
        return c

    def recursive(self, root):
        if not root:
            return 0
        lh=self.maxDepth(root.left)
        rh=self.maxDepth(root.right)
        return max(lh+1, rh+1)

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)