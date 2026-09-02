"""
['W', 'a', 's', 'i', 't', 'a', 'c', 'a', 'r', 'o', 'r', 'a', 'c', 'a', 't', 'I', 's', 'a', 'w']

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        print("start")
        result = [char.lower() for char in s if char.isalnum()]  # only chars
        print("result ", result)
        start, end = 0, len(result) - 1
        while start < end:
            print(result[start])
            print(result[end])
            if result[start] != result[end]:
                return False

            start += 1
            end -= 1

        return True