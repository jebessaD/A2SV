class Solution:
    def printVertically(self, s: str) -> List[str]:
        store={}
        arr=s.split(" ")
        size=max(map(len,arr))
        store=defaultdict(list)
        for word in arr:
            for i in range(size):
                print(word,i)
                if i>=len(word) and len(word)<size:
                    store[i].append(" ")
                else:
                    store[i].append(word[i])

        ans=[]
        for row in store.values():
            while row[-1]==" ":
                row.pop()
            ans.append("".join(row))

        return ans