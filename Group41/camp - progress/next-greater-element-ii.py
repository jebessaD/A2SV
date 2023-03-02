class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n *2
        stack = []
        nums = nums + nums
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                ans[index] = nums[i]
            stack.append(i)

        return ans[:n]