#BOJ1991 트리 순회 20210305
import sys
input = sys.stdin.readline

def order(f, n, adj):
    f(n, adj)
    print("")

def pre(n, adj):
    print(n,end="")
    for i in range(2):
        v = adj[n][i]
        if v != ".":
            pre(v, adj)

def _in(n,adj):
    if adj[n][0] != ".": _in(adj[n][0],adj)
    print(n, end="")
    if adj[n][1] != ".": _in(adj[n][1],adj)


def post(n,adj):
    for i in range(2):
        v= adj[n][i]
        if v != ".":
            post(v,adj)
    print(n,end="")

def main():
    adj = {}
    for _ in range(int(input())):
        a,b,c = input().rstrip().split()
        adj[a] = (b,c)
    order(pre, "A", adj)
    order(_in, "A", adj)
    order(post, "A", adj)
if __name__ == '__main__':
    main()