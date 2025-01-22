from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.count = 0
        self.n = n
        self.discount = discount
        self.products_prices = {pid: price for pid, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        self.count += 1

        for pid, amt in zip(product, amount):
            bill += amt * (self.products_prices[pid])

        if self.count % self.n == 0:
            bill *= ((100 - self.discount) / 100)

        return bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)