def validParenthesis(s):
    if len(s)<2:
        return False

    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']
    stack = []

    for i in s:
        if i in open_bracket:
            stack.append(i)

        elif i in close_bracket:
            if bool(stack):
                index_close = close_bracket.index(i)
                if stack[-1]==open_bracket[index_close] :
                    stack.pop()
                else:
                    return False
            else:
                return False

    if stack:
        return False
    else:
        return True

print(validParenthesis('){'))
