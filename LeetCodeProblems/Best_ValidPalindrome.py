def isPalindrome( s: str) -> bool:
    is_Palindrome = True

    i = 0
    j = len(s)-1
    
    while i < j:

        index_Found = CheckForIsAlNum(s,i,j)
        i = index_Found[0]
        j = index_Found[1]

        if s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1


    return is_Palindrome

def CheckForIsAlNum(s: str, i, j):
    found = False
    index_found = [0, 0]
    while found == False and i < j:

        if s[i].isalnum() and s[j].isalnum():
            found = True
            index_found = [i ,j]
        
        if s[i].isalnum() == False:
            i += 1

        if s[j].isalnum() == False:
            j -= 1
    
    return index_found

s = "A man, a plan, a canal: Panama"
print(f"is Palindrome - {isPalindrome(s)}")


