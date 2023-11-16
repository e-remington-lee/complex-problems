# graph (child connect to parents, ect) -> tree (parents can have many nodes, no order) -> binary search tree (each parent node's left is less and right is greater than it)
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    #DFS
    def preorder(self, node):
        if node:
            print(node.value, end="")
            self.preorder(node.left)
            self.preorder(node.right)

    def preorder_iterative(self, node):
        stack=[]
        stack.append(node)
        while stack:
            current = stack.pop()
            if current:
                print(current.value)
                stack.append(current.right)
                stack.append(current.left)

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

    # DFS
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

    def peek(self, stack):
        if len(stack)>0:
            return stack[-1]
    # hard
    def postorder_hard(self, node):
        if not node:
            return
        stack=[]
        while True:
            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.right and self.peek(stack)==node.right:
                stack.pop()
                stack.append(node)
                node=node.right
            else:
                print(node.value)
                node=None
            
            if not stack:
                break

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

    def tree_level(self, node):
        stack = []
        stack.append(node)
        while stack:
            node = stack.pop(0)
            if node:
                print(node.value)
                stack.append(node.left)
                stack.append(node.right)

    def max_depth(self, node):
        if not node:
            return 0
        return 1+max(self.max_depth(node.left), self.max_depth(node.right))
    # can be improved slightly
    # def max_depth(self, node):
    #     return self.max_depth_helper(node, 0)
      
    # # time, On, space worst cast On, amortized O(n/2) I think
    # def max_depth_helper(self, node, depth):
    #     if not node:
    #         return depth
    #     depth +=1
    #     left = self.max_depth_helper(node.left, depth)
    #     right = self.max_depth_helper(node.right, depth)
    #     return max(left, right)

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

    # for a binary search tree
    def search_node(self, node, value):
        if not Node:
            return None
        if node.value==value:
            return node
        if value > node.value:
            return self.search_node(node.right, value)
        else:
            return self.search_node(node.left, value)

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

        
    # Time is On because we perform operations on all nodes in the tree; space is Oh where h is the height.
    def symmetric_tree(self, node):
        if not node:
            return True
        return self.__symmetric_tree_helper(node.left, node.right)
    
    #Needs boiler plate None error checking
    def __symmetric_tree_helper(self, left, right):
        if not left and not right:
            return True
        elif left.value!=right.value:
            return False
        elif self.__symmetric_tree_helper(left.left, right.right) and self.__symmetric_tree_helper(left.right, right.left):
            return True
        return False

    def symmetric_tree_iterative(self, node):
        if not node:
            return True
        s1 = [node.left]
        s2 = [node.right]
        while s1 and s2:
            left = s1.pop()
            right = s2.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if right.value!=left.value:
                return False
            else:
                s1 += left.left, left.right
                s2 += right.right, right.left
        return True


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
        
    def invert(self, node):
        if not node:
            return None
        node.left, node.right = node.right, node.left
        self.invert(node.right)
        self.invert(node.left)
        return node

    def tree_height(self, node):
        if not node:
            return 0
        return 1+max(self.tree_height(node.left), self.tree_height(node.right))

    def exists_in_tree(self, node, value):
        if not node:
            return False
        return node.value==value or self.exists_in_tree(node.left, value) or self.exists_in_tree(node.right, value)
    
    def invert_iterative(self, node):
        stack = [node]
        while stack:
            node = stack.pop()
            if node:
                node.right, node.left = node.left, node.right
                stack += node.right, node.left
        return node


# [8, 6, 11, 3, 7, 9, 13]
# root i=0; left = 2i+1; right=2i+2 
#          8
#        /   \
#       6      11
#      / \     / \
#     3   7   9   13       
# l1 = Node(6, left=Node(3), right=Node(7))
# r1 = Node(11, left=Node(9), right=Node(13))
# n1 = Node(8, left=l1, right=r1)
b = Node("b", left=Node("d"), right=Node("e"))
c = Node("c", left=Node("f"), right=Node("g"))
root = Node("a", left=b, right=c)

b2 = Node("c", left=Node("g"), right=Node("f"))
c2 = Node("c", left=Node("f"), right=Node("g"))
root2 = Node("a", left=b2, right=c2)
print(root2.symmetric_tree(root2))
print(root2.symmetric_tree_iterative(root2))
a3 = Node(3, left=Node(2))
root3 = Node(1, right=a3)
# root.preorder(root)
# root.preorder_iterative(root)
# root.in_order(root)
# root.in_order_iterative(root)
# root.post_order(root)
# root.post_order_iterative(root)
print(root.tree_level(root2))
# print(root.max_depth(root3))
# print(root.search_node(root3, 3))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

