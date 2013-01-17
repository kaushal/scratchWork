def parenMatch(input):
    stack = []
    for char in input:
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
        elif char == '}' or char == ')' or char == ']':
            if stack[len(stack) - 1] == '(' and char == ')':
                stack.pop()
            elif stack[len(stack) - 1] == '{' and char == '}':
                stack.pop()
            elif stack[len(stack) - 1] == '[' and char == ']':
                stack.pop()
            else:
                print 'Returning false'
                return False

    if len(stack) == 0:
        return True
    else:
        return False

print parenMatch('[({}){}]')
