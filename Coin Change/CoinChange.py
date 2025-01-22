class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * amount
        dp.append(0)

        #11:0
        

        for value in range(amount-1, -1, -1):
            min_coins = float("inf")
            for coin in coins:
                if value+coin <= amount:
                    min_coins= min(min_coins, dp[value+coin])
            
            dp[value] = 1+min_coins

        return dp[0] if dp[0] != float("inf") else -1
