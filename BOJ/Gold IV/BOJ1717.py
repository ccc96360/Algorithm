#BOJ1717 집합의 표현 20210324 유니온 파인드
import sys
input = sys.stdin.readline

parent = []

def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x,y):
    x = find(x)
    y = find(y)
    parent[y] = x

def main():
    global parent
    n,m = map(int,input().rstrip().split())
    parent = [i for i in range(n+1)]
    for ___ in range(m):
        cmd, a, b, = map(int, input().rstrip().split())
        if cmd == 1:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
        else:
            union(a,b)
if __name__ == '__main__':
    main()