class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        ans = []
        for ind in range(len(nums)-1):
            prefix.append(prefix[-1] * nums[ind])
            suffix.append(suffix[-1] * nums[~ind])
        suffix.reverse()
        
        return [ pre * suf for pre, suf in zip(prefix,suffix)]