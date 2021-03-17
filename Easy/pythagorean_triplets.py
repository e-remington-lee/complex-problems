# Hi, here's your problem today. This problem was recently asked by Uber:

# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 5^2 + 12^2 = 13^2.

class Solution:
    def answer(self, li):
        # a2 + b2 = c2, 
        squared = {x**2 for x in li}
        for x in li:
            for y in li:
                ans = x**2 + y**2
                if ans in squared:
                    return [x,y]
        return [0,0]


def main():
    li = [3,4,5,13,10]
    ans = Solution().answer(li)
    ans2 = Solution().answer2(li)
    print(ans)
    print(ans2)

main()