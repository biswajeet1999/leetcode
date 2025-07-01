class StockSpanner:

    # def __init__(self):
    #     self.stocks = []
    #     self.stack = []

    # def next(self, price: int) -> int:
    #     stack = self.stack
    #     while len(stack) > 0 and self.stocks[stack[-1]] <= price:
    #         stack.pop()
        
    #     ans = 0
    #     if len(stack) == 0:
    #         ans = len(self.stocks) + 1
    #     else:
    #         ans = len(self.stocks) - self.stack[-1]
        
    #     self.stocks.append(price)
    #     self.stack.append(len(self.stocks) - 1)

    #     return ans

    
    def __init__(self):
        self.curDay = 0
        self.stack = [] # (price, day)

    def next(self, price: int) -> int:
        self.curDay += 1
        
        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            self.stack.pop()
        
        if len(self.stack) == 0:
            res = self.curDay - 0
        else:
            res = self.curDay - self.stack[-1][1]
        
        self.stack.append((price, self.curDay))
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)