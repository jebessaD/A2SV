class Solution:
    def countVowels(self, word: str) -> int:
        #
        dp = [0] * len(word)
        dp[0] = 1 if word[0] in "aeiou" else 0
        
        for i in range(1,len(word)):
            if word[i] in "aeiou":
                dp[i] = dp[i-1] + i+1
            else:
                dp[i] = dp[i-1]
            
        return sum(dp)