class Solution:
    def postorder(self, root):
        output = []
        return self.helper(root, output)
    
    def helper(self, root, output):
        if not root:
            return output
        for x in root.children:
            self.helper(x, output)
        output.append(root.val)
        return output

    def iterative(self, root):
        output = []
        if not root:
            return []
        
        stack = [root]
        while stack:
            current = stack.pop()
            output.insert(0, current.val)
            for x in current.children:
                stack.append(x)  
        return output

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)