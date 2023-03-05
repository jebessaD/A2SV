class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = tickets[k]
        person_ticket = tickets[k]
        
        for i in range(k + 1,len(tickets)):
            if tickets[i] < person_ticket:
                time += tickets[i]
            else:
                time += person_ticket - 1
        
        for i in range(k):
            time += min(tickets[i],person_ticket)

        return time

# 2nd
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        person_ticket = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i],person_ticket)
            else:
                time += min(tickets[i],person_ticket - 1)

        return time

