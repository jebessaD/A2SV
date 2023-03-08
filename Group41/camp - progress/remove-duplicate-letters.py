class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        last_index = {}
        for i,char in enumerate(s):
            last_index[char] = i

        stack = []
        visited = set()
        for i , char in enumerate(s):
            while stack and s[stack[-1]] > char and last_index[s[stack[-1]]] > i and not char in visited:
                letter = stack.pop()
                visited.remove(s[letter])

            if char not in visited:
                stack.append(i)
                visited.add(char)

        return "".join([s[ind] for ind in stack])
        