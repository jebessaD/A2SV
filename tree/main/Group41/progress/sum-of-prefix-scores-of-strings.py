class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1
        
    def search(self, word):
        curr= self.root
        res = 0
        for char in word:
            curr = curr.children[char]
            res += curr.count

        return res
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = WordDictionary()
        for word in words:
            trie.addWord(word)

        ans = []
        for word in words:
            ans.append(trie.search(word))

        return ans
        