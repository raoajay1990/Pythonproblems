# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        # words = ''.join(s.strip().split(" "))
        # normalized_text = "".join(s.strip())
        # words = normalized_text.split()
        if(len(words) > 0):
            return len(words[-1])


nums = "   fly me   to   the moon  "
sol = Solution()
result = sol.lengthOfLastWord(nums)
print(f"Result - {result}")
