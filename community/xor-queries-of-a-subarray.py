# https://leetcode.com/problems/xor-queries-of-a-subarray/submissions/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor=0
        prexors=[]
        for n in arr:
            prexor^=n
            prexors.append(prexor)
        prexors.append(0)
        ans=[]
        
        for i,j in queries:
            ans.append(prexors[i-1]^prexors[j])
        return ans