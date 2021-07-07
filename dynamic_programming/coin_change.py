
class CoinChange(object):
    '''
    time: O (n*m), target*coins
    space: O N, target
    '''
    def answer(self, coins, amount):
        amount_list = [0] + [float('inf')]*amount
        # amount_list = [float('inf')]*amount
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    amount_list[i] = min(amount_list[i], amount_list[i-coin] + 1)
        if amount_list[-1] == float('inf'):
            return -1
        return amount_list[-1]
    
    '''
    good recursion problem
    time: target^coins, because worst case each coin has targer responses and the responses will need to be evaluated by the other coins
    '''
    def brute(self, coins, target):
        answer = self.brute_helper(coins, target)
        if answer==float('inf'):
            return -1
        else:
            return answer
        
    def brute_helper(self, coins, target):
        if target==0:
            return 0
        count=float('inf')
        for coin in coins:
            if coin<=target:
                count=min(count, 1+self.brute_helper(coins, target-coin))
        return count


# print(divmod(11,1))
coins = [2,5,10]
amount=3
x = CoinChange()
print(x.answer(coins, amount))
print(x.brute(coins, amount))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
