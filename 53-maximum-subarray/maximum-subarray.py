class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sumTilNow = nums[0]

        for idx in range(1, len(nums)):
            sumTilNow = max(sumTilNow + nums[idx], nums[idx])
            maxSum = max(maxSum, sumTilNow)
        return maxSum