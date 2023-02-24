class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        operation = [0] * ( len(s) + 1)

        for start,end,direction in shifts:
            if direction == 1:
                operation[start] += 1
                operation[end + 1] -= 1
            else:
                operation[start] -= 1
                operation[end + 1] += 1
        operation.pop()
        prefix = 0
        prefix_sum = []
        for num in operation:
            prefix += num
            prefix_sum.append(prefix)

        ans = []
        for move,letter in  zip(prefix_sum,s):
            ASKI = ord(letter) + move
            ASKI = (ASKI - 97) % 26 + 97
            ans.append(chr(ASKI))
            
        return "".join(ans)