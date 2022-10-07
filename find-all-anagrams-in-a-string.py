class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict=Counter(p)
        length=len(p)-1
        sub={}
        l=r=0
        ans=[]
        while r<len(s):
            if s[r] in sub:sub[s[r]]+=1
            else: sub[s[r]]=1
                
            if(r-l==length):
                if(sub==p_dict): ans.append(l)
                    
                if sub[s[l]]==1 : del sub[s[l]]
                else: sub[s[l]]-=1     
                l+=1
                
            r+=1
            
        return ans
        
        