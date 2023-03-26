class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = ptr = 0
        
        while right <= len(chars) :
            if right == len(chars) or chars[left] != chars[right]:
                if right - left > 1:
                    num = str((right - left))
                    chars[ptr] = chars[left]
                    ptr += 1
                    for n in num:
                        chars[ptr] = n
                        ptr += 1
                else:
                    chars[ptr] = chars[left]
                    ptr += 1
                left = right

                if right == len(chars):
                    break
            else:
                right += 1

        return ptr