#BOJ1992 쿼드트리 20210307
import sys
input = sys.stdin.readline

def canCompress(n, li):
    a = li[0][0]
    for i in range(n):
        for v in li[i]:
            if a != v:
                return -1
    return a
def compress(n, li):
    a = canCompress(n, li) 
    if a != -1:
        return a
    l = [[],[],[],[]]
    for i in range(n//2):
        l[0].append(li[i][:n//2])
        l[1].append(li[i][n//2:])
    for i in range(n//2,n):
        l[2].append(li[i][:n//2])
        l[3].append(li[i][n//2:])
    res = ""
    for v in l:
        res += compress(n//2, v)
    return "(" + res + ")"
def main():
    n = int(input())
    li = [input().rstrip() for _ in range(n)]
    print(compress(n,li))
if __name__ == '__main__':
    main()