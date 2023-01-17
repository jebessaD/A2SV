class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        length=len(nums)
        newArray=[0]*length
        for half in range(length//2):
            newArray[2*half+1]=nums[half]
            newArray[2*half]=nums[half-(length//2)]
            if (length%2!=0):
                newArray[length-1]=nums[length//2]    
        return(newArray)
        