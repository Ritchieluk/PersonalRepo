# Brute force method for counting the bits in a binary word
# O(n) where n is number of bits to represent integer x
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print("Count Bits: {}".format(count_bits(12740)))


# Bruce force method for determining the parity of a binary word.
# O(n) where n is number of bits to represent integer x
def brute_force_parity(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>=1
    return result

print("Brute Force Parity{}".format(brute_force_parity(12740)))


# More efficient method for determining the parity of an binary word
# O(n) where n is number of bits set to 1 in x
def drop_bit_parity(x: int)-> int:
    result = 0
    while x:
        result ^= x & 1
        x &= x-1 # drop the lowest set bit in the word
    return result

print("Drop Bit Parity{}".format(drop_bit_parity(12740)))


