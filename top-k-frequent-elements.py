class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        
        for i in nums:
            if i in mydict.keys():
                mydict[i]+=1
            else:
                mydict[i]=1
                
        sorted_dict= {k: v for k, v in sorted(mydict.items(), reverse=True, key=lambda item: item[1])}

        nums_set=[]
        for num in sorted_dict.keys():
            nums_set.append(num)
        return(nums_set[:k])