def array():
    n = 8
    target = [1, 5]
    stack = []
    operations = []
    j = 0
    for i in range(1, n+1):
        if j == max(target):
            break
        j += 1
        stack.append(i)
        operations.append("push")
        if i not in target:
            stack.pop()
            operations.append("pop")
    return stack, operations
print(array())
