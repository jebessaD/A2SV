class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index={}
        for i in range(len(s)):
            if(s[i] not in index ):
                index[s[i]]=[i,i]
            else:
                index[s[i]][1]=i
            
        l,r=index[s[0]]
        output=[]
        
        for k in index.keys():
            a,b=index[k]
            if(r+1==a):
                output.append(r-l+1)
                l=a
                r=b
            elif(b>r and a>l):
                r=b
                
        output.append(r-l+1)   
        return output
                