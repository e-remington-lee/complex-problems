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

    # can be improved slightly
    def max_depth(self, node):
        if not node:
            return 0
        count = 1
        return self.__md(node, count)

    def __md(self, node, count):
        cr = cl = 0
        if node.left:
            cl = count+1
            cl = self.__md(node.left, cl)
        if node.right:
            cr = count +1
            cr = self.__md(node.right, cr)
        return max(cr, cl, count)

    def get_node_depth(self, node, value):
        return self.__depth_helper(node, value, 1)

    # does not work if there are multiple nodes of the same value that both get found, which one do we pick?
    # this one would choose the furthest one, but not a good way to reverse it
    def __depth_helper(self, node, value, depth):
        if not node:
            return -1
        if node.value==value:
            return depth
        depth+=1
        dl = self.__depth_helper(node.left, value, depth)
        dr = self.__depth_helper(node.right, value, depth)
        return max(dl, dr)

    # perfect binary tree means all leaf nodes are the same depth and all nodes have 2 children
    # log(n) time
    def get_perfect_binary_tree_depth(self, node):
        if not node:
            return 0
        return self.__hpbtd(node, 1)

    def __hpbtd(self, node, depth):
        if node.left:
            return self.__hpbtd(node.left, depth+1)
        else:
            return depth

        
    def palindrome(self, node):
        if not node:
            return False
        return self.__palindrome_helper(node.left, node.right)
    
    #TODO add some boiler plate error checking for NoneType.value if not perfectly balanced
    def __palindrome_helper(self, left, right):
        if left is None and right is None:
            return True
        if left.value != right.value:
            return False
        if self.__palindrome_helper(left.left, right.right) and self.__palindrome_helper(left.right, right.left):
            return True
        else:
            return False


    def palindrome_iterative(self, node):
        if not node:
            return False
        if node.right is None and node.left is None:
            return True
        stack_left = []
        stack_right = []
        stack_left.append(node.left)
        stack_right.append(node.right)
        while stack_left and stack_right and len(stack_left)==len(stack_right):
            left = stack_left.pop()
            right = stack_right.pop()
            if left.value == right.value:
                if left.left: stack_left.append(left.left)
                if left.right: stack_left.append(left.right)
                if right.right: stack_right.append(right.right)
                if right.left: stack_right.append(right.left)
            else:
                return False
        return True
        
        


        

b = Node("b", left=Node("d"), right=Node("e"))
c = Node("c", left=Node("f"), right=Node("g"))
root = Node("a", left=b, right=c)

b2 = Node("c", left=Node("g"), right=Node("f"))
c2 = Node("c", left=Node("f"), right=Node("g"))
root2 = Node("a", left=b2, right=c2)
print(root2.palindrome(root2))
print(root2.palindrome_iterative(root2))
a3 = Node(2)
root3 = Node(1, right=a3)
# root.pre_order(root)
# root.pre_order_iterative(root)
# root.in_order(root)
# root.in_order_iterative(root)
# root.post_order(root)
# root.post_order_iterative(root)
print(root.tree_level_order(root2))
print(root.max_depth(root3))

