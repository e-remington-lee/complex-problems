'''
Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

time: O n, we make multiple loops but it is still linear
space: o n, we have the force/response functions, both are linear space
'''
class Solution(object):
    def answer(self, dominos):
        dominos=list(dominos)
        left=[]
        right=[]
        for i, x in enumerate(dominos):
            if x=="R":
                right.append(i)
            elif x=="L":
                left.append(i)
        while left or right:
            self.__helper(left, right, dominos)
        return "".join(dominos)
        
    def __helper(self, left, right, dominos):
        length = len(dominos)
        for i, r in enumerate(right):
            if r+2<length:
                if dominos[r+1]==".":
                    if dominos[r+2]=="L":
                        dominos[r+1]="F"
                        del right[i]
                    else:
                        dominos[r+1]="R"
                        right[i]+=1
                elif dominos[r+1]=="L" or dominos[r+1]=="R":
                    del right[i]
            elif r+1<length:
                if dominos[r+1]==".":
                    dominos[r+1]="R"
                    right[i]+=1
                elif dominos[r+1]=="L" or dominos[r+1]=="R":
                    del right[i]
            else:
                del right[i]
        
        for i, l in enumerate(left):
            if l-1>0:
                if dominos[l-1]==".":
                    dominos[l-1]="L"
                    left[i]-=1
                elif dominos[l-1]=="F":
                    dominos[l-1]="."
                    del left[i]
                elif dominos[l-1]=="R":
                    del left[i]
                elif dominos[l-1]=="L":
                    del left[i]
            else:
                del left[i]

    def optimal(self, dominos):
        length = len(dominos)
        force =[0]*length

        f=0
        for i in range(length):
            if dominos[i]=="R":
                f=length
            elif dominos[i]=="L":
                f=0
            else:
                f=max(f-1, 0)
            force[i]+=f
        f=0
        for i in range(length-1, -1, -1):
            if dominos[i]=="R": f=0
            if dominos[i]=="L": f=length
            else: f=max(f-1, 0)
            force[i]-=f
        
        response=[]
        for f in force:
            if f >0: response.append("R")
            elif f<0: response.append("L")
            else: response.append(".")
        return "".join(response)

            

dominos="..R..LL..R."
x = Solution().optimal(dominos)
print(x)
n=0
l=[0,1,2,3,4]
for x in l:
    if x==0:
        n=5
    else:
        n-=1
print(n)