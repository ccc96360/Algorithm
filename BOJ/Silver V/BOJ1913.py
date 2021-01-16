#BOJ1913 달팽이 20210116 
UP = 0; DOWN = 1; LEFT = 2; RIGHT = 3
def changeDir(dir):
    idx = (dir["idx"] + 1) % 4
    dir["idx"] = idx
    dir["curDir"] = dir["dir"][idx]
    return dir
def move(x,y,dir):
    curDir = dir["curDir"]
    if curDir == DOWN:
            y += 1
    elif curDir == UP:
        y -= 1
    elif curDir == LEFT:
        x -= 1
    elif curDir == RIGHT:
        x += 1
    return x,y

def main():
    dir = {"dir": [DOWN, RIGHT, UP, LEFT], "idx": 0, "curDir" : DOWN}
    n = int(input())
    t = int(input())
    li = [[0]*n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    x = 0; y = 0
    
    for i in reversed(range(1, (n**2)+1)):
        if i == t : ret = (y+1,x+1)
        li[y][x] = i
        visited[y][x] = True
        bx = x; by = y
        x,y = move(x,y,dir)
        if x == n or y == n:
            changeDir(dir)
            x,y = move(bx, by, dir)
        if visited[y][x]:
            changeDir(dir)
            x,y = move(bx, by, dir)
    for i in range(n):
        for j in range(n):
            print(li[i][j], end=" " if j != n-1 else "\n")
    print(ret[0],ret[1])
if __name__ == '__main__':
    main()