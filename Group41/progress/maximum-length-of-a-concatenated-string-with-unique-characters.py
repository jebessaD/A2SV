class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0

        def backtrack(curr,cand):
            
            curr.append(arr[cand])
            strs = "".join(curr)
            if len(strs) == len(set(strs)):
                self.ans = max(self.ans,len(strs))

            for i in range(cand+1,len(arr)):
                backtrack(curr,i)
            curr.pop()

        for i in range(len(arr)):
            backtrack([],i)

        return self.ans


        