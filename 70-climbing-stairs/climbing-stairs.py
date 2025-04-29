class Solution:
    def climbStairs(self, n: int) -> int:
        noOfSteps = [0 for n in range(n + 1)]
        noOfSteps[n] = 1
        noOfSteps[n - 1] = 1

        for idx in range(n - 2, -1, -1):
            noOfSteps[idx] = noOfSteps[idx + 1] + noOfSteps[idx + 2]
        
        return noOfSteps[0]

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        noOfSteps = [0 for _ in range(n)]
        noOfSteps[n - 1] = 1
        noOfSteps[n - 2] = 2

        for idx in range(n - 3, -1, -1):
            noOfSteps[idx] = noOfSteps[idx + 1] + noOfSteps[idx + 2]
        
        return noOfSteps[0]