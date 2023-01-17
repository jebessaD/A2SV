class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        print(nums)
        list_index=[]
        for i in range(len(nums)):
            if(target==nums[i]):
                list_index.append(i)
                print(list_index)
        
        return(list_index)
        