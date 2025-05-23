# O(n) time | O(n) space
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         leftMax = [0 for _ in height]
#         rightMax = [0 for _ in height]

#         leftMax[0] = height[0]
#         rightMax[-1] = height[-1]

#         for idx in range(1, len(height)):
#             leftMax[idx] = max(leftMax[idx - 1], height[idx])

#         for idx in range(len(height) - 2, -1, -1):
#             rightMax[idx] = max(rightMax[idx + 1], height[idx])
        
#         maxArea = 0
#         for idx in range(1, len(height) - 1):
#             currentArea = min(leftMax[idx], rightMax[idx]) - height[idx]
#             maxArea += currentArea if currentArea > 0 else 0
#         return maxArea



class Solution:
    # def trap(self, height: List[int]) -> int:
    #     maxLeft = height[0]
    #     maxRight = height[-1]
    #     maxWater = 0
    #     left = 0
    #     right = len(height) - 1
        
    #     while left < right:
    #         maxLeft = max(maxLeft, height[left])
    #         maxRight = max(maxRight, height[right])

    #         if height[left] < height[right]:
    #             currentWater = maxLeft - height[left]
    #             left += 1
    #         else:
    #             currentWater = maxRight - height[right]
    #             right -= 1

    #         maxWater += currentWater
    #     return maxWater

    def trap(self, height: List[int]) -> int:
        leftMax = 0
        maxRight = 0
        maxWater = 0

        left = 0
        right = len(height) - 1

        while left < right:
            leftMax = max(leftMax, height[left])
            maxRight = max(maxRight, height[right])

            # if height[left] < height[right]:
            if leftMax < maxRight:
                maxWater += (leftMax - height[left])
                left += 1
            else:
                maxWater += (maxRight - height[right])
                right -= 1
        return maxWater
