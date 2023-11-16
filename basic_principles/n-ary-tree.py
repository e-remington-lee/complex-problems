class TreeNode(object):
    def __init__(self, value, children=[]):
        self.value=value
        self.children=children

    def get_depth(self, node):
        if not node:
            return 0
        m=0
        for n in node.children:
            d=self.get_depth(n)
            m=max(m,d)
        return m+1

    def inorder(self, node):
        if not node:
            return None
        
        children = len(node.children)

        for i in range(children - 1):
            self.inorder(node.children[i])
        
        print(node.value)

        self.inorder(node.children[-1])


def main():
    n1 = TreeNode("a1", children=[TreeNode("b2", children=[TreeNode("c3"), TreeNode("d3")]), TreeNode("c2")])
    # n1 = TreeNode("a1")
    print(n1.get_depth(n1))
    import sys
    sys.path.append(".")
    from utilities import to_string
    flashcard=to_string.file_to_string(__file__)
    print(flashcard)

if __name__=="__main__":
    main()
