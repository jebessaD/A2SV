class Solution:
    def average(self, salary: List[int]) -> float:
        minimum=min(salary)
        maximum=max(salary)
        total=0
        for num in salary:
            if num!=minimum and num!=maximum:
                total +=num
        return total/(len(salary)-2)