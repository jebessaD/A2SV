class Solution:
    def compress(self, chars: List[str]) -> int:
        l=r=count=0
        while l<len(chars) and r<len(chars):
            if(chars[l]!=chars[r]):
                if(count==1):
                    l=r
                    count=0
                    continue
                chars[l+1:l+count]=list(str(count))
                count=0
                l+=2
                r=l-1
            else:
                count+=1     
            r+=1
        if count!=1:
            chars[l+1:l+count]=list(str(count))
            
                
                