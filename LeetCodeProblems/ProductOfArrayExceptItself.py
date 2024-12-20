# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums) :
        product_array = [1] * len(nums)

        # Find the product of array by doing 2 steps
        # Find the prefix sum 
        # Find the Suffix sum 
        # Multiply prefix and Suffix

        # In this loop we will find the Prefix Sum buy starting from the left
        for i in range(1,len(nums)):
            product_array[i] = product_array[i-1] * nums[i-1]

        # Initializing right for Suffix sum
        right = nums[-1]

        # In this loop we will find the Suffix sum by starting from the right and multiply with left product
        for i in range(len(nums)-2, -1, -1):
            product_array[i] *= right
            right *= nums[i]

        return product_array

    




nums = [1,2,3,4]
sol = Solution()
result = sol.productExceptSelf(nums)
print(f"Result - {result}")

nums = [-1,1,0,-3,3]
result = sol.productExceptSelf(nums)
print(f"Result2 - {result}")