class Solution:
    def checkIfExist(self, arr):
        doubles_set = set()
        for i in range(len(arr)):
            double_key = 2 * arr[i]
            half_key = arr[i] / 2
            if (double_key in doubles_set) or (half_key in doubles_set):
                return True
            doubles_set.add(arr[i])

        return False

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)