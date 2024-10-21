# 169. Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums) -> int:
        checked_nums = []
        for i in range(0, len(nums)):
            if nums[i] not in checked_nums:
                if nums.count(nums[i]) > len(nums)//2:
                    return nums[i]
                checked_nums.append(nums[i])


nums = [2,2,1,1,1,2,2]
sol = Solution()
result = sol.majorityElement(nums)
print(f"Result - {result}")