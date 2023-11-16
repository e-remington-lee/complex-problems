# https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def optimal(self, matrix, target):
        if not matrix:
            return False
        row, col = len(matrix) - 1, 0
        
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            cur = matrix[row][col]
            if cur == target:
                return True
            elif cur < target:
                col += 1
            else:
                row -= 1
        return False


    def searchMatrix(self, matrix, target: int) -> bool:
        for i in range(len(matrix)):
            if self.binary_search(matrix[i], target):
                return True
        return False
    
    
    def binary_search(self, arr, target):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(high+low)//2
            if arr[mid]==target:
                return True
            elif target<arr[mid]:
                high=mid-1
            else: 
                low=mid+1
        return False

class Solution2:
    def searchMatrix(self, matrix, target: int) -> bool:
        if len(matrix)<len(matrix[0]):
            for i in range(len(matrix)):
                if self.binary_search(matrix[i], target):
                    return True
            return False
        else:
            for i in range(len(matrix[0])):
                if self.binary_search_vertical(matrix, i, 0, len(matrix)-1, target):
                    return True
        return False       
        
    def binary_search(self, arr, target):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(high+low)//2
            if arr[mid]==target:
                return True
            elif target<arr[mid]:
                high=mid-1
            else: 
                low=mid+1
        return False
                
    def binary_search_vertical(self, matrix, index, low, high, target):
        while low<=high:
            mid=(high+low)//2
            if matrix[mid][index]==target:
                return True
            elif target<matrix[mid][index]:
                high=mid-1
            else:
                low=mid+1
        return False

    def brute(self, matrix, target: int) -> bool:
        self.w=len(matrix[0])
        self.h=len(matrix)
        self.m=[[False for x in matrix[0]] for y in matrix]
    
        return self.helper(matrix, target, 0,0)
    
    def helper(self, matrix, target, i, j):
        if self.m[i][j]:
            return False
        current=matrix[i][j]
        if target==current:
            return True
        if target>current:
            if i+1<self.h:
                if self.helper(matrix, target, i+1, j):
                    return True
            if j+1<self.w:
                if self.helper(matrix, target, i, j+1):
                    return True
        self.m[i][j]=True
        return False


class Solution3:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        return self.helper(0, 0, len(matrix)-1, len(matrix[0])-1, matrix, target)
    
    
    def helper(self, top, left, bottom, right, matrix, target):
        if left>right or top>bottom:
            return False
        elif target<matrix[top][left] or target>matrix[bottom][right]:
            return False
        
        mid=(right+left)//2
        i=top
        while i < bottom+1 and matrix[i][mid]<=target:
            if matrix[i][mid]==target:
                return True
            i+=1

        return self.helper(i, left, bottom, mid-1, matrix, target) or self.helper(top, mid+1, i-1, right, matrix, target)


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)