class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coinCache = { 5: 0, 10: 0, 20: 0 }

        for bill in bills:
            if not self.isSellable(bill, coinCache):
                return False
        return True

    def isSellable(self, amount, coinCache):
        coinCache[amount] += 1
        returnAmount = amount - 5
        availableCoins = [20, 10, 5]
        coinIdx = 0

        while returnAmount > 0 and coinIdx < len(availableCoins):
            coin = availableCoins[coinIdx]
            if coin > returnAmount or coinCache[coin] == 0:
                coinIdx += 1
                continue
            else:
                noOfCoinsRequired = min(returnAmount // coin, coinCache[coin])
                coinCache[coin] -= noOfCoinsRequired
                returnAmount -= (coin * noOfCoinsRequired)
                coinIdx += 1

        return returnAmount == 0