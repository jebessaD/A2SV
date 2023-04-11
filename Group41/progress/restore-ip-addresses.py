class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def checkRange(num):
            if num and not ( len(num) > 1 and num[0] == "0"):
                return 0 <= int(num) <= 255
            return False

        ans = []
        def backtrack(ans,curr):
            if len(curr) == 4 and checkRange(s[curr[-1] : ]):
                valid_ip = f'{s[curr[0]:curr[1]]}.{s[curr[1]:curr[2]]}.{s[curr[2]:curr[3]]}.{s[curr[3]:]}'
                ans.append(valid_ip)
                return 

            for i in range( curr[-1] + 1 ,len(s) + 1):
                if checkRange(s[curr[-1] : i]) :
                    curr.append(i)
                    backtrack(ans,curr)
                    curr.pop()


        backtrack(ans,[0])    
        return ans
