#BOJ10775 공항 20210421
import sys
input = sys.stdin.readline

def find(v,parent):
    if v == parent[v]:
        return v
    else:
        parent[v] = find(parent[v],parent)
        return parent[v]

def union(a,b,parent):
    a = find(a,parent)
    b = find(b,parent)
    if a != b:
        parent[b] = a
def main():
    g,p = [int(input()) for _ in range(2)]
    airplane = [int(input()) for _ in range(p)]
    parent = [i for i in range(g+1)]
    cnt = 0
    for v in airplane:
        idx = find(v,parent)
        if idx == 0: break
        cnt += 1
        parent[idx] -= 1
        union(idx, v, parent)
    print(cnt)

if __name__ == '__main__':
    main()