class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dicts={}
        nums.sort()
        for i in nums:
            if i in dicts.keys():
                dicts[i]+=1
            else:
                dicts[i]=1
        counter=0
        
        for i in dicts.keys():
            for j in range(dicts[i]):
               
                if (k-i) in dicts.keys():
                    if i==k-i:
                        counter += dicts[i]//2
                        break
                    if dicts[i]!=0 and dicts[k-i]!=0:
                        counter+=1
                        dicts[i]-=1
                        dicts[k-i]-=1
                        
                        
        return counter