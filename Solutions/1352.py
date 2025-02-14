class ProductOfNumbers:

    """
    Stores prefix products, divide last product by (|prefix_prod| - (k + 1))th product
    """

    def __init__(self):
        self.prefix_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod = [0] * len(self.prefix_prod) + [1]
        else:
            self.prefix_prod.append(self.prefix_prod[-1] * num) 

    def getProduct(self, k: int) -> int:
        divider = self.prefix_prod[len(self.prefix_prod) - (k + 1)]
        if divider == 0:
            return 0
        return self.prefix_prod[-1] // divider

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
