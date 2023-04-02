class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit = x ^ y
        shift = 1
        bit_len = len(bin(bit)) - 2
        num_bit = 0
        while bit_len > 0:
            if bit & shift:
                num_bit += 1
            shift = shift << 1
            bit_len -= 1

        return num_bit