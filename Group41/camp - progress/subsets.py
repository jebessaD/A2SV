class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        ans.add(tuple([]))

        def backtrack(curr,cand):
            curr.append(nums[cand])
            ans.add(tuple(curr.copy()))
            
            for i in range(cand + 1,len(nums)):
                backtrack(curr,i)

            curr.pop()
            
        for i in range(len(nums)):
            backtrack([],i)

        return list(ans)
