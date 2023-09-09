class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for ind, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                top = stack.pop()
                output[top] = ind - top
            stack.append(ind)

        return output
