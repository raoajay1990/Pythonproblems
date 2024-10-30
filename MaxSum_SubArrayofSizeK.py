def maxSumOfSubArray(nums, k):
    initial = nums[0]

    if len(nums) < k:
        return 0
    
    max_sum = sum(nums[:k])
    

    for i in range(1,len(nums) -k +1):

        new_sum = max_sum + nums[i+k -1] - initial
        max_sum = max(max_sum, new_sum)
        initial = nums[i]

    return max_sum

nums = [100, 200, 300, 400]
k =2
max_sum = maxSumOfSubArray(nums, 2)
print(max_sum)
