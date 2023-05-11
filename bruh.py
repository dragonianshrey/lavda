def r(word):
    stack = []
    for i in word:
        stack.append(i)
    r = ''
    while len(stack) > 0:
        r += stack.pop()
    return r
a=r("bruh")
print(a)
print("bruh")
