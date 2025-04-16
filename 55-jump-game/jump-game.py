class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0

        for idx in range(0, len(nums) - 1):
            maxJump = max(maxJump, idx + nums[idx])
            if idx == maxJump:
                return False
        
        return True