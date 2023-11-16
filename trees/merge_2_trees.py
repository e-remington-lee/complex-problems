class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        
        elif not root2:
            return root1
        
        root1.val += root2.val
        
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


    def iteartive(self, root1, root2):
        if not root1:
            return root2
        
        elif not root2:
            return root1
        
        stack1 = deque([root1])
        stack2 = deque([root2])
        while stack1 or stack2:
            c1 = stack1.popleft()
            c2 = stack2.popleft()
            
            if not c2:
                continue
            
            c1.val = c1.val + c2.val
            if not c1.left:
                c1.left = c2.left
            else:
                stack1.append(c1.left)
                stack2.append(c2.left)
                
            if not c1.right:
                c1.right = c2.right
            else:
                stack1.append(c1.right)
                stack2.append(c2.right)
  
        return root1

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)