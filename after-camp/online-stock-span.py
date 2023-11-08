class StockSpanner:

    def __init__(self):
        self.ans = []
        self.prices = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        self.ans.append(0)
        while self.prices and self.prices[-1][0] <= price:
            pr,ind = self.prices.pop()
            self.ans[self.index] += self.ans[ind]

        self.prices.append((price,self.index))
        self.ans[self.index] += 1
        return self.ans[self.index]
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)