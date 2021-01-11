PRECOMPUTED = {
    0b0000: 0,
    0b0001: 1,
    0b0010: 1,
    0b0011: 0,
    0b0100: 1,
    0b0101: 0,
    0b0110: 0,
    0b0111: 1,
    0b1000: 1,
    0b1001: 0,
    0b1010: 0,
    0b1011: 1,
    0b1100: 0,
    0b1101: 1,
    0b1110: 1,
    0b1111: 0
}

def parity(x):
    mask_size = 4
    bit_mask = 0xF
    return (PRECOMPUTED[x >> (3 * mask_size)] ^
            PRECOMPUTED[(x >> (2 * mask_size)) & bit_mask] ^ 
            PRECOMPUTED[(x >> mask_size) & bit_mask] ^
            PRECOMPUTED[x & bit_mask])

print(parity(0b01110001110001))
print(parity(0b01110001110011))