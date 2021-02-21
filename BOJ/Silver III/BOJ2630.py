#BOJ2630 색종이 만들기 20210221
import sys
input = sys.stdin.readline

WHITE = 0
BLUE = 1

def isOneColor(li):
    n = len(li)
    target = li[0][0]
    for i in range(n):
        for j in range(n):
            if li[i][j] != target:
                return -1
    if target == WHITE: return WHITE
    return BLUE
def divide(li):
    white,blue = 0, 0
    if isOneColor(li) == WHITE:
        return 1, 0
    elif isOneColor(li) == BLUE:
        return 0, 1
    else:
        n = len(li)
        parts = [[],[],[],[]]
        for i in range(n//2):
            parts[0].append(li[i][:n//2])
            parts[1].append(li[i][n//2:])
        for i in range(n//2, n):
            parts[2].append(li[i][:n//2])
            parts[3].append(li[i][n//2:])
        for part in parts:
            a,b = divide(part)
            white += a
            blue += b
        return white, blue
def main():
    n = int(input().rstrip())
    li = []
    for _ in range(n):
        li.append(list(map(int, input().rstrip().split())))
    white, blue = divide(li)
    print(white, blue, sep="\n")
if __name__ == '__main__':
    main()