# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=ans=0
        visited={}
        while r<len(s):
            if(s[r] not in visited):
                visited[s[r]]=r
                r+=1
            else:
                ans=max(len(visited),ans)
                val=list(visited.values()).copy()
                n=visited[s[r]]
                for index in val:
                    if(index>n):
                        break
                    del visited[s[index]]
                l=index
                
        ans=max(len(visited),ans)
        return ans
            
        