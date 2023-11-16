class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left=left
        self.right=right
    
    @staticmethod
    def binary_search(arr, value):
        if not arr:
            return None
        idx = len(arr)//2
        current = arr[idx]
        if current==value:
            return value
        if value >= current:
            return binary_search(arr[idx+1:], value)
        else:
            return binary_search(arr[:idx], value)

    def search_node(self, root, value)->object:
        if not root or root.value==value:
            return root
        if value >= root.value:
            return self.search_node(root.right, value)
        else:
            return self.search_node(root.left, value)

    def search_node_iterative(self, root, value)->object:
        if not root:
            return None
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                return None
            if node.value==value:
                return node
            if value > node.value:
                stack.append(node.right)
            else:
                stack.append(node.left)

    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        if root.value==value:
            return root
        if value > root.value:
            root.right = self.insert(root.right, value)
        else:
            root.left= self.insert(root.left, value)
        return root

    def delete(self, root, value):
        if not root:
            return None
        if root.value==value:
            if root.right:
                root.value = root.right.value
                root.right=None
            elif root.left:
                root.value = root.left.value
                root.left=None
            else:
                root=None
            return root
        if value > root.value:
            root.right = self.delete(root.right, value)
        else:
            root.left = self.delete(root.left, value)  
        return root     
        
# Consider doing with heap sort too
#worst n^2, average n logn,  space is in-place so??
class KthLargest(object):
    def __init__(self):
        super().__init__()

    def kth_largest(self, arr, k):
        if k > len(arr):
            return None
        k = len(arr)-k
        return self.quick_sort(arr, 0, len(arr)-1, k)

    def quick_sort(self, arr, low, high, k):
        if low < high:
            pi = self.partition(arr, low, high)
            if k>pi:
                self.quick_sort(arr, pi+1, high, k)
            elif k<pi:
                self.quick_sort(arr, low, pi-1, k)
            elif k==pi:
                return arr[pi]
        return arr[k]

    def partition(self, arr, low, high):
        for x in range(low, high):
            if arr[x]<=arr[high]:
                arr[low], arr[x] = arr[x], arr[low]
                low+=1
        arr[high], arr[low] = arr[low], arr[high]
        return low
        


#Make sure to print them 
def main():
    b2 = TreeNode(4, left=TreeNode(3), right=TreeNode(6))
    c2 = TreeNode(10, left=TreeNode(9), right=TreeNode(11))
    root = TreeNode(7, left=b2, right=c2)
    node1=root.search_node_iterative(root, 10)
    print(node1.left.value, node1.value, node1.right.value)
    root2 = root.insert(root, 5)
    def post_order(root):
        if root:
            post_order(root.left)
            post_order(root.right)
            print(root.value, end="")
    post_order(root2)
    print("")
    root3 = root.delete(root, 5)
    post_order(root3)
    print("")
    li = [4,5,8,2]
    
    print(KthLargest().kth_largest([2,1,5,4,3], 1))

    # nums = [1,2,3,4,5,6,7,8,9]
    # print(root.binary_search(nums, 5))

main()
