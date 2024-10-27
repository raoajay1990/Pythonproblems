# 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

def isSubsequence(s: str, t: str) -> bool:

    if s in t:
        return True
    
    exists_Counter = 0
    i = 0
    j = 0

    while(i<len(s) and j<len(t)):

        if s[i] == t[j]:
            i += 1
            j += 1

            exists_Counter += 1
        else:
            j += 1

    return True if exists_Counter == len(s) else False

s='abc'
t='ahbgdc'
print(f"{s} exists in {t} -> {isSubsequence(s,t)}")

s='aec'
t='ahbgdc'
print(f"{s} exists in {t} -> {isSubsequence(s,t)}")