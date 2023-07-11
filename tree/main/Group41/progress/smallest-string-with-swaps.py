class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        parent = {(c,index):(c,index) for index, c in enumerate(s)}

        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if p1 > p2:
                parent[p2] = p1
            else:
                parent[p1] = p2

        for i,j in pairs:
            union((s[i],i),(s[j],j))

        groups = defaultdict(list)
        for x,y in parent.items():
            heappush(groups[find(y)],x)

        ans = []
        for inx,char in enumerate(s):
            par = find((char,inx))
            letter = heappop(groups[par])
            ans.append(letter[0])
     
        return "".join(ans)

        