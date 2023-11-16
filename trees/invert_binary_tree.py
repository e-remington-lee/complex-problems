class Solution:
    def invertTree(self, root):
        if not root:
            return root
        stack=[root]
        while stack:
            node = stack.pop()
            node.right, node.left = node.left, node.right
            if node.left : stack.append(node.left)
            if node.right : stack.append(node.right)
        return root

    def recursive(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.recursive(root.left)
            self.recursive(root.right)
        return root


import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)