class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        balance = {5:0,10:0,20:0}
        for num in bills:
            if num == 5:
                balance[5] += 1
            elif num == 10:
                if balance[5] < 1:
                    return False
                balance[10] += 1
                balance[5] -= 1
            else:
                if balance[10] and balance[5] :
                    balance[10]-= 1
                    balance[5] -= 1    
                elif balance[5] >= 3:
                    balance[5] -= 3
                else:
                    return False

        return True