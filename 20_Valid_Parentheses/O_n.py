class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for i in s:
            if i not in ['(', '{', '[']:
                if not stack:
                    return False
                else:
                    if mapper[i] == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(i)
            else:
                stack.append(i)
        return not stack 

