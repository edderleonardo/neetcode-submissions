"""
Input: nums = [3,2,2,3], val = 3
Output: k = 2, nums = [2,2,_,_]
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            print("read", read)
            print("num", nums[read])
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write
        