class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        bit_array = []
        for word in words:
            bit = 0
            for letter in word:
                bit = bit | (1 << ord(letter) - 97)
            bit_array.append((bit,len(word)))

        ans = 0
        for bit_word1,length1 in bit_array: 
            for bit_word2,length2 in bit_array:
                if not( bit_word1 & bit_word2):
                    ans = max(ans, length1 * length2)
        
        return ans