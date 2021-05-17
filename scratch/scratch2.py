class Sorting(object):
    def merge_sort(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            left=arr[:mid]
            right=arr[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            k=i=j=0
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
                k+=1
                j+=1
        return arr

    def quick_sort(self, arr):
        low=0
        high=len(arr)-1
        return self.__quick_sort(low, high, arr)
    
    def __quick_sort(self, low, high, arr):
        if low<high:
            p = self.__partition(low, high, arr)
            self.__quick_sort(low, p-1, arr)
            self.__quick_sort(p+1, high, arr)
        return arr
    
    def __partition(self, low, high, arr):
        par = arr[high]
        for i in range(low, high):
            if arr[i]<par:
                arr[low], arr[i] = arr[i], arr[low]
                low+=1
        arr[low], arr[high] = arr[high], arr[low]
        return low

    def bubble_sort(self, arr):
        l = len(arr)
        for i in range(l):
            for j in range(l-i-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1]=arr[j+1], arr[j]
        return arr

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_index=i
            for j in range(i, len(arr)):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[min_index], arr[i]=arr[i], arr[min_index]
        return arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr
           
    def heap_sort(self, arr):
        n = len(arr)

        for i in range(n//2+1, -1, -1):
            self.__heapify(arr, n, i)
            
        for i in range(n-1, 0, -1):
            arr[0], arr[i]=arr[i],arr[0]
            self.__heapify(arr, i, 0)
        return arr

    def __heapify(self, arr, n, i):
        largest=i
        left=2*i+1
        right=2*i+2

        if left < n and arr[left]>arr[largest]:
            largest=left
        
        if right<n and arr[right]>arr[largest]:
            largest=right

        if i!=largest:
            arr[i], arr[largest]=arr[largest],arr[i]
            self.__heapify(arr, n, largest)
            
def main():
    arr = [4, 2, 6, 7, 3, 9, 1, 8]
    s = Sorting()
    print(s.bubble_sort(arr))
    arr = [4, 2, 6, 7, 3, 9, 1, 8]
    print(s.insertion_sort(arr))
    arr = [4, 2, 6, 7, 3, 9, 1, 8]
    print(s.selection_sort(arr))
    arr = [4, 2, 6, 7, 3, 9, 1, 8]
    print(s.merge_sort(arr))
    arr = [4, 2, 6, 7, 3, 9, 1, 8]
    print(s.quick_sort(arr))
    arr = [4, 2, 6, 7, 3, 9, 1, 8]
    print(s.heap_sort(arr))

main()