# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
from collections import Counter
def minWindow(s: str, t: str) -> str:

    if len(t) > len(s):
        return " "
    
    i = 0
    current_string = s[:len(t)]
    j = len(t) - 1
    window_size = len(s) + 1
    start_index, end_index = 0, 0
    is_Found = False
    t_counter = Counter(t)
    while i < len(s):
        while j < len(s):
            current_string_counter = Counter(current_string)
            
            if all(current_string_counter[ch] >= t_counter[ch] for ch in t_counter ):
                is_Found = True
                if window_size > len(current_string):
                    window_size = len(current_string)
                    start_index = i
                    end_index = j
                i += 1    
            else:
                
                j += 1
            
            current_string = s[i:j+1]
        i += 1

    return s[start_index:end_index+1] if is_Found else " "

s="aa"
t="aa"
print(minWindow(s,t))

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))

s = "a"
t = "a"
print(minWindow(s,t))

s = "a"
t = "aa"
print(minWindow(s,t))
