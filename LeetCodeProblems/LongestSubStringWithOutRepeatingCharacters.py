# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    
    current_subString = s[0]
    i = 0
    j = i + 1
    longest_window = 1

    while i < len(s) - 1:

        while j < len(s):
            if s[j] not in current_subString:
                current_subString += s[j]
                longest_window = max(longest_window, len(current_subString))
                j += 1
            else:     
                i += 1
                j = i + 1
                current_subString = s[i]
        
        i += 1

        if longest_window == len(s):
            return longest_window



    return longest_window

s='dvdf'
print(f"{lengthOfLongestSubstring(s)}")
s = "au"
print(f"{lengthOfLongestSubstring(s)}")
s = "abcabcbb"
print(f"{lengthOfLongestSubstring(s)}")
s = "bbbbb"
print(f"{lengthOfLongestSubstring(s)}")
s = "pwwkew"
print(f"{lengthOfLongestSubstring(s)}")
