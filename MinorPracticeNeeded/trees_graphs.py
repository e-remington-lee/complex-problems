# typical tree operations
class Node(object):
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def dfs(self):
        print(self.value, end="")
        for child in self.children:
            child.dfs()

    def post_order(self):
        for child in self.children:
            child.post_order()
        print(self.value, end="")

    def dfs_iterative(self):
        stack = []
        stack.append(self)
        while len(stack):
            node = stack.pop()
            print(node.value, end="")
            #reversed better than li[::-1], https://www.geeksforgeeks.org/python-reversed-vs-1-which-one-is-faster/
            for child in reversed(node.children):
                stack.append(child)


    def bfs_iterative(self):
        queue = []
        queue.append(self)
        while len(queue):
            node = queue.pop(0)
            print(node.value, end="")
            for child in node.children:
                queue.append(child)



# b = Node("b", [Node("d"), Node("e")])
# c = Node("c", [Node('f'), Node("g")])
# root = Node("a", [b, c])
# root.dfs()
# print("")
root = Node(1, [Node(2, [Node(3)])])
root.post_order()
# root.dfs_iterative()