'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

Time: O n,
Space, constant
'''
class BestStockPrice(object):
    def answer(self, arr):
        buy=0
        money=0
        for i in range(1, len(arr)):
            if arr[i]>arr[buy]:
                money=max(money, arr[i]-arr[buy])
            else:
                buy=i
        return money

    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0        
        for x in prices[1:]:
            if x < buy:
                buy = x
            else:
                profit = max(profit, x - buy)
        return profit
           

    def brute(self, arr):
        money=0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j]>arr[i]:
                    money=max(money, arr[j]-arr[i])
        return money
            




arr1=[7,11,1,5,3,6,4]
x=BestStockPrice()
print(x.answer(arr1))
import sys
sys.path.append(".")
from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)