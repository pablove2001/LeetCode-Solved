def main(root):
    return maxDepth(root, 1)

def maxDepth(root, num):
    if root == None:
        return num
    return max(maxDepth(root.right, num+1), maxDepth(root.left, num+1))


root = []
print(main(root))