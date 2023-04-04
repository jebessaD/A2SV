class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.max_num = 0
        self.ans = 0
        for num in nums:
            self.max_num |= num
        
        def backtrack(curr,cand,bit_or):
            curr.append(cand)
            bit_or = bit_or | nums[cand]

            if bit_or == self.max_num:
                self.ans += 1

            for i in range(cand+1,len(nums)):
                backtrack(curr,i,bit_or)
                
            curr.pop()
            bit_or = 0
            for j in curr:
                bit_or |= nums[j] 
            
        for i in range(len(nums)):
            backtrack([],i,0)

        return self.ans

    
            