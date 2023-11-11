from Stack import Stack


# input: str
# output: ib_error : boolean
# output: location : int

def bracket_check(str):
    is_error = False
    location = []
    stack = Stack()

    for i in range(len(str)):
        s = str[i]
        if s == '(' or s == '[' or s == '{':
            stack.push(s)
        elif s == ')' or s == ']' or s == '}':
            p = ''
            if not stack.isEmpty():
                p = stack.pop()
            else:
                is_error = True

            if not ((p == '(') and (s == ')') or ((p == '[') and (s == ']')) or ((p == '{') and s == '}')):
                is_error = True
                location.append(i)

    if not stack.isEmpty():
        is_error = True

    return is_error, location


test_string = '[{(Hello)}]'
isError, locations = bracket_check(test_string)
print(f'error: {isError}')
print('location:', locations)
