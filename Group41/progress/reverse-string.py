class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead. 
        2 pointers
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

#second solution tilde (~) bitwise operator
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead. 
        2 pointers
        """
        for ind in range(len(s)//2):
            s[ind],s[~ind]=s[~ind],s[ind]