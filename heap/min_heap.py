from __future__ import division
from nose.tools import assert_equal
import sys


class MinHeap(object):
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def extract_min(self):
        if not self.array:
            return None

        if len(self.array) == 1:
            return self.array.pop(0)
        minimum = self.array[0]
        # Move the last element to the root
        self.array[0] = self.array.pop(-1)
        self._bubble_down(index=0)

        return minimum


    def peek_min(self):
        return self.array[0] if self.array else None

    def insert(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        self.array.append(key)
        self._bubble_up(index=len(self.array) - 1)


    def _bubble_up(self, index):
        if index == 0:
            return
        index_parent = (index - 1) // 2
        if self.array[index] < self.array[index_parent]:
            # Swap the indices and recurse
            self.array[index], self.array[index_parent] = self.array[index_parent], self.array[index]
            self._bubble_up(index_parent)

    def _bubble_down(self, index):
        min_child_index = self._find_smaller_child(index)
        if min_child_index == -1:
            return
        if self.array[index] > self.array[min_child_index]:
            # Swap the indices and recurse
            self.array[index], self.array[min_child_index] = self.array[min_child_index], self.array[index]
            self._bubble_down(min_child_index)

    def _find_smaller_child(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        # No right child
        if right_child_index >= len(self.array):
            #No left child
            if left_child_index >= len(self.array):
                return -1
            # Left child only
            else:
                return left_child_index
        else:
            # Compare left and right children
            if self.array[left_child_index] < self.array[right_child_index]:
                return left_child_index
            else:
                return right_child_index



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

        while heap:
            mins.append(heap.extract_min())
        assert_equal(mins, [3, 5, 15, 20, 22, 40])
        print('Success: test_min_heap')

    

def main():
    test = TestMinHeap()
    test.test_min_heap()

if __name__ == '__main__':
    main()