# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:

    def rotate(self, nums, start, end):

        while(start < end):

            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            end -= 1
            start += 1
        
        return " ".join(nums)

    def reverseWords(self, s: str) -> str:

        str_array = s.split()
        len_array = len(str_array)

        if len_array - 1 > 0:
            return Solution.rotate(self, str_array, 0, len_array - 1)
        else:
            return " ".join(str_array)


nums = "a good   example"
k = 3
sol = Solution()
result = sol.reverseWords(nums)
print(f"Result - {result}")

