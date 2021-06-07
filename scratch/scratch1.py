class Node(object):
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

'''
Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.
'''  
class Solution:
    def answer(self, n):
        force = [0]*len(n)
        f=0
        for i in range(len(n)):
            if n[i]=="R":
                f=len(n)
            elif n[i]=="L":
                f=0
            else:
                f=max(0, f-1)
            force[i]+=f
        
        fl=0
        for i in range(len(n)-1, -1, -1):
            if n[i]=="L":
                fl=-len(n)
            elif n[i]=="R":
                fl=0
            else:
                fl=min(fl+1, 0)
            force[i]+=fl
        
        response=[]
        for x in force:
            if x>0:
                response.append("R")
            elif x<0:
                response.append("L")
            else:
                response.append(".")
        return "".join(response)




def main():
    dominos="..R..LL..R."
    x=Solution()
    print(x.answer(dominos))

main()


def fib(n):
    #index 0, 1, 2 are 1,1,2 vs indexing at 1,2,3 as 1,1,2
    first=0
    second=1
    for _ in range(n):
        first, second = second, first+second
    return second
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)

