class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_array = [0]
        for index, subtrahend in enumerate(prices):
            if index == len(prices) - 1:
                break
            max_sell = 0
            for minuend in prices[index + 1::]:
                if minuend - subtrahend > max_sell:
                    max_sell = minuend - subtrahend
            sell_array.append(max_sell)

        return max(sell_array)
