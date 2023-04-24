class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_nodes = set()

        for out,in_ in edges:
            in_nodes.add(in_)

        return [ node for node in range(n) if node not in in_nodes]

