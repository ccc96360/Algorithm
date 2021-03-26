#BOJ2448 별 찍기-11 20210326
import sys
input = sys.stdin.readline

li = []
def star(r,c,k,width):
    global li
    if k == 0:
        li[r][c+2] = "*"
        li[r+1][c+1] = "*"
        li[r+1][c+3] = "*"
        for i in range(width):
            li[r+2][c+i] = "*"
    else:
        n = 3*(2**k)
        nn = 2**(k-1)
        nWidth = nn * 5 + nn - 1
        star(r+n//2, c, k - 1,nWidth)#left
        star(r,c + width//2-nWidth//2,k-1,nWidth)#top
        star(r+n//2, c + width-nWidth, k - 1,nWidth)#right
def main():
    global li
    n = int(input())
    m = n//3
    width = m * 5 + m - 1
    li = [[" " for _ in range(width)] for _ in range(n)]
    k = 0
    for i in range(11):
        if m == 2 ** i:
            k = i
    star(0,0,k,width)
    for v in li:
        print("".join(v))
if __name__ == '__main__':
    main()