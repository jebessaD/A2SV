class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
#         
        n = len(img1)
        
        def inBound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        
        def check(r_shift, c_shift):
            count = 0
            
            for r in range(n):
                for c in range(n):
                    if inBound(r + r_shift, c + c_shift):
                        if img1[r+r_shift][c + c_shift] and img2[r][c]:
                            count += 1
            return count
        
        ans = 0
        
        for r in range(-n, n):
            for c in range(-n, n):
                ans = max(ans, check(r, c))
        return ans 