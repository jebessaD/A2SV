class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_anagram = Counter(p)
        s_anagram = Counter(s[:len(p)])
        left = right = 0
        res = []

        if p_anagram == s_anagram:
            res.append(left)

        for right in range(len(p),len(s)):
            s_anagram[s[left]] -= 1
            if s_anagram[s[left]] == 0:
                s_anagram.pop(s[left])
            left += 1

            s_anagram[s[right]] = s_anagram.get(s[right], 0) + 1
            if p_anagram == s_anagram:
                res.append(left)

        return res