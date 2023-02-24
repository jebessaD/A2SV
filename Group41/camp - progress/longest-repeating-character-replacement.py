class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def findMaxLength(letter,s,k):
            left = 0
            max_size = 0
            for right in range(len(s)):
                if s[right] != letter:
                    k -= 1
                while k < 0:
                    if s[left] != letter:
                        k += 1
                    left += 1

                max_size = max(max_size, right - left + 1)

            return max_size

        letters = set(s)
        ans = 0
        for letter in letters:
            ans = max( ans , findMaxLength(letter,s,k) )

        return ans
        