class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum_word=strs[0]
        for word in strs:
            if len(word)<len(minimum_word):
                minimum_word=word
        i=0
        for letter in minimum_word:
            for word in strs:
                if word[i]!=letter:
                    return minimum_word[:i]
            i+=1
        return minimum_word 
        