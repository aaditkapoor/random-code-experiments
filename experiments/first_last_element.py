from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        
        nums = list(map(lambda x: str(x), nums))
        indices = [x for x,v in enumerate(nums) if v == str(target)]
        
        return [indices[0], indices[-1]]
        
