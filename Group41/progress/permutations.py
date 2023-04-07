class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(candidate,bit_mask,ans):

            if len(candidate) == len(nums):
                ans.append(candidate.copy())
                return
                
            for i in range(len(nums)):
                if not(bit_mask & 1 << i):

                    bit_mask = bit_mask | 1 << i
                    candidate.append(nums[i])

                    backtrack(candidate,bit_mask,ans)
                    candidate.pop()

                    bit_mask = bit_mask ^ (1 << i)
 

        backtrack([],0,ans)

        return ans