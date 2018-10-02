import unittest

# Counts the bits that are set to 1 in a number
# Example: 255 has 8 bits set to 1: (1111 1111)
# 254 has only 7 bits set to 1: (1111 1110)
def count_bits(x):
    num_bits = 0
    while x:
        # bitwise AND operation
        num_bits += x & 1
        # Shift the bits to the right by 1 bit 
        x >>= 1
    return num_bits

class Test(unittest.TestCase):
    def test_bitCount(self):
        self.assertTrue(1 == count_bits(1))
        self.assertTrue(8 == count_bits(255))
        self.assertTrue(7 == count_bits(254))

if(__name__ == "__main__"):
    unittest.main()