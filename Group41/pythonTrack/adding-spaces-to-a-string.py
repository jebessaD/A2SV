class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        left=0
        right=0
        ans=""
        while left<len(s):
            if len(spaces) > right and spaces[right]==left:
                ans+=" "
                right+=1
            else:
                ans+=s[left]
                left+=1
                
        return ans
                
                
                
        
            
        