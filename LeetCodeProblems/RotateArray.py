# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

class Solution:

    def reverseInput(self, nums, start, end):

        while(start<end):
            try:
                temp = nums[start]  
                nums[start] = nums[end]
                nums[end] = temp

                start += 1
                end -= 1
            except IndexError as e:
                end -= 1
                start -= 1
            
    def rotate(self, nums, k: int) :
        # result = [1]* len(nums)
        # for i in range(len(nums)-1 , -1,-1):
        #     result[i] = nums[i - k]
        # return result

        # in space solution
        Solution.reverseInput(self, nums, 0, len(nums)-1)
        Solution.reverseInput(self, nums,0,k-1)
        Solution.reverseInput(self, nums, k, len(nums)-1)

        return nums
        

nums = [1,2]
k = 3
sol = Solution()
result = sol.rotate(nums,k)
print(f"Result - {result}")

# nums = [-1]
# k = 2
# sol = Solution()
# result = sol.rotate(nums,k)
# print(f"Result - {result}")

# nums = [-1,-100,3,99]
# k=2
# sol = Solution()
# result = sol.rotate(nums,k)
# print(f"Result - {result}")

# nums = [1,2,3,4,5,6,7]
# k=3
# sol = Solution()
# result = sol.rotate(nums,k)
# print(f"Result2 - {result}")