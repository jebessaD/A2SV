class Solution:
    def racecar(self, target: int) -> int:

        queue = deque()
        visited = set()

        queue.append(((0,1),0))
        visited.add((0,1))
        while queue:
            (pos,speed),level = queue.popleft()
            if pos == target:
                return level

            nextCommand = (pos + speed,speed * 2)
            if nextCommand not in visited:
                queue.append((nextCommand,level + 1))
                visited.add(nextCommand)

            reverse = -1 if speed > 0 else  1
            nextCommand = (pos,reverse)
            if nextCommand not in visited:
                queue.append((nextCommand,level + 1))
                visited.add(nextCommand)
