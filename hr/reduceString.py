# Complete the superReducedString function below.
def superReducedString(s):
    stack = []
    for c in s:
        if len(stack) != 0:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    if len(stack) == 0:
        return "Empty String"
    else:
        return "".join(stack)

if __name__ == '__main__':
    s = ""

    result = superReducedString(s)
    print(result)