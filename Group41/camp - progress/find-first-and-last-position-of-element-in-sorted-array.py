class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findIndex(nums,target,order):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                mid = left + (right - left)//2
                if order == "increasing":
                    operation = nums[mid] < target
                else:
                    operation = nums[mid] > target

                if operation:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        first = findIndex(nums,target,"increasing")
        second = findIndex(nums[::-1],target,"decreasing")

        if first >= len(nums) or nums[first] !=target:
            return [-1,-1]
        return [first,len(nums) - second - 1]
        