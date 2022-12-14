
class Monkey:
    def __init__(self, int, items, div, operation, operand):
        self.i = int
        self.count = 0
        self.items = items
        self.divisor = div
        self.operation = operation
        self.operand = operand

    def __str__(self):
        return f"Monkey {self.i}: self.count"

    def setOthers(self, T, F):
        self.t = T
        self.f = F
    
    def addItem(self, item):
        self.items.append(item)

    def inspectItems(self):
        for i in range(0, len(self.items)):
            if (self.operation == 0):
                self.items[i] = self.items[i] * self.items[i]
            elif (self.operation == 1):
                self.items[i] = self.items[i] + self.operand
            elif (self.operation == 2):
                self.items[i] = self.items[i] * self.operand
            self.items[i] /= 3
            self.t.addItem(self.items.pop())


with open('input11.txt') as f:
    lines = f.readlines()
