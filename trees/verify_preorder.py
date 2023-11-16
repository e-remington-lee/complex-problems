# https://www.youtube.com/watch?v=GYdC4hQSo8A

class Solution:
    def verifyPreorder(self, preorder):
        root = -float('inf')
        stack = []
        
        for i, val in enumerate(preorder):
            while stack and val > stack[-1]:
                root = stack[-1]
                stack.pop()
            if val < root:
                return False
            stack.append(val)
        
        return True


class Solution2:
    def verifyPreorder(self, preorder):
        lo = -float('inf')
        hi = -float('inf')
        
        for i, val in enumerate(preorder):
            if val <= lo:
                return False
            
            if val > hi:
                lo = hi
                hi = val
            else:
                j = i-1
                while j >= 0 and val > preorder[j]:
                    lo = preorder[j]
                    j -= 1
                
        return True