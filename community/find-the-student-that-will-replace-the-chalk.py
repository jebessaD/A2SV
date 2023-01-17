class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k=k%sum(chalk)
        presum=0
        for i,n in enumerate(chalk):
            presum+=n
            if(presum>k):
                return i