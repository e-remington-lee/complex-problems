from itertools import combinations, permutations

out=[]
for c in combinations("1234", 3):
    out.append(''.join(c))

print(out)

# out2=[]
# for c in permutations("1234", 3):
#     out2.append(''.join(c))


# print(out2)

# amount of combinations = c! / (r!(c-r)!) where c is the list of numbers and r is how many we can choose from them 

a=[1,2,3]
print(a)
nums = list(range(1, 2 + 1)) + [4 + 1]
print(nums)

class Node(object):
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def find(target, node):
    if not node:
        return False
    if node.val is target or find(target, node.next):
        return True
    else:
        return False

def insert_after(after, new_node, node):
    if not node:
        return
    if node.val is after:
        hold = node.next
        node.next = Node(new_node)
        node.next.next = hold
    else:
        insert_after(after, new_node, node.next)

class LL:
    def __init__(self, node):
        self.head = node

    def delete_node(self, target):
        current = self.head
        if not current:
            return None
        if current.val is target:
            self.head = current.next
            current = None
            return None
        return self.delete_helper(target, current.next, current)
    
    def delete_helper(self, target, current, prev):
        if not current:
            return None
        
        if current.val is target:
            prev.next = current.next
            current = None
            return True
        else:
            return self.delete_helper(target, current.next, current)


n = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(find(3, n))
insert_after(3, 6, n)

l = LL(n)
l.delete_node(3)
current = l.head
while current:
    print(current.val)
    current = current.next

# while n:
#     print(n.val)
#     n = n.next

s="abcd"
out = set()
if len(s) is 0:
    out.add("")
    print(out)

x= [1,2,3,4,5]
print(x[4::-1])

