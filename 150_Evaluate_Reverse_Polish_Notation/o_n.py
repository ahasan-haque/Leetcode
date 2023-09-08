class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()
                result = eval(f'{a} {token} {b}')
                result = floor(result) if result > 0 else ceil(result)
                stack.append(str(result))
            else:
                stack.append(token)
        return int(stack.pop())
