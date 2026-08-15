class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        counter = 1
        while len(self.stocks) > 0 and price >= self.stocks[-1][0]:
            counter += self.stocks[-1][1]
            self.stocks.pop()
        self.stocks.append((price, counter))
        return counter


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)