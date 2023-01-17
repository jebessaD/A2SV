class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        size = len(strs[0])
        count=0
        for i in range(size):
            temp=strs[0][i]
            for word in strs:
                if temp > word[i]:
                    count+=1
                    break
                
                temp=word[i]

        return count