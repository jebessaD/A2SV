class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        on_bits = [0]*32

        for num in nums:
            index = 0
            pos = num > 0
            num = abs(num)

            while num != 0:
                if num % 2 != 0 :
                    if pos:
                        on_bits[index] += 1
                    else:
                        on_bits[index] -= 1

                index += 1
                num = num >> 1
          
        new_bits = [bit %3 for bit in on_bits]
        sign = 1
        for i, bit in enumerate(new_bits):
            if bit:
                num = num | 1 << i
            if bit == 2:
                sign = - 1

        return num * sign