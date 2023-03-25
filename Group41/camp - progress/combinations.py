class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr,cand,n,k):
            curr.append(cand)
            if len(curr) == k:
                ans.append(curr.copy())
                curr.pop()
                return

            for i in range(cand+1,n+1):
                backtrack(curr,i,n,k)
            curr.pop()
        
        for i in range(1,n+1):
            backtrack([],i,n,k)
            
        return ans