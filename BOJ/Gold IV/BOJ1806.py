#BOJ1806 부분합 20210328
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n,s = map(int,input().rstrip().split())
    li = list(map(int,input().rstrip().split()))
    sum_ = 0
    q = deque()
    mn = 100001
    for v in li:
        sum_ += v
        q.append(v)
        if sum_ >= s:
            while sum_ - q[0] >= s:
                sum_ -= q.popleft()
            mn = min(mn, len(q))
    print(mn if mn != 100001 else 0)
if __name__ == '__main__':
    main()