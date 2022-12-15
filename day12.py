
def getElevation(A):
    if (A == 'a'):
        return 1
    elif (A == 'b'):
        return 2
    elif (A == 'c'):
        return 3
    elif (A == 'd'):
        return 4
    elif (A == 'e'):
        return 5
    elif (A == 'f'):
        return 6
    elif (A == 'g'):
        return 7
    elif (A == 'h'):
        return 8
    elif (A == 'i'):
        return 9
    elif (A == 'j'):
        return 10
    elif (A == 'k'):
        return 11
    elif (A == 'l'):
        return 12
    elif (A == 'm'):
        return 13
    elif (A == 'n'):
        return 14
    elif (A == 'o'):
        return 15
    elif (A == 'p'):
        return 16
    elif (A == 'q'):
        return 17
    elif (A == 'r'):
        return 18
    elif (A == 's'):
        return 19
    elif (A == 't'):
        return 20
    elif (A == 'u'):
        return 21
    elif (A == 'v'):
        return 22
    elif (A == 'w'):
        return 23
    elif (A == 'x'):
        return 24
    elif (A == 'y'):
        return 25
    elif (A == 'z'):
        return 26   
    elif (A == 'S'):
        return 1
    elif (A == 'E'):
        return 26
    else:
        return 0


# Python3 code to implement the approach
import sys

# User defined Pair class
class Pair:
    def __init__(self, x, y):
        self.first = x
        self.second = y

# Check if it is possible to go to (x, y) from the current
# position. The function returns false if the cell has
# value 0 or already visited
def isSafe(mat, visited, x, y, a, b):
    print('a')
    return (x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and (abs(mat[x][y] - mat[a][b]) <= 1) and (not visited[x][y]))

def findShortestPath(mat, visited, i, j, x, y, min_dist, dist):
    if (i == x and j == y):
        min_dist = min(dist, min_dist)
        return min_dist

    # set (i, j) cell as visited
    visited[i][j] = True

    # go to the bottom cell
    if (isSafe(mat, visited, i + 1, j, i, j)):
        min_dist = findShortestPath(
            mat, visited, i + 1, j, x, y, min_dist, dist + 1)

    # go to the right cell
    if (isSafe(mat, visited, i, j + 1, i, j)):
        min_dist = findShortestPath(
            mat, visited, i, j + 1, x, y, min_dist, dist + 1)

    # go to the top cell
    if (isSafe(mat, visited, i - 1, j, i, j)):
        min_dist = findShortestPath(
            mat, visited, i - 1, j, x, y, min_dist, dist + 1)

    # go to the left cell
    if (isSafe(mat, visited, i, j - 1, i, j)):
        min_dist = findShortestPath(
            mat, visited, i, j - 1, x, y, min_dist, dist + 1)

    # backtrack: remove (i, j) from the visited matrix
    visited[i][j] = False
    return min_dist

# Wrapper over findShortestPath() function
def findShortestPathLength(mat, src, dest):
    if (len(mat) == 0 or mat[src.first][src.second] == 0
        or mat[dest.first][dest.second] == 0):
        return -1

    row = len(mat)
    col = len(mat[0])

    # construct an `M × N` matrix to keep track of visited
    # cells
    visited = []
    for i in range(row):
        visited.append([None for _ in range(col)])

    dist = sys.maxsize
    dist = findShortestPath(mat, visited, src.first,
                            src.second, dest.first, dest.second, dist, 0)

    if (dist != sys.maxsize):
        return dist
    return -1

with open('input12.txt') as f:
    lines = f.readlines()

    # Driver code
    mat = []
    for i in range(0, len(lines)):
        mat.append([])
        for j in range(0, len(lines[i])):
            tmp = getElevation(lines[i][j])
            if (tmp):
                mat[i].append(tmp)
    print(mat)

    src = Pair(0, 0)
    dest = Pair(3, 4)
    dist = findShortestPathLength(mat, src, dest)
    if (dist != -1):
        print("Shortest Path is", dist)

    else:
        print("Shortest Path doesn't exist")



    
