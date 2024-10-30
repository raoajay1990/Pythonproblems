# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome , and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def isPalindrome(x: int) -> bool:
    x = str(x)
    i = 0
    j = len(x) - 1

    while i < j:

        if x[i] != x[j]:
            return False
        else:
            i += 1
            j -= 1

    
    return True

x = 121
print(f"Is {x} palindrome ? : {isPalindrome(x)}")
x = -121
print(f"Is {x} palindrome ? : {isPalindrome(x)}")
x=10
print(f"Is {x} palindrome ? : {isPalindrome(x)}")