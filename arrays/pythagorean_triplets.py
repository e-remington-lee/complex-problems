'''
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.
'''

class Solution:
    def answer(self, li):
        squares = {x**2 for x in li}
        for i, x in enumerate(li):
            for y in li[i+1:]:
                if x**2+y**2 in squares:
                    return True
        return False


def main():
    li = [12, 10,5,4,3]
    ans = Solution().answer(li)
    print(ans)
    import sys
    sys.path.append(".")
    from utilities import to_string
    flashcard=to_string.file_to_string(__file__)
    print(flashcard)

main()