class Solution:
    # doesn't pass LC, but passes almost all of the tests, unsure what breaks it
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        
        return self.get_height(root.left) + self.get_height(root.right)

    def get_height(self, root):
        if not root:
            return 0
        
        return max(1 + self.get_height(root.left), 1 + self.get_height(root.right))


