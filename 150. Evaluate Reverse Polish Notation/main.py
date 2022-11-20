class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ('+', '-', '*', '/'):
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif tokens[i] == '-':
                    pas = int(stack.pop())
                    stack.append(int(stack.pop()) - pas)
                elif tokens[i] == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                else:
                    pas = int(stack.pop())
                    stack.append(int(int(stack.pop()) / pas))
        return stack.pop()