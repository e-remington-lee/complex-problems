class Solution(object):
    def __init__(self):
        self.count=0
        self.i=0

    def answer(self, h, w):
        if h>1 and w>1:
            return self.__helper(h,w)
        return 1
    
    def __helper(self,h,w):
        # if you write out this solution with 3,3 you see that when you get to 2,2 you calculate the same things coming from 3,2 and 2,3. 
        # This means we have repeat calculations, we can optimize this
        if h>1:
            self.__helper(h-1, w)
        if w>1:
            self.__helper(h, w-1)
        if h==1 and w==1:
            self.count+=1
        return self.count

    # the fully, non-class recursive way to do this problem
    def __helper2(self, h,w):
        if h==1 and w==1:
            return 1
        if h==0 or w==0:
            return 0
        return self.__helper2(h-1, w)+self.__helper2(h,w-1)

    def regular_recursion(self, h, w):
      # here, you can return 1 if h or w is 1 because from there you only have 1 direction to go
      # since you can only go right or down
      if h==1 or w==1:
        return 1
      else:
        self.i+=1
        print(self.i)
        return self.abc(h-1, w)+self.abc(h,w-1)

    # To get here, you'd have to realize you are duplicating results. Once you figured out that well I know how many ways I can get to each 
    # individual square, you can reason that hey if the top one has 1 way to get to it, the left one has 1 way, then the square I am on has 2 ways.
    # then you can propogate that to the next few squares. If the top square has 2 ways, left has 3, then there are 5 ways to get to the current square
    # this does require that you start off with the array 
    def optimal(self, h, w):
        A = [[0 for x in range(w)] for x in range(h)]
        for x in range(w):
            A[0][x]=1
        for x in range(h):
            A[x][0]=1
        for i in range(0, h):
            for j in range(0, w):
                ##if you did not realize you can pre-modify the array, you can also do it in line here
                # if i==0:
                #     A[i][j]=1
                # elif j==0:
                #     A[i][j]=1
                # else:
                #     A[i][j]=A[i-1][j]+A[i][j-1]
                A[i][j]=A[i-1][j]+A[i][j-1]
        print(A)
        return A[h-1][w-1]

# x = Solution().regular_recursion(3,3)
# x = Solution().answer(3,3)
x = Solution().optimal(3,4)
print("answer, " + str(x))


