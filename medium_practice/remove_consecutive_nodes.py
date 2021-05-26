'''
Given a linked list of integers, remove all consecutive nodes that sum up to 0.
The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed. 4 -> -4 also sums up to 0 too so that sequence should also be removed.
'''
class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next


class Solution(object):
    def get_list(self, node):
        li = []
        while node:
            li.append(node.value)
            node=node.next
        return li

    # very rough way to delete items from a list while iterating
    def brute(self, node):
        li = self.get_list(node)
        d={}
        finished=False
        outer_break=False
        while not finished:
            outer_break=False
            for i in range(len(li)):
                sum=li[i]
                for j in range(i+1, len(li)):
                    sum+=li[j]
                    if sum==0:
                        del li[i:j+1]
                        outer_break=True
                        break
                if outer_break:
                    break
                if i+1==len(li):
                    finished=True
                    break
        return li

    def optimal(self, node):
        pass

n1=Node(10, Node(5, Node(-3, Node(-3, Node(1, Node(4, Node(-4)))))))
x = Solution().brute(n1)
print(x)
while x:
    print(x.value)
    x=x.next


# l=[1,2,3,4,5,6]
# for i, x in enumerate(l):
#     if x==3:
#         del l[2:4]
#     print(i)
# print(l)