#BOJ1697 숨바꼭질 20210302
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n,k = map(int, input().rstrip().split())
    q = deque([n])
    time = [0] * 200000
    while q:
        tmp = q.popleft()
        if tmp == k: break
        d = [1, -1, tmp]
        for i in range(3):
            next = tmp + d[i]
            if 0 <= next < 200000:
                if time[next] == 0:
                    time[next] = time[tmp] + 1
                    q.append(next)
    print(time[k])
if __name__ == '__main__':
    main()