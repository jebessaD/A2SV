class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mydict={}
        length=len(arr)
        for i in arr:
            if i in mydict.keys():
                mydict[i]+=1
            else:
                mydict[i]=1
        sorted_dict= {k: v for k, v in sorted(mydict.items(), reverse=True, key=lambda item: item[1])}
        sum=0
        
        for i,num in enumerate(sorted_dict.keys()):
            sum+=sorted_dict[num]
            if sum >= length/2:
                return i+1
                
              
        