class Node(object):
    def __init__(self, value, right=None, left=None):
        self.value=value
        self.right=right
        self.left=left
        
class BinaryTree(object):
    def invert_recursive(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.invert_recursive(node.left)
            self.invert_recursive(node.right)
        return node

    def preorder(self, node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def invert_bfs(self, node):
        queue=[node]
        while queue:
            current=queue.pop(0)
            if current:
                current.left, current.right = current.right, current.left
                queue.append(current.left)
                queue.append(current.right)
            # current.left, current.right = current.right, current.left
            # if current.left: queue.append(current.left)
            # if current.right: queue.append(current.right)
        return node

    def invert_dfs(self, node):
        stack=[node]
        while stack:
            current=stack.pop()
            if current:
                current.left, current.right = current.right, current.left
                stack.append(current.right)
                stack.append(current.left)
        return node


b = Node("b", left=Node("d"), right=Node("e"))
c = Node("c", left=Node("f"), right=Node("g"))
root = Node("a", left=b, right=c)
x = BinaryTree()
# x.invert_recursive(root)
x.invert_dfs(root)
x.preorder(root)


