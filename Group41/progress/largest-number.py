class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                num1 = int(str(nums[j]) + str(nums[j+1]))
                num2 = int(str(nums[j+1]) + str(nums[j]))
                
                if num2 > num1:
                    nums[j+1],nums[j] = nums[j],nums[j+1]
        
        return str(int("".join(list(map(str,nums)))))
  