"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        self.ans = 0
        visited = set()

        def dfs(id):
            visited.add(id)
            for employee in employees:
                if employee.id == id:
                    self.ans += employee.importance
                    for sub_ord in employee.subordinates:
                        if sub_ord not in visited:
                            dfs(sub_ord)
                            
        dfs(id)

        return self.ans



