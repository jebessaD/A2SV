class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=""
        i=len(s)-1
        while i >= 0:
            if s[i]=="#":
                num=s[i-2:i]
                i-=2
            else:
                num=s[i]

            ans+=chr(int(num)+ord("a")-1)
            i-=1
        return ans[::-1]



                




