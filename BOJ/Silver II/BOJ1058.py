#BOJ1058 친구 20210609
import sys
input = sys.stdin.readline

def get2Friends(v, adj):
    friends = set()
    for nv in adj[v]:
        friends.add(nv)
        for nv2 in adj[nv]:
            if nv2 != v: friends.add(nv2)
    return friends
def main():
    n = int(input())
    li = [list(input().rstrip()) for _ in range(n)]
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if li[i][j] == "Y": 
                adj[i].append(j)
    mx = 0
    for i in range(n):
        friends = get2Friends(i, adj)
        mx = max(mx, len(friends))
    print(mx)
if __name__ == '__main__':
    main()