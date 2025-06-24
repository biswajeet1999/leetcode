import math

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        res = 1

        # for idx in range(0, n):
        #     if idx % 2 == 0:
        #         res *= 5
        #     else:
        #         res *= 4

        noOfEvens = math.ceil(n / 2)
        noOfOdds = n - noOfEvens
        res = self.pow(5, noOfEvens) * self.pow(4, noOfOdds)  # (5 ** noOfEvens) * (4 ** noOfOdds)
        
        return res % (10**9 + 7)

    def pow(self, num, p):
        if p == 0:
            return 1
        if p == 1:
            return num
        res = 1
        
        while p:
            if p%2 == 0:
                num = (num * num)  % (10**9 + 7)
                p //= 2
            else:
                res =  (res * num)  % (10**9 + 7)
                p -= 1
        return res