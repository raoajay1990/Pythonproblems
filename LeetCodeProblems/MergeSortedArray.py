# Problem Statement

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


# Solution:
# Similar to merge sort, but no need for division since we have two arrays in non decreasing order 

def mergeSortedArray(left_array, right_array, n1, n2):

    i=n1-1
    j=n2-1
    k=len(left_array)-1

    while (i>=0 and j>=0):
        if(left_array[i] <= right_array[j]):
            left_array[k] = right_array[j]
            j = j - 1
        else:
            left_array[k] = left_array[i]
            j = j - 1
        k = k - 1

    while i >= 0:
            left_array[k] = left_array[i]
            k = k - 1
            i = i - 1
        
    while j >= 0:
            left_array[k] = right_array[j]
            k = k - 1
            j = j - 1

    

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

# nums1 = [0]
# nums2 = [1]
# m = 0
# n = 1

print("nums1 before sorting")
print(f"nums1 : {nums1}")

mergeSortedArray(nums1, nums2, m, n )

print(" nums1 after sorting")
print(f"{nums1}")

