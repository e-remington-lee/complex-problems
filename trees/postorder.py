 def postorder(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end="")

#post order, meaning post fact, reverse the preorder
def postorder_iterative(self, root):
    if not root:
        return
    s1 = []
    s2 = []
    s1.append(root)
    output = []
    while s1:
        current = s1.pop()
        s2.append(current)
        if current.left: s1.append(current.left)
        if current.right: s1.append(current.right)
    while s2:
        node2 = s2.pop()
        
        output.append(node2.val)
        
    return output