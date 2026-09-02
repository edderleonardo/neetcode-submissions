"""
You are given a binary array nums, return the maximum number of
consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]

Output: 3

Example 2:

Input: nums = [1,0,1,1,0,1]

Output: 2
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        [1, 1, 0, 1, 1, 1]
        [1, 0, 1, 1, 0, 1]
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        """

        # max_element = count_elem = 0
        max_ones = 0
        ones_found = 0

        for num in nums:
            print("num => ", num)
            if num == 0:
                print("reset max_ones")
                # max_ones = 0
                ones_found = 0
            else:
                ones_found += 1
                print("ones_found", ones_found)
                # como saco el maximo?
                if ones_found > max_ones:
                    print("Remplaza")
                    max_ones = ones_found
                # max_ones = max(max_ones, ones_found)
        return max_ones