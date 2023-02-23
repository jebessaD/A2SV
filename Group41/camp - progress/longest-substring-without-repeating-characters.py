class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        left = 0
        right = 0
        ans = 0

        while right < len(s):
            if s[right] in store:
                store.remove(s[left])
                left += 1
            else:
                store.add(s[right])
                right += 1
                ans = max(ans,right - left)

        return ans