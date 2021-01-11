# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress 
# it to become 'A4B4C5D2E4'. For this problem, you can falsely 
# "compress" strings of single or double letters. For instance, 
# it is okay for 'AAB' to return 'A2B1' even though this 
# technically takes more space.

# The function should also be case sensitive, 
# so that a string 'AAAaaa' returns 'A3a3'.

def compress(s):
    if len(s) == 0:
        return None

    result = ''
    count = 0
    prev = None
    
    index = 0
    while index < len(s):
        current = s[index]

        # Special case, first index
        if index == 0:
            result += current
            count += 1
            prev = current

        # special case, last index
        elif index == len(s) - 1:

            if current != prev:
                result += str(count)
                result += current
                result += str(1)
            else:
                count += 1
                result += str(count)

        # Normal iterative case
        else:
            if current != prev:
                result += str(count)
                result += current
                prev = current
                count = 1
            else:
                count += 1
            
        # advance the index to the next char
        index += 1

    return result

print(compress("AAABBBCCC"))
print(compress("AAaaaBBBBbbCcc"))
print(compress("AAb"))