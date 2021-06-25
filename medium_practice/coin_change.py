
class CoinChange(object):
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
    '''
    def brute(self, coins, amount):
        if amount==0:
            return 0
        response = float('inf')
        for coin in coins:
            if amount-coin>=0:
                response=min(response, self.recursive(coins, amount-coin)+1)
        if response == float('inf'):
            return -1
        else:
            return response


# print(divmod(11,1))
coins = [1,3,10]
amount=11
x = CoinChange()
print(x.answer(coins, amount))
print(x.brute(coins, amount))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)
