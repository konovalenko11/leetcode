from typing import List
import dis

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    min_price = prices[0]
    profit = 0

    for price in prices:
      if price < min_price:
        min_price = price

      if price - min_price > profit:
        profit = price - min_price
    return profit

f = Solution()

input = {
  'prices': [7,1,5,3,6,4]
}

print(f'Input: {input}')
print(f'Answer: {f.maxProfit(**input)}')