class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        store=set()
        for ind,box in enumerate(boxes):
            if box=="1":
                store.add(ind)
                
        ans=[0]*len(boxes)
        for ind in range(len(ans)):
            for num in store:
                if num !=ind:
                    ans[ind]+=abs(num - ind)

        return ans