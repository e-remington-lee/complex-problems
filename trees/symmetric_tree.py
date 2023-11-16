class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        return self.symmetric_helper(root.left, root.right)
    
    def symmetric_helper(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        
        if n1.val == n2.val:
            if self.symmetric_helper(n1.left, n2.right) and self.symmetric_helper(n1.right, n2.left):
                return True
            else:
                return False

import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)