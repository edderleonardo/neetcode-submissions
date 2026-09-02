class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        for read in range(len(arr)):
            if read == len(arr) - 1:
                arr[read] = -1
            else:
                arr[read] = max(arr[read + 1:])
        return arr
