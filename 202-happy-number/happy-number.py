class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n

        while True:
            slow = self.sumOfSquare(slow)
            fast = self.sumOfSquare(fast)
            fast = self.sumOfSquare(fast)

            if fast == 1:
                return True

            if fast == slow:
                return False

    def sumOfSquare(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            output += (digit ** 2)
            n = n // 10
        return output
            