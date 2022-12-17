
def getElevation(A):
    if (A == 'S'):
        return 0
    elif (A == 'E'):
        return 27
    else:
        return ord(A)%96


def createLandscape(I):
    L = []
    for i in range(len(I)):
        L.append([])
        for j in range(len(I[i])-1):
            L[i].append(getElevation(I[i][j]))
    return L


def createVisited(L):
    return [[0 for x in range(len(L[0]))] for y in range(len(L))]


def findStartAndEnd(L):
    sx, sy = 0, 0
    ex, ey = 0, 0
    for i in range(len(L)):
        for j in range(len(L[i])):
            if (L[i][j] == 0):
                sx, sy = i, j
            elif (L[i][j] == 27):
                ex, ey = i, j
    return sx, sy, ex, ey


def canMove(x, y, a, b):
    if ((a < 0 or b < 0) or (a >= len(landscape) or b >= len(landscape[0]))):
        return False
    if ((visited[a][b] == 1) or abs(landscape[x][y] - landscape[a][b]) > 1):
        return False
    return True


def travel(xx, xy):
    global length, shortestLength, visited, foundPath, endx, endy
    if (xx == endx and xy == endy):
        foundPath = True
        shortestLength = min(shortestLength, length)
        return
    visited[xy][xx] = 1
    length += 1
    if (canMove(xy, xy, xx+1, xy)):
        travel(xx+1, xy)
    if (canMove(xy, xy, xx, xy+1)):
        travel(xx, xy+1)
    if (canMove(xy, xy, xx-1, xy)):
        travel(xx-1, xy)
    if (canMove(xy, xy, xx, xy-1)):
        travel(xx, xy-1)
    visited[xx][xy] = 0
    length -= 1


def findPath():
    travel(startx, starty)


lines = []
landscape = []
visited = []
startx, starty, endx, endy = 0, 0, 0, 0
shortestLength = 2**20
length = 0
foundPath = False

def main():
    global lines, landscape, visited, startx, starty, endx, endy
    with open('input12.txt') as f:
        lines = f.readlines()
        landscape = createLandscape(lines)
        visited = createVisited(landscape)
        startx, starty, endx, endy = findStartAndEnd(landscape)
        findPath()

if __name__ == '__main__':
    main()
    if foundPath:
        print(f"Shortest Path Length: {shortestLength}")
    else:
        print("No Path Possible")
