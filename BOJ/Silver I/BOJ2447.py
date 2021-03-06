#BOJ2447 별 찍기-10 20210306
import sys
input = sys.stdin.readline

def blank(n,x,y,li):
    for i in range(n):
        for j in range(n):
            li[y+j][x+i] = " "

def star(n,x,y,li):
    if n == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    li[y+i][x+j] = " "
                else: li[y+i][x+j] = "*"
    else:
        for i in range(y,y+n,n//3):
            for j in range(x,x+n,n//3):
                if i == y + n//3 and j == x + n//3:
                    blank(n//3,j,i,li)
                else:
                    star(n//3,j,i,li)
        
def main():
    n = int(input())
    li = [["" for _ in range(n)] for _ in range(n)]
    star(n,0,0,li)
    for i in range(n):
        for j in range(n):
            print(li[j][i],end="")
        print("")
if __name__ == '__main__':
    main()