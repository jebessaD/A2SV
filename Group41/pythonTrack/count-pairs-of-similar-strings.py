class Solution:
    def similarPairs(self, words: List[str]) -> int:
        new_words= list(map(set,words))
        ans=0
        for i in range(len(new_words)):
            for j in range(i+1,len(new_words)):
                if new_words[i]==new_words[j]:
                    ans+=1

        
        return ans