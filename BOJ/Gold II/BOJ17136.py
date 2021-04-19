#BOJ17136 색종이 붙이기 20210419
import sys
input = sys.stdin.readline

CAN_FILL = 1
FILLED = 2

numOne = 0
ans = 30
def canN(li,n,r,c):
    if r + n - 1 >= 10 or c + n - 1 >= 10: return False
    for i in range(r,r+n):
        for j in range(c,c+n):
            if li[i][j] != 1:
                return False
    return True

def fillKbyN(li,k,n,r,c):
    for i in range(r,r+n):
        for j in range(c,c+n):
            li[i][j] = k

def nextOne(li):
    for r in range(10):
        for c in range(10):
            if li[r][c] == 1: return (r,c)

def solve(li,leftPaper,size):
    global numOne,ans
    if numOne == 0:
        ans = min(ans,size)
    else:
        r,c = nextOne(li)
        size += 1
        for i in range(1,6):
            if leftPaper[i] > 0 and canN(li,i,r,c):
                fillKbyN(li,FILLED,i,r,c)
                leftPaper[i] -= 1
                numOne -= i**2
                
                solve(li,leftPaper,size)

                numOne += i**2
                leftPaper[i] += 1
                fillKbyN(li,CAN_FILL,i,r,c)

def main():
    li = [list(map(int,input().rstrip().split())) for _ in range(10)]
    ones = []
    leftPaper = [0,5,5,5,5,5]
    global numOne
    for i in range(10):
        for j in range(10):
            if li[i][j] == 1:
                ones.append((i,j))
                numOne += 1
    solve(li,leftPaper,0)
    print(ans if ans != 30 else -1)
if __name__ == '__main__':
    main()