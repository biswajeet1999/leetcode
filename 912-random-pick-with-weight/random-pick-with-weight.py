import random

class Solution:

    def __init__(self, w: List[int]):
        self.cumSum = []
        prevSum = 0

        for num in w:
            self.cumSum.append(prevSum + num)
            prevSum += num

    def pickIndex(self) -> int:
        randNumber = random.randint(1, self.cumSum[-1])

        resIdx = -1
        left = 0
        right = len(self.cumSum) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.cumSum[mid] >= randNumber:
                resIdx = mid
                right = mid - 1
            else:
                left = mid + 1
        return resIdx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()