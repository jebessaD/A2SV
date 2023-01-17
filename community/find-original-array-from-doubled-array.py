class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        result=[]
        dicts={}
        for i in changed:
            if i in dicts.keys():
                dicts[i]+=1
            else:
                dicts[i]=1
                

        for i in dicts.keys():
            for j in range(dicts[i]):
                if i*2 in dicts.keys():
                    if dicts[i]!=0 and dicts[i*2]!=0:
                        dicts[i]-=1
                        dicts[i*2]-=1
                        result.append(i)
          
        for i in dicts.keys():
            if dicts[i]!=0:
                result=[]
            
        return result
  