from nose.tools import assert_equal
import sys

class MinHeap:
    def __init__(self):
        self.array = []

    def insert(self, val):
        if val is None:
            raise TypeError('key cannot be None')
        self.array.append(val)
        index = len(self.array) - 1
        self._bubble_up(index)

    def peek_min(self):
        return None if len(self.array) == 0 else self.array[0]

    def extract_min(self):
        if len(self.array) == 0:
            return None
        if len(self.array) == 1:
            return self.array.pop()

        min = self.array.pop(0)
        end = self.array.pop()
        self.array.insert(0, end)
        self._bubble_down(0)

        return min

    def _bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.array[index] < self.array[parent_index]:
            self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
            return self._bubble_up(parent_index)

    def _bubble_down(self, index):
        smaller_index = self._find_smaller_child(index)
        if smaller_index == -1:
            return
        if self.array[smaller_index] < self.array[index]:
            self.array[smaller_index], self.array[index] = self.array[index], self.array[smaller_index]
            self._bubble_down(smaller_index)

    def _find_smaller_child(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        if right >= len(self.array):
            if left >= len(self.array):
                return -1
            else:
                return left
        else:
            if self.array[left] < self.array[right]:
                return left
            else:
                return right

class TestMinHeap(object):
    def test_min_heap(self):

        heap = MinHeap()

        assert_equal(heap.peek_min(), None)

        assert_equal(heap.extract_min(), None)

        heap.insert(20)

        assert_equal(heap.array[0], 20)

        heap.insert(5)

        assert_equal(heap.array[0], 5)

        assert_equal(heap.array[1], 20)

        heap.insert(15)

        assert_equal(heap.array[0], 5)

        assert_equal(heap.array[1], 20)

        assert_equal(heap.array[2], 15)

        heap.insert(22)

        assert_equal(heap.array[0], 5)

        assert_equal(heap.array[1], 20)

        assert_equal(heap.array[2], 15)

        assert_equal(heap.array[3], 22)

        heap.insert(40)

        assert_equal(heap.array[0], 5)

        assert_equal(heap.array[1], 20)

        assert_equal(heap.array[2], 15)

        assert_equal(heap.array[3], 22)

        assert_equal(heap.array[4], 40)

        heap.insert(3)

        assert_equal(heap.array[0], 3)

        assert_equal(heap.array[1], 20)

        assert_equal(heap.array[2], 5)

        assert_equal(heap.array[3], 22)

        assert_equal(heap.array[4], 40)

        assert_equal(heap.array[5], 15)

        mins = []

        while heap.array:
            mins.append(heap.extract_min())
        assert_equal(mins, [3, 5, 15, 20, 22, 40])
        print('Success: test_min_heap')

    

def main():
    test = TestMinHeap()
    test.test_min_heap()

if __name__ == '__main__':
    main()