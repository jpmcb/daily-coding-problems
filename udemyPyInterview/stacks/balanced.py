from stack import Stack

# Checks if a string has balanced parans in it
# For example, {[]} would return true. Ignores none paran chars
def balanced(s):
    opening = set('{[(')
    closing = set('}])')
    matches = set([('(', ')'), ('{', '}'), ('[', ']')])

    stack = Stack()

    # String is even
    for char in s:
        if char in opening:
            stack.push(char)
        elif char in closing:
            # Check to see if the match is at the top of the stack
            if stack.isEmpty():
                return False

            if (stack.pop(), char) not in matches:
                return False

    return stack.isEmpty()
        
# False
print(balanced("{(a{[ab]}}"))
# True
print(balanced('({([[][]])})'))
# False
print(balanced('({({[][]])}]'))