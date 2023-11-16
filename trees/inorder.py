#DFS, probably the most accuracte dfs compared to the pre/post order
def inorder(self, node):
    if node:
        self.in_order(node.left)
        print(node.value, end="")
        self.in_order(node.right)

#DFS
#INorder, INFINITE, WHILE TRUE:
def inorder_iterative(self, node):
    stack = []
    current = node
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.value, end="")
            current = current.right
        else:
            break