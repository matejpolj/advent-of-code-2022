import sys
from string import ascii_lowercase
from collections import deque


def main1():
    def getNext(x: int, y: int) -> list:
        return [i for i in [(x-1, y), (x+1,y), (x, y-1), (x, y+1)] if i[0] >= 0 and i[0] <= xmax and i[1] >= 0 and i[1] <= ymax if landscape.get(i) - landscape.get((x, y)) < 2]
    height = lambda v: list('S'+ascii_lowercase+'E').index(v) if v in 'S'+ascii_lowercase+'E' else None
    input_text = [list(r) for r in open("input12.txt", 'r').read().splitlines()]
    landscape = {(x,y):height(v) for y, r in enumerate(input_text) for x, v in enumerate(r)}
    xmax, ymax = len(input_text[0])-1, len(input_text)-1
    start = [c for c, v in landscape.items() if v == 0][0]
    end = [c for c, v in landscape.items() if v == 27][-1]
    qpoint, qvalue = deque([(0, start[0], start[1])]), deque([(0, start[0], start[1])])
    while qpoint:
        number_steps, next_x, next_y = qpoint.popleft()
        if (next_x, next_y) == end: break
        if (next_x, next_y) in qvalue: continue
        qvalue.append((next_x, next_y))
        for nnx, nny in getNext(next_x, next_y):
            qpoint.append((number_steps+1, nnx, nny))
    print(min([nums for nums, numx, numy in qpoint]))


def main2():
    def getNext(x: int, y: int) -> list:
        return [i for i in [(x-1, y), (x+1,y), (x, y-1), (x, y+1)] if i[0] >= 0 and i[0] <= xmax and i[1] >= 0 and i[1] <= ymax if landscape.get(i) - landscape.get((x, y)) < 2]
    height = lambda v: list('S'+ascii_lowercase+'E').index(v) if v in 'S'+ascii_lowercase+'E' else None
    input_text = [list(r) for r in open("input12.txt", 'r').read().splitlines()]
    landscape = {(x,y):height(v) for y, r in enumerate(input_text) for x, v in enumerate(r)}
    xmax, ymax = len(input_text[0])-1, len(input_text)-1
    start = [c for c, v in landscape.items() if v <= 1]
    end = [c for c, v in landscape.items() if v == 27][-1]
    aa = list()
    for s in start:
        qpoint, qvalue = deque([(0, s[0], s[1])]), deque([(0, s[0], s[1])])
        while qpoint:
            number_steps, next_x, next_y = qpoint.popleft()
            if (next_x, next_y) == end: break
            if (next_x, next_y) in qvalue: continue
            qvalue.append((next_x, next_y))
            for nnx, nny in getNext(next_x, next_y):
                qpoint.append((number_steps+1, nnx, nny))
        if len(qpoint): 
            aa.append(min([nums for nums, numx, numy in qpoint]))
            print(min([nums for nums, numx, numy in qpoint]))
    print(min(aa))


if __name__ == '__main__':
    sys.exit(main2())
