class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        def gcd(num1,num2):
            if num2==0:
                return num1
            return gcd(num2,num1%num2)

        count = 0
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i,len(nums)):
                num = gcd(num,nums[j]) 
                if gcd(num,nums[j]) == k:
                    count += 1
                elif num < k:
                    break
                        
        return count
        