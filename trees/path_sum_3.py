from collections import defaultdict
class Solution: 
    def prefix_sum(self, root, targetSum):
        if not root:
            return 0
        self.target = targetSum
        self.carry = self.count = 0
        self.prefix_sum = defaultdict(int)
        self.pre_order(root)
        return self.count
    
    def pre_order(self, root):
        self.carry += root.val
        
        if self.carry == self.target:
            self.count += 1
        
        self.count += self.prefix_sum[self.carry - self.target]
        
        self.prefix_sum[self.carry] += 1
        
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)
            
        self.prefix_sum[self.carry] -= 1
        self.carry -= root.val

    def brute(self, root, targetSum):
        '''
        brute force is n^2 and linear space
        we would run an algo that finds the sums assuming each node as a head. this will take n^2, then we need lienar space
        for recursion, best case log(h) where h is the height
        '''
        pass

    def bad(self, root, targetSum):
        '''
        I believe the time/space is O(2n) / O(2N) bc we loop through the tree twice at each node, then we have to check to make sure
        the node has not been seen before, it is hasn't we can call it with a 0 carry, else we skip that
        '''
        if not root:
            return 0
        self.seen = {}
        self.count = 0
        self.target = targetSum
        self.path_helper(root, 0)
        return self.count
    
    def path_helper(self, root, carry):
        if root.val + carry == self.target:
            self.count += 1
        
        if root.left:
            if root.left not in self.seen:
                self.path_helper(root.left, 0)
            self.path_helper(root.left, carry + root.val)
        if root.right:
            if root.right not in self.seen:
                self.path_helper(root.right, 0)
            self.path_helper(root.right, carry + root.val)
        self.seen[root] = True


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)