class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
#        
# try this in trie - on progress sheet it is a trie question 
        ans = 0
        for i in range(31,-1,-1):
            prev = set([num>>i for num in nums])

            ans <<=1 
            cand = ans+1 

            for pre in prev:
                if cand ^ pre in prev:
                    ans = cand
                    break

        return ans
