class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        def backtrack(curr,cand_ind):
            
            curr.append(nums[cand_ind])
            if len(curr) >= 2:
                self.ans.add(tuple(curr.copy()))
            
            for i in range(cand_ind+1,len(nums)):
                if nums[i] >= nums[cand_ind]:
                    backtrack(curr,i)
                
            curr.pop()

        for j in range(len(nums)):
            backtrack([],j)

        return list(self.ans)