class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ')':
                if not stack:
                    return False
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif i == ']':
                if not stack:
                    return False
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif i == '}':
                if not stack:
                    return False
                if stack[-1] != '{':
                    return False
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        return True
