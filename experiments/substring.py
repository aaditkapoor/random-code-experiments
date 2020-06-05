# 1. isPalindrome(str) -> bool
# 2. length(str) -> int (get the length of the longest palindrome)
# 3. getSubStrings() -> List[str] (get all the substrings)
class Solution:
    def longestPalindrome(self,s: str) -> str:

        length = len(s)
        table = [ [None] * length for _ in range(length) ] # create a 2d matrix


        # 1
        def isPalindrome(low, high):
            # corner cases
            # if len(str) == 1, then always true (low == high)
            # if low+1 == high and str is same then true. (two char that are palindrome)
            # if outermost are different , then false else we check str[low+1:high-1]

            if table[low][high] is not None: # i.e we have a value
                return table[low][high]

            # case 1 (low == high)
            if low == high:
                return True
            elif low + 1 == high: # case 2 (low + 1 == high) (2 characters are palindrome)
                return s[low] == s[high]

            # case 3 (False if outermost are not equal, if True then extract recursively +1 and -1)
            outer = False if str[low] != str[high] else isPalindrome(low+1, high-1)
            table[low][high] = outer
            return outer

        # 2 (generate all the substrings)
        def getSubStrings():
            strings = []
            N = length
            found = False

            # str is empty
            if not str:
                return ['']

            for i in range(length, 0, -1):
                found = False
                for sub in range(length - 1 + 1):
                    if isPalindrome(sub, sub + 1 - 1):
                        found = True
                        strings.append(s[sub:sub+1])
                if found:
                    break
                
            return strings


        return getSubStrings()
        
            
            

        
