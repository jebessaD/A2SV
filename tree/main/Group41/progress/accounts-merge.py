class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        parent = [ i for i in range(len(accounts) + 1)]
        rank = [1] * (len(accounts) + 1)
        
        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

        accountOwner = {}
        for i,user in enumerate(accounts):
            for account in user[1:]:
                if account in accountOwner:
                    union(accountOwner[account],i)
                else:
                    accountOwner[account] = i

        
        emails = defaultdict(list)
        for email, i in accountOwner.items():
            emails[find(i)].append(email)
        ans = []
        for inx,arr in emails.items():
            res = [accounts[inx][0]] + sorted(arr)
            ans.append(res)

        return ans
            