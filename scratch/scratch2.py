class Node:
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

class BT(object):
    def inorder(self, node):
        current = node
        if current:
            self.inorder(current.left)
            print(current.value)
            self.inorder(current.right)

    def inorder_iterative(self, node):
        stack = []
        current = node
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.value)
                current=current.right
            else:
                break

    def preorder(self, node):
        current = node
        if current:
            print(current.value)
            self.preorder(current.left)
            self.preorder(current.right)

    def preorder_iterative(self, node):
        stack=[]
        stack.append(node)
        while stack:
            current = stack.pop()
            if current:
                print(current.value)
                stack.append(current.right)
                stack.append(current.left)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

    #easy
    def postorder_iterative(self, node):
        s1 = []
        s2 = []
        s1.append(node)
        # current = node
        while s1:
            current = s1.pop()
            s2.append(current)
            if current.left: s1.append(current.left)
            if current.right: s1.append(current.right)
        while s2:
            s = s2.pop()
            print(s.value)

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

    def dfs(self, node):
        stack=[]
        stack.append(node)
        while stack:
            node = stack.pop()
            if node:
                print(node.value)
                stack.append(node.right)
                stack.append(node.left)

    #bfs
    def tree_level(self, node: Node):
        stack = []
        stack.append(node)
        while stack:
            node = stack.pop(0)
            if node:
                print(node.value)
                stack.append(node.left)
                stack.append(node.right)

    def max_depth(self, node):
        return self.max_depth_helper(node, 0)
      
    # time, On, space worst cast On, amortized O(n/2) I think
    def max_depth_helper(self, node, depth):
        if not node:
            return depth
        depth +=1
        left = self.max_depth_helper(node.left, depth)
        right = self.max_depth_helper(node.right, depth)
        return max(left, right)

    # TC On because we perform operations on all nodes in the tree; space is Oh where h is the height.
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
        

def main():
    # [8, 6, 11, 3, 7, 9, 13]
    # root i=0; left = 2i+1; right=2i+2 
    #          8
    #        /   \
    #       6      11
    #      / \     / \
    #     3   7   9   13
    l1 = Node(6, left=Node(3), right=Node(7))
    r1 = Node(11, left=Node(9), right=Node(13))
    n1 = Node(8, left=l1, right=r1)
    l2 = Node(2, left=Node(3), right=Node(4))
    r2 = Node(2, left=Node(4), right=Node(3))
    n2 = Node(1, left=l2, right=r2)
    bt = BT()
    # bt.inorder_iterative(n1)
    # bt.inorder(n1)
    #3 6 7 8 9 11 13
    # bt.preorder(n1)
    # bt.preorder_iterative(n1)
    # 8 6 3 7 11 9 13
    # bt.postorder(n1)
    # bt.postorder_iterative(n1)

    # bt.postorder_hard(n1)
    # bt.tree_level(n1)
    print(bt.max_depth(n1))
    print(bt.symmetric_tree(n2))
main()



