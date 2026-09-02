class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        +: Sum previos two scores
        D: New item, doble of previos score
        C: invalid previos score, removing 

        example:
        ["1","2","+","C","5","D"]
        iterations:
            1: [1]
            2: [1, 2]
            +: [1, 2, 3]
            C: [1, 2]
            5: [1, 2, 5]
            D: [1, 2, 5, 10]
        
        output: 18 (sum)
        """
        stack = []
        if not operations:
                return 0
        for num in operations:
            if num == "+":
                res = stack[-1] + stack[-2]
                stack.append(res)
            elif num == "D":
                stack.append(stack[-1] * 2)
            elif num == "C":
                stack.pop()
            else:
                stack.append(int(num))
            
        return sum(stack)

        