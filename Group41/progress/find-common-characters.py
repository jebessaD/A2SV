class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        store = Counter(words[0])
        for word in words:
            for letter in store:
                if letter not in word:
                    store[letter]=0
            for char in word:
                freq= word.count(char)
                if char in store:
                   store[char]=min(freq,store[char])
                else:
                    store[char]=0
        ans=[]
        for character in store:
            for value in range(store[character]):
                ans.append(character)

        return ans