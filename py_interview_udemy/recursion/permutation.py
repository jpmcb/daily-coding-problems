# Given a string, write a function that uses recursion to 
# output a list of all the possible permutations of that string.

# For example, given s='abc' the function should 
# return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# Note: If a character is repeated, treat each occurence 
# as distinct, for example an input of 'xxx' would return 
# a list with 6 "versions" of 'xxx'

def perm(s):
    if len(s) == 1:
        return [s]

    r = []
    for i, c in enumerate(s):
            
        # For every permutation resulting from Step 2 and 3 described above
        for p in perm(s[:i] + s[i+1:]):
            
            # Add it to output
            r += [c + p]
    
    return r

print(perm("abc"))