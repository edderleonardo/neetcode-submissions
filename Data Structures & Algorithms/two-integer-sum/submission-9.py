class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force 
        """"
        total = len(nums)
        for i in range(total):
            for j in range(i + 1, total):
                # print(f"Este es i, {i}, {nums[i]}")
                # print(f"Este es j, {j}, {nums[j]}")
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []        
        """
        # using hashmap
        # complement k = target - value
        nums_to_index = {}
        for index, value in enumerate(nums):
            complement = target - value

            if complement in nums_to_index:
                return [nums_to_index[complement], index]
            
            nums_to_index[value] = index
        
        return []

