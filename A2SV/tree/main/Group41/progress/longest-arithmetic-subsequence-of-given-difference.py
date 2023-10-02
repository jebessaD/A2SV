class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = defaultdict(int)
        ans = 0
        for num in arr:
            dic[num] = 1 + dic[num - difference ]
            ans = max(ans,dic[num])
       
        return ans
        
        