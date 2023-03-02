class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertAndReverse(binary):
            inverted = ["1" if num == "0" else "0" for num in binary ]
            inverted.reverse()
            return "".join(inverted)

        def binaryString(strs):
            if len(strs) >= k:
                return strs[k-1]

            strs = strs + "1" + invertAndReverse(strs)
            return binaryString(strs)

        return binaryString("0")
    