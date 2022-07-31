# Given an array of numbers consisting of daily stock prices, calculate the maximum amount 
# of profit that can be made from buying on one day and selling on another.

# In an array of prices, each index represents a day, and the value on that index represents the price of the stocks on that day.

# Note that you need to buy the stocks before you sell them so the day (index) indicating the buying price should be before the day 
# (index) indicating the selling price.

# My solution (I tried a better solution but...)

def buy_and_sell_stock_once(prices):
    max = 0
    for i in range(len(prices) - 1):
        for j in range (1, len(prices)):
            if i < j and prices[j] - prices[i] > max:
                max = prices[j] - prices[i]
    return max
  
# Educative solution 1 (similar to mine, but still better... sad
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_once(A):
  max_profit = 0
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[j] - A[i] > max_profit:
          max_profit = A[j] - A[i]
  return max_profit


# Educative solution 2
# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
  max_profit = 0.0
  min_price = float('inf')
  for price in prices:
    min_price = min(min_price, price)
    compare_profit = price - min_price
    max_profit = max(max_profit, compare_profit)
  return max_profit
