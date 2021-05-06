#BOJ1092 배 20210506
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    cranes = list(sorted(list(map(int,input().rstrip().split()))))
    m = int(input())
    boxes = list(sorted(list(map(int,input().rstrip().split()))))
    if boxes[0] > cranes[-1] or boxes[-1] > cranes[-1]:
        return print(-1)

    jobs = [deque() for _ in range(n)]
    idx = 0
    for v in boxes:
        while v > cranes[idx]:
            idx += 1
        jobs[idx].append(v)


    cnt = time = 0
    while cnt < m:
        time += 1
        for i in range(n):
            idx = i
            while not jobs[idx] and idx > 0:
                idx -= 1
            if jobs[idx]:
                jobs[idx].popleft()
                cnt += 1
    print(time)

if __name__ == '__main__':
    main()