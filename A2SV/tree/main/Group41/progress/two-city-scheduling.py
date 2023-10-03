class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costa = 0
        diff = []
        for ca,cb in costs:
            costa += ca
            diff.append(cb-ca)
        diff.sort()
        return costa + sum(diff[:len(costs)//2])


        