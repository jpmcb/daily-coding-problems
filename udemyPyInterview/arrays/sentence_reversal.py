# Given a string of words, 
# reverse all the words. For example:

# Given:
# 'This is the best'

# Return:
# 'best the is This'

# As part of this exercise you should remove 
# all leading and trailing whitespace. So that inputs such as:
# '  space here'  and 'space here      '

# both become:
# 'here space'

def reverse_words(s):
    return " ".join(reversed(s.split()))