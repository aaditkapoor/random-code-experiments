# corner cases
# if len(str) == 1, then always true (low == high)
# if low+1 == high and str is same then true. (two char that are palindrome)
# if outermost are different , then false else we check str[low+1:high-1]

class Solution:
    def longestPalindrome(self,s: str) -> str:

        # initialize the table
        
        table = [ [False for _ in range(len(s))] for _ in range(len(s)) ]

        imax = jmax = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                k = j - i # distance

                # if diagonal table[i][i] and if length is less than 3 or check outer
                # and divide the substring (low+1:high-1)
                # For every possible palindrome put True in the table
                table[k][j] = s[k] == s[j] and ( j - k < 3 or table[k+1][j-1] )

                if table[k][j] and j - k + 1 > jmax - imax + 1:
                    imax = k # setting max i index
                    jmax = j # setting max j index

        return s[imax:jmax + 1] # max index i : j+1
    
    
