class ReverseString:
    # O(n), space O(n)
    def classic(self, s):
        li = list(s)
        i, j = 0, len(s)-1
        while i <= j:
            li[i], li[j] = li[j], li[i]
            i+=1
            j-=1
        return "".join(li)

    def pythonic(self, s):
        return s[::-1]


def quick_sort(arr):
    return qs_helper(arr, 0, len(arr)-1)

def qs_helper(arr, low, high):
    if low<high:
        pi = partition_highlow(arr, low, high)
        # pi = partition_lowhigh(arr, low, high)
        qs_helper(arr, pi+1, high)
        qs_helper(arr, 0, pi-1)
    return arr

def partition_lowhigh(arr, low, high):
    for x in range(low, high):
        if arr[x]<=arr[high]:
            arr[low], arr[x] = arr[x], arr[low]
            low+=1
    arr[low], arr[high] = arr[high], arr[low]
    return low

def partition_highlow(arr, low, high):
    for x in range(low, high):
        if arr[x]>=arr[high]:
            arr[low], arr[x] = arr[x], arr[low]
            low+=1
    arr[high], arr[low] = arr[low], arr[high]
    return low


print(quick_sort([5,3,1,6]))
