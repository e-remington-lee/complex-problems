from utilities import to_string


class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        self.sum = 0
        cur = root

        return self.helper(cur, False)

    def helper(self, cur, left):
        if not cur:
            return 0

        if cur.left or cur.right:
            l = r = 0
            if cur.left:
                l = self.helper(cur.left, True)
            if cur.right:
                r = self.helper(cur.right, False)
            return l + r
        else:
            if left:
                return cur.val
            else:
                return 0


flashcard = to_string.file_to_string(__file__)
print(flashcard)
