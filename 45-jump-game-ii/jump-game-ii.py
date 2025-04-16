class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        steps = nums[0]
        maxJump = nums[0]
        minJump = 0

        for idx in range(1, len(nums)):
            steps -= 1
            maxJump = max(maxJump, nums[idx] + idx)

            if steps == 0 or idx == len(nums) - 1:
                minJump += 1
                steps = maxJump - idx
        
        return minJump

        