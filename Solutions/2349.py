class NumberContainers:

    def __init__(self):
        self.numbers = defaultdict(int)  # index -> elemnt
        self.indices = defaultdict(SortedList)  # element -> indexes

    def change(self, index: int, number: int) -> None:
        # remove index if exist
        if self.numbers[index]:
            self.indices[self.numbers[index]].remove(index)

        self.numbers[index] = number
        self.indices[number].add(index)

    def find(self, number: int) -> int:
        return self.indices[number][0] if self.indices[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
