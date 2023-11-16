'''
Largest Smaller BST Key
Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree that is smaller than num. If such a number doesn’t exist, return -1. Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.
'''
class Node:
# Constructor to create a new node
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
      self.root = None

  def find_largest_smaller_key(self, num):
    # return self.helper(num, self.root, -1)
    current = self.root
    output=-1
    while current:
      if current.key < num:
        output=current.key
        current = current.right
      else:
        current = current.left
    return output

  def helper(self, num, current, output):
    if not current:
      return output
    else:
      if current.key < num:
        # output = current.key
        return self.helper(num, current.right, current.key)
      else:
        return self.helper(num, current.left, output)

  def iterative(self, num):
    current = self.root
    output=-1
    while current:
      if current.key < num:
        output=current.key
        current = current.right
      else:
        current = current.left
    return output


  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid
  # using reference parameters)
  def insert(self, key):
      # 1) If tree is empty, create the root
      if (self.root is None):
          self.root = Node(key)
          return

      # 2) Otherwise, create a node with the key
      #    and traverse down the tree to find where to
      #    to insert the new node
      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right

######################################### 
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()
 
# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)   
result = bst.find_largest_smaller_key(17)

print ("Largest smaller number is %d " %(result))


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)