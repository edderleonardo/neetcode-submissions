class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # save values, not keys
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        

