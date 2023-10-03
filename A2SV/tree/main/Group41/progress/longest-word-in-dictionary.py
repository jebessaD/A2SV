class TrieNode:
    def __init__(self):
        self.children = {}
        

class Solution:
    def __init__(self):
        self.root = TrieNode() 

    def longestWord(self, words: List[str]) -> str:
        
        words.sort()
        words = sorted(words, key=len)
        
        longest = ""
        for word in words:
            flag = True
            curr = self.root
            
            for ind,char in enumerate(word):
                if char not in curr.children:
                    if ind < len(word)-1:
                        flag = False
                        break
                    curr.children[char] = TrieNode()
                else:
                    curr = curr.children[char]

            if flag:
                longest = max(longest,word,key=len)

        return longest