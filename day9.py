
def decodeInp(L):
    x = 0
    y = 0
    if (L[0] == 'U'):
        y = int(L[2:len(L)])
    elif (L[0] == 'D'):
        y = -int(L[2:len(L)])
    elif (L[0] == 'L'):
        x = -int(L[2:len(L)])
    elif (L[0] == 'R'):
        x = int(L[2:len(L)])
    else:
        x = 0
        y = 0
    #print(L, x, y)
    return x, y


class Head:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def __str__(self):
        return f"Head: ({self.x}, {self.y})"

    def move(self, L):
        i, j = decodeInp(L)
        self.x = self.x + i
        self.y = self.y + j
        return i, j


class Tail:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = [[0, 0]]

    def __str__(self):
        return f"Tail: ({self.x}, {self.y})"

    def storePosition(self, H):
        for i in range(0, len(self.pos)):
            if ((self.x == self.pos[i][0]) and (self.y == self.pos[i][1])):
                return
        self.pos.append([self.x, self.y])
        return

    def followHead(self, H):
        if ((abs(H.x - self.x) > 1) or (abs(H.y - self.y) > 1)):
            if (H.x > self.x):
                self.x += 1
            elif (H.x < self.x):
                self.x -= 1
            if (H.y > self.y):
                self.y += 1
            elif (H.y < self.y):
                self.y -= 1
        self.storePosition(H)
            

with open('input09.txt') as f:
    lines = f.readlines()
    head = Head()
    tail1 = Tail()
    tail2 = Tail()
    tail3 = Tail()
    tail4 = Tail()
    tail5 = Tail()
    tail6 = Tail()
    tail7 = Tail()
    tail8 = Tail()
    tail9 = Tail()
    for i in range(0, len(lines)):
        x, y = head.move(lines[i])
        for i in range(0, abs(x + y)):
            tail1.followHead(head)
            tail2.followHead(tail1)
            tail3.followHead(tail2)
            tail4.followHead(tail3)
            tail5.followHead(tail4)
            tail6.followHead(tail5)
            tail7.followHead(tail6)
            tail8.followHead(tail7)
            tail9.followHead(tail8)
    print(len(tail9.pos))
