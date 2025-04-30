class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cols = amount + 1
        rows = len(coins) + 1

        coinChange = [0 for _ in range(cols)]
        coinChange[0] = 1

        for coin in coins:
            for col in range(1, cols):
                if coin > col:
                    continue
                coinChange[col] = coinChange[col] + coinChange[col - coin]
        return coinChange[-1]
