class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        for letter1,letter2 in zip(word1,word2):
            ans+=letter1
            ans+=letter2
        if len(word1)>len(word2):
            return ans + word1[len(word2):]
        else:
            return ans + word2[len(word1):]
           