
# Sorting is usually between the worst case (brute force) and the best case scenario
# https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/#:~:text=%2B1%5D%20%3D%20temp-,Quicksort,greater%20numbers%20on%20the%20right.
class Sorting(object):
    # O(n*2), constant space
    # https://www.youtube.com/watch?v=xli_FI7CuzA
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    # O(n*2), constant space
    # https://www.youtube.com/watch?v=JU767SDMDvA
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    # O(n*2), constant space
    # https://www.youtube.com/watch?v=g-PGLbMth_g
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[min_index]>arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    #https://www.youtube.com/watch?v=4VqmGXwpLqc
    #https://www.geeksforgeeks.org/merge-sort/
    # average, o(n*log(n)), space O n (sometimes)
    def merge_sort(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            self.merge_sort(left)
            self.merge_sort(right)

            i=j=k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                arr[k]=left[i]
                k+=1
                i+=1
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
        return arr

    # https://www.geeksforgeeks.org/heap-sort/   
    # https://www.youtube.com/watch?v=2DmK_H7IdTo
    # https://www.youtube.com/watch?v=t0Cq6tVNRBA
    # average, o(n*log(n))
    def heap_sort(self, arr):
        n = len(arr)

        for i in range(n//2-1, -1, -1):
            self.__heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.__heapify(arr, i, 0)
            
        return arr

    def __heapify(self, arr, n, i):
        largest = i
        left = 2*i+1
        right = 2*i+2

        if left < n and arr[largest] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.__heapify(arr, n, largest)

    # figure out better way to calculate pivot
    # worst O(n*2) if you pick the worst pivot each time
    # average, o(n*log(n)), average space is log(n) with worst being n if we get a sorted list
    # https://www.youtube.com/watch?v=Hoixgm4-P4M
    def quick_sort(self, arr, low, high):
        if high>low:
            pi = self.__partition(arr, low, high)
            self.quick_sort(arr, low, pi-1)
            self.quick_sort(arr, pi+1, high)
        return arr

    # pass by object, the arr is a mutiple object that is being modified in the function, low is an integer which is also being modified, yet
    # only the arr is changed outside of this scope while the variable low is not! 
    def __partition(self, arr, low, high):
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[low], arr[j] = arr[j], arr[low]
                low+=1
        arr[low], arr[high] = arr[high], arr[low]
        return low

sort = Sorting()
# li = [2, 5, 3, 8, 1, 6]
# print(sort.bubble_sort(li))
# li = [2, 5, 6, 8, 1, 3]
# print(sort.selection_sort(li))
# li = [2, 5, 6, 8, 1, 3]
# print(sort.insertion_sort(li))
li = [2, 5, 3, 8, 1, 6]
print(sort.quick_sort(li, 0,len(li)-1))
# li = [2, 5, 6, 8, 1, 3]
# print(sort.merge_sort(li))
# li = [2, 5, 6, 8, 1, 3,3,3,3,]
# print(sort.heap_sort(li))
# import sys
# sys.path.append(".")
# from utilities import to_string
# flashcard=to_string.file_to_string(__file__)
# print(flashcard)