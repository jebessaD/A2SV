class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = {}
        for ind,char in enumerate(s):
            if char in store:
                store[char]= (store[char][0],ind)
            else:
                store[char] = (ind,ind)
        minimum=0
        maximum=0
        output = []
        for x,y in store.values():
            if x > maximum:
                output.append(maximum - minimum + 1)
                minimum = x
                maximum = y
            minimum = min(minimum,x)
            maximum = max(maximum,y)

        output.append(maximum - minimum + 1)

        return output