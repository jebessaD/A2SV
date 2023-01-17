class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans=[]
        rev=[]
        for letter in s:
            if(letter==")"):
                for i in reversed(ans):
                    if i=="(":
                        # rev.append(ans.pop())
                        ans.pop()
                        break
                    else:
                        rev.append(ans.pop())
                ans.extend(rev)
                rev=[]
            else:
                ans.append(letter)
        s=""
        return s.join(ans)
        