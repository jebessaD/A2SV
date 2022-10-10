# https://leetcode.com/problems/bag-of-tokens/submissions/
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l=score=ans=0
        r=len(tokens)-1
        while l<=r:
            if(power>=tokens[l]):
                power-=tokens[l]
                score+=1
                l+=1
            elif(score>=1):
                ans=max(ans,score)
                score-=1
                power+=tokens[r]
                r-=1
            else:
                return ans
            
        return max(score,ans)