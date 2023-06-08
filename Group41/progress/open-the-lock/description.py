class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        nextMove = {"0": ["9", "1"],"1": ["0", "2"],"2": ["1", "3"],"3": ["2", "4"],"4": ["3", "5"],"5": ["4", "6"],"6": ["5", "7"],"7": ["6", "8"],"8": ["7", "9"],"9": ["8", "0"]}

        queue = deque()
        visited = set()

        queue.append(("0000",0))
        visited.add("0000")
        while queue:
           
            parent,level = queue.popleft()

            if parent == target:
                return level
            elif parent in deadends:
                continue

            for i in range(4):
                for key in nextMove[parent[i]]: 
                    next_key = list(parent)
                    next_key[i] = key
                    next_key_str = "".join(next_key)
                    if next_key_str not in visited:
                        queue.append((next_key_str,level + 1))
                        visited.add(next_key_str)

        return -1