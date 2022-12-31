class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total=sum(map(lambda x: x if x%2==0 else 0,nums))
        print(total)
        ans=[]
        for val, index in queries:
            calc=nums[index]+val
            if calc %2 ==0 and nums[index]%2 !=0:
                total += calc
            elif calc %2==0 and nums[index]%2==0:
                total += calc - nums[index]
            elif calc %2 !=0 and nums[index]%2 ==0:
                total -= nums[index]
            nums[index]=calc
            ans.append(total)
        return ans
