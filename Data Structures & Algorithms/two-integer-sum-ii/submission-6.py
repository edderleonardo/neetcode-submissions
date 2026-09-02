"""
[2, 7, 11, 15], target = 9


"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            total = numbers[start] + numbers[end]
            # print(total)
            if total == target:
                # print("start:", start, "→ valor:", numbers[start])
                # print("end:", end, "→ valor:", numbers[end])
                return [start + 1, end + 1]
            elif total > target:
                end -= 1
            else:
                start += 1
        return []

                
        