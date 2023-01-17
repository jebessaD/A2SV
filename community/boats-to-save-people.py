class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        r=len(people)-1
        l=0
        count=0
        while(r>=l):
            count=0
            while(people[l]<=limit and count<2):
                count+=1
                people[l]+=people[r]
                r-=1
            r+=1
            l+=1
            
        return(l)
