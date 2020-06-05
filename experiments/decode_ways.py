from itertools import chain, combinations

def powerset(iterable):
             s = list(iterable)
             return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))
 

class Solution:
    def numDecodings(self, s: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        mapping = {}
        count = 1
        for index,val in enumerate(letters):
            mapping[index+1] = val
            count+=1
        
        print(mapping)
        sets = list(set([ "".join(i) for i in list(powerset(s))]))
        ways = 0
        print(sets)
        for i in sets:
            if mapping.get(int(i)):
                ways+=1
        
        
        
        return ways
    



s = Solution()


print(s.numDecodings("226"))
        
        
        
        