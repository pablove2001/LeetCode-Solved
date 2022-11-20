def main(s):
    s = list(s)
    print(s)


def sumArr(s):
    nums = []
    op = []
    for i in s:
        if i not in ('(', ')', ' '):
            if i in ('-', '+'):
                op.append(i)
            else:
                nums.append(int(i))
    for i in op[::-1]:
        if i == '+':
            n = nums.pop()
            nums[-1] += n
        else:
            n = nums.pop()
            nums[-1] -= n
    if len(nums) == 0:
        return 0
    return nums[0]

            
    





s = "(1 + (44 + 5+ 2) - 3) +( 6 +  8 )"
print(main(s))