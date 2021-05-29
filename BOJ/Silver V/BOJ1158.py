#BOJ1158 요세푸스 문제 20210529
import sys
from collections import deque
input = sys.stdin.readline


def main():
    n,k = map(int, input().rstrip().split())
    q = deque([i+1 for i in range(n)])
    res = []
    while q:
        for _ in range(k-1): q.append(q.popleft())
        res.append(q.popleft())
    print("<",end="")
    for i in range(n-1): print("{0}, ".format(res[i]), end="")
    print("{0}>".format(res[-1]))
if __name__ == '__main__':
    main()