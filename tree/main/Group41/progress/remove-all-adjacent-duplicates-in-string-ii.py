class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i,char in enumerate(s):

            if stack and stack[-1][0] == char:
                stack[-1][1]+=1
            else:
                stack.append([char,1])

            if stack and stack[-1][1] == k:
                stack.pop()

        ans = ""
        for letter,freq in stack:
            ans += letter * freq

        return ans
            

            

        