class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        queue = deque()
        visited = set()
        queue.append(0)

        while queue:
            parent = queue.popleft()
            visited.add(parent)
            for child in rooms[parent]:
                if child not in visited:
                    queue.append(child)
    
        return len(visited) == len(rooms)