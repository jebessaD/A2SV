class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        indegrees = defaultdict(int)
        
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                indegrees[recipes[i]] += 1

        queue = deque()
        visited = set()
        set_recipes = set(recipes)
        for sup in supplies:
            if not indegrees[sup]:
                queue.append(sup)
                visited.add(sup)
        ans = []

        while queue:
            parent = queue.popleft()
            if parent in set_recipes:
                ans.append(parent)

            for child in graph[parent]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)
                    visited.add(child)

        return ans
        