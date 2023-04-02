class Solution:
    def findComplement(self, num: int) -> int:
        bit_mask = (2**(len(bin(num)) - 2)) - 1
        return bit_mask ^ num