# Using recursion, reverse a given string

def reverse(s):
    if len(s) == 1:
        return s

    # Slice the string from 2nd to last index 
    return reverse(s[1:]) + s[0]

print(reverse('hello world'))