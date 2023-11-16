class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        composite_nums = {}
        square_root = int(n ** 0.5)
        for base in range(2, square_root + 1):
            if base not in composite_nums:
                for multiple in range(base*base, n, base):
                    composite_nums[multiple] = 1
        
        return n - 2 - len(composite_nums)


from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)