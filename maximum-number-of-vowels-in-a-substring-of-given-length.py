class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        print(s)
        vowels={"a","e","i","o","u"}
        l=r=count=ans=0
        while r<len(s):
            if(s[r] in vowels):
                count+=1
            if r-l==k-1:
                ans=max(ans,count)
                if(s[l] in vowels):
                    count-=1
                l+=1
              
            r+=1
        return ans