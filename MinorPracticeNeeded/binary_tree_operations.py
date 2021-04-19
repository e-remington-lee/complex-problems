class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def pre_order(self, node):
        if node:
            print(node.value, end="")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def pre_order_iterative(self, node):
        stack = []
        stack.append(node)
        while len(stack):
            current_node = stack.pop()
            print(current_node.value, end="")
            if current_node.right: stack.append(current_node.right) 
            if current_node.left: stack.append(current_node.left)
 

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end="")
            self.in_order(node.right)


    def in_order_iterative(self, node):
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


    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end="")

    def post_order_iterative(self, node):
        if not Node:
            return
        s1 = []
        s2 = []
        s1.append(node)
        while s1:
            current = s1.pop()
            s2.append(current)
            # print(current.value, end="")
            if current.left: s1.append(current.left)
            if current.right: s1.append(current.right)
        while s2:
            node2 = s2.pop()
            print(node2.value, end="")


    def tree_level_order(self, node):
        response = []
        if not node:
            return response
        return self.__trl(response, [node])
        

    def __trl(self, response, li):
        if not li:
            return response
        response.append([nv.value for nv in li])
        li2 = []
        for n in li:
            if n.left: li2.append(n.left)
            if n.right: li2.append(n.right)
        return self.__trl(response, li2)


    def tree_level_order_iterative(self, node):
        pass

        


b = Node("b", left=Node("d"), right=Node("e"))
c = Node("c", left=Node("f"), right=Node("g"))
root = Node("a", left=b, right=c)
# a = Node(2, left=Node(3))
# root = Node(1, right=a)
# root.pre_order(root)
# root.pre_order_iterative(root)
# root.in_order(root)
# root.in_order_iterative(root)
# root.post_order(root)
# root.post_order_iterative(root)
print(root.tree_level_order(root))

