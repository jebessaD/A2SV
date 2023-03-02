class Solution:
    def reverseString(self, s: List[str] , left = 0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if left >= len(s)//2:
            return

        s[left],s[~left] = s[~left],s[left]
        self.reverseString(s,left + 1)