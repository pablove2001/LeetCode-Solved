def main(s):
    stack = []
    for c in list(s):
        if stack != [] and abs(ord(stack[-1]) - ord(c)) == 32:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

s = 'cCaAbBssSsMm'
print(main(s))