# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def isPalindrome( s: str) -> bool:
    new_str = ""
    for ch in s.lower():
        if ch.isalnum():
            new_str += ch
            
    is_Palindrome = True

    if len(s) == 1:
        return True

    i=0
    j=len(new_str) - 1

    while(i < j):
        if new_str[i] != new_str[j]:
            return False
        else:
            i += 1
            j -= 1

    return is_Palindrome

s = "A man, a plan, a canal: Panama"
print(f"is Palindrome - {isPalindrome(s)}")