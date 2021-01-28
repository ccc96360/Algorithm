#BOJ1010 다리 놓기 20210128
import sys
input = sys.stdin.readline

def main():
    li = [list(range(1,31))]; cnt = 9
    for i in range(29):
        tmp = [0]*30
        li.append(tmp)

    for i in range(1, 30):
        for j in range(i,30):
            if i == j:
                li[i][j] = 1
            else:
                li[i][j] = li[i][j-1] + li[i-1][j-1]
    for __ in range(int(input())):
        n,m = map(int, input().split(" "))
        print(li[n-1][m-1])
if __name__ == '__main__':
    main()