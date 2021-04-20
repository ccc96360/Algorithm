#BOJ2250 트리의 높이와 너비 20210420
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def findRoot(parent,leafNode):
    while parent[leafNode] != -1:
        leafNode = parent[leafNode]
    return leafNode

LEFT = 0
RIGHT = 1
column = 1
mxLev = 0
def dfs(v,adj,lev,nodeInfo):
    global column, mxLev
    if v != - 1:
        mxLev = max(mxLev,lev)
        dfs(adj[v][LEFT],adj,lev+1, nodeInfo)
        nodeInfo[v] = (lev,column)
        column += 1
        dfs(adj[v][RIGHT],adj,lev+1, nodeInfo)

def main():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    parent = [-1] * (n+1)
    leafNode = 0
    for _ in range(n):
        p,*child = map(int,input().rstrip().split())
        adj[p].extend(child)
        for v in child:
            if v != -1: parent[v] = p
        if child == [-1,-1]:
            leafNode = p
    root = findRoot(parent,leafNode)

    nodeInfo = [0 ] * (n+1)
    dfs(root,adj,1,nodeInfo)

    dic = {lev+1 : {"left" : n+1, "right":0} for lev in range(mxLev)}
    for lev, column in nodeInfo[1:]:
        dic[lev]["left"] = min(dic[lev]["left"], column)
        dic[lev]["right"] = max(dic[lev]["right"], column)

    width = lambda x: x[1]["right"] - x[1]["left"] + 1
    a = sorted(dic.items(), key=lambda x: (-(width(x)), x[0]))
    print(a[0][0], width(a[0]))
    
if __name__ == '__main__':
    main()