#BOJ9466 텀 프로젝트 20210329
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [0] + list(map(int,input().rstrip().split()))
    visited = [0] * (n+1)
    res = 0
    for i in range(1,n+1):
        if visited[i] == 0:
            k = i
            visited[k] = 1
            if li[k] == k:
                res += 1
                continue
            visitedNode = set()
            visitedNode.add(k)
            while visited[li[k]] == 0:
                visited[li[k]] = visited[k] + 1
                k = li[k]
                visitedNode.add(k)
                if li[k] in visitedNode:
                    res += visited[k] - visited[li[k]] + 1
    print(n-res)
if __name__ == '__main__':
    for _ in range(int(input())):
        main()