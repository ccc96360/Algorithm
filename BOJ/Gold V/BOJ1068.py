#BOJ1068 트리 20210511
import sys
input = sys.stdin.readline

ALIVE = 1
DEAD = 2
class Node:
    def __init__(self, num):
        self.num = num
        self.parent = -1
        self.children = set()        
        self.status = ALIVE

def findLeaf(node):
    if node.status == DEAD: return 0
    if not node.children:
        return 1
    ret = 0
    childrenAllDead = True
    for v in node.children:
        if v.status == ALIVE: childrenAllDead = False
        ret += findLeaf(v)
    if childrenAllDead: ret = 1
    return ret

def killNode(node):
    node.status = DEAD
    for v in node.children:
        killNode(v)

def main():
    n = int(input())

    tree = [Node(i) for i in range(n)]
    root = -1
    parents = list(map(int, input().rstrip().split()))
    for i in range(n):
        tree[i].parent = parents[i]
        if parents[i] != -1:
            tree[parents[i]].children.add(tree[i])
        else:
            root = i

    k = int(input())
    killNode(tree[k])
    print(findLeaf(tree[root]))

if __name__ == '__main__':
    main()