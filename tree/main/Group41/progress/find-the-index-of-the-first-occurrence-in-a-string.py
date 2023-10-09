class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        p1 = 0
        p2 = 0
        Flag = False
        
        while p1 < len(haystack) and p2 < len(needle):
            ans = p1
            while p1 < len(haystack) and p2 < len(needle) and haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
                
            if p2 == len(needle):
                Flag = True
                return ans
            
            p1 = ans + 1
            p2 = 0
            
        if not Flag:
            return -1
            
            
                
            
            