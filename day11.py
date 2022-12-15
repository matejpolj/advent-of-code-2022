
class Monkey:
    def __init__(self, int, items, div, operation, operand):
        self.i = int
        self.count = 0
        self.items = items
        self.divisor = div
        self.operation = operation
        self.operand = operand
        self.round = 0

    def __str__(self):
        return f"Monkey {self.i}: {self.count}, {self.items, self.divisor, self.operation, self.operand. self.t.ind, self.f.ind}"

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
            self.items[i] //= 3
            if ((self.items[i]%self.divisor) == 0):
                self.t.addItem(self.items.pop())
            else:
                self.f.addItem(self.items.pop())
            self.count += 1


def decodeOne(l):
    items = []
    operation = 0
    operand = -1
    divisor = 0
    if (l[2][23] == '+'):
        operation = 1
    elif (l[2][23] == '*'):
        if (l[2][25:len(l[2])] == 'old\n'):
            operation = 0
        else:
            operation = 2
    if (operation > 0):
        print(l[2][25:len(l[2])], operation)
        operand = int(l[2][25:len(l[2])])
    divisor = int(l[3][21:len(l[3])])
    itm = l[1].split()
    items = [int(x[0:2]) for x in itm[2:len(itm)]]
    #print(items, operation, operand, divisor)
    return items, divisor, operation, operand
    

def decodeTwo(l):
    t = int(l[4][29:len(l[4])])
    f = int(l[5][30:len(l[5])])
    return t, f


with open('input11.txt') as f:
    lines = f.readlines()
    monkeys = []
    #print(lines, decodeOne(lines[7:13]), decodeTwo(lines[7:13]))
    for i in range(0, (len(lines)), 7):
        print(lines[(i):(i + 6)])
        itm, di, op, opr = decodeOne(lines[(i):(i + 6)])
        monkeys.append(Monkey(i, itm, di, op, opr))
    for i in range(0, len(lines), 7):
        t, f = decodeTwo(lines[i:(i+6)])
        monkeys[i].setOthers(monkeys)
