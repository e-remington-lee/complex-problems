class Solution:
    def preorder(self, root):
        return self.helper(root, [])
    
    def helper(self, root, output):
        if not root:
            return output
        
        output.append(root.val)
        for x in root.children:
            self.helper(x, output)
        return output

    def iterative(self, root):
        if not root:
            return []
        output = []
        stack = [root]
        while stack:
            current = stack.pop()
            output.append(current.val)
            for i in range(len(current.children)-1, -1, -1):
                stack.append(current.children[i])
        return output

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)